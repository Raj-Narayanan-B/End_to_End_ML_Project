from src.mlproject.constants import *
from src.mlproject.utils.common import load_binary,load_yaml
from pathlib import Path #type: ignore

class PredictionPipeline:
    def __init__(self) -> None:
        self.config = load_yaml(CONFIG_PATH)
        self.model_path = self.config.model_trainer.model_name
        self.model = load_binary(Path(self.model_path))

    def prediction(self,data):
        pred = self.model.predict(data)

        return (pred)