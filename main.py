from src.mlproject import logger
from src.mlproject.pipeline.stage_1_data_ingestion import DataIngestionPipeline
from src.mlproject.pipeline.stage_2_data_validation import DataValidationPipeline

stage_name = "Data_Ingestion"

if __name__=="__main__":
    try:
        logger.info(f"\n\n>>>>>>>>>> STAGE {stage_name} STARTED <<<<<<<<<<\n\n")
        obj  = DataIngestionPipeline()
        obj.main()
        logger.info(f"\n\n>>>>>>>>>> STAGE {stage_name} ENDED <<<<<<<<<<\n\n")
    
    except Exception as e:
        logger.exception(e)
        raise e
    

stage_name = "Data Validation Stage"

if __name__=="__main__":
    try:
        logger.info(f"\n\n>>>>>>>>>> STAGE {stage_name} STARTED <<<<<<<<<<\n\n")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f"\n\n>>>>>>>>>> STAGE {stage_name} ENDED <<<<<<<<<<\n\n")
    
    except Exception as e:
        logger.exception(e)
        raise e