from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject import logger

stage_name = "Data_Ingestion"

class DataIngestionPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zipfile()


if __name__=="__main__":
    try:
        logger.info(f">>>>>>>>>> STAGE {stage_name} STARTED <<<<<<<<<<")
        obj  = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> STAGE {stage_name} ENDED <<<<<<<<<<")
    
    except Exception as e:
        logger.exception(e)
        raise e
