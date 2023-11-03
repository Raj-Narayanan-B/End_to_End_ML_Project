from src.mlproject import logger
from src.mlproject.entity.config_entity import DataTransformationConfig

from pathlib import Path #type: ignore
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class data_transformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config

    def data_transformation(self):
        df = pd.read_csv(Path(self.config.data_path))

        train,test = train_test_split(df, test_size= 0.25, random_state= 8)

        train.to_csv(Path(self.config.train_path),index=False)
        logger.info("Train data saved")

        test.to_csv(Path(self.config.test_path),index=False)
        logger.info("Test data saved")

        print(train.shape)
        print(test.shape)