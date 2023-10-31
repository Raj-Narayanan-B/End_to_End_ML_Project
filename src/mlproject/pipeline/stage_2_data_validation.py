from src.mlproject import logger
from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.data_validation import data_validation

class DataValidationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):  
        config = ConfigurationManager()
        validation_config = config.get_data_validation_config()
        data_validation_object = data_validation(config=validation_config)
        data_validation_object.data_validation()

stage = "Data Validation Stage"

if __name__=="__main__":
    try:
        logger.info(f"\n\n>>>>>{stage} Started<<<<<\n\n")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f"\n\n>>>>>{stage} Completed<<<<<\n\n")
    
    except Exception as e:
        logger.exception(e)
        raise e