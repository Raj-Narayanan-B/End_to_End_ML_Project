import pandas as pd
import joblib
from sklearn.linear_model import ElasticNet
from src.mlproject.entity.config_entity import ModelTrainerConfig

class model_trainer:
    def __init__(self, config: ModelTrainerConfig) -> None:
        self.config = config

    def train(self):
        train = pd.read_csv(self.config.train)
        test = pd.read_csv(self.config.test)

        xtrain = train.drop(columns = self.config.target)
        xtest = test.drop(columns = self.config.target)

        ytrain = train[self.config.target]
        ytest = test[self.config.target]

        elastic_net = ElasticNet(alpha= self.config.alpha,
                                 l1_ratio= self.config.l1_ratio,
                                 random_state= 8)
        
        elastic_net.fit(xtrain,ytrain)

        joblib.dump(elastic_net,self.config.model)