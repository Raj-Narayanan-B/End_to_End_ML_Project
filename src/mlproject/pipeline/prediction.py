from src.mlproject.constants import *
from src.mlproject.utils.common import load_binary,load_yaml
from pathlib import Path #type: ignore
import pandas as pd

class PredictionPipeline:
    def __init__(self) -> None:
        self.config = load_yaml(CONFIG_PATH)
        self.model_path = self.config.model_trainer.model_name
        self.model = load_binary(Path(self.model_path))

    def prediction(self,data):
        data_df = pd.DataFrame(data,index=[0])
        pred = self.model.predict(data_df)

        return (pred)