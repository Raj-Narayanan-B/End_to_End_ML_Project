from src.mlproject import logger
from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.data_transformation import data_transformation

class DataTransformationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        schema_config = config.get_data_validation_config()

        with open(schema_config.data_val_status_path) as file:
            validation_status = file.read().split(" ")[-1]
        
        if validation_status == "True":
            data_transformation_config = config.get_data_transformation_config()
            obj = data_transformation(config= data_transformation_config)
            obj.data_transformation()
        else:
            raise Exception("Schema Mismatch!")

# stage_name = "Data Transformation Stage"

# if __name__ == "__main__":
#     try:
#         logger.info(f"\n\n>>>>>{stage_name} Started<<<<<\n\n")
#         obj = DataTransformationPipeline()
#         obj.main()
#         logger.info(f"\n\n>>>>>{stage_name} Completed<<<<<\n\n")
    
#     except Exception as e:
#         logger.exception(e)
#         raise e