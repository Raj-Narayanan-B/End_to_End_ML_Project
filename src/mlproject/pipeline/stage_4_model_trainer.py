from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.model_trainer import model_trainer
from src.mlproject import logger

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):            
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_obj = model_trainer(config= model_trainer_config)
        model_trainer_obj.train()

# stage_name = "Model Training Stage"

# if __name__=="__main__":
#     logger.info(f"\n\n>>>>>{stage_name} Started<<<<<\n\n")
#     obj = ModelTrainingPipeline()
#     obj.main()
#     logger.info(f"\n\n>>>>>{stage_name} Ended<<<<<\n\n")