from sklearn.metrics import mean_squared_error,r2_score
import numpy as np
import pandas as pd
from pathlib import Path #type: ignore

import mlflow
import mlflow.sklearn
from urllib.parse import urlparse #type: ignore

from src.mlproject.utils.common import load_binary,save_json
from src.mlproject.entity.config_entity import ModelEvaluation

class model_evaluation:
    def __init__(self, config: ModelEvaluation) -> None:
        self.config = config

    def eval_metrics(self, y_true, y_pred):
        rmse = np.sqrt(mean_squared_error(y_true=y_true, y_pred=y_pred))
        r2score = r2_score(y_true=y_true, y_pred=y_pred)
        return ({'rmse': rmse,
                 "r2_score": r2score})

    def ml_flow_logging(self):
        test_data = pd.read_csv(self.config.test_path)
        model = load_binary(Path(self.config.model_name))

        xtest = test_data.drop(columns=self.config.target)
        ytest = test_data[self.config.target]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            ypred = model.predict(xtest)

            scores = self.eval_metrics(y_true = ytest, y_pred = ypred)

            save_json(data = scores, path = Path(self.config.metrics))

            mlflow.log_params(self.config.parameters)

            mlflow.log_metric('rmse',scores['rmse'])
            mlflow.log_metric('r2_score',scores['r2_score'])

            if tracking_url_type != 'file':
                mlflow.sklearn.log_model(model,'model',registered_model_name='ElasticNet')
            else:
                mlflow.sklearn.log_model(model,'model')