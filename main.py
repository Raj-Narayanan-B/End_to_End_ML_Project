from src.mlproject import logger
from src.mlproject.pipeline.stage_1_data_ingestion import DataIngestionPipeline
from src.mlproject.pipeline.stage_2_data_validation import DataValidationPipeline
from src.mlproject.pipeline.stage_3_data_transformation import DataTransformationPipeline
from src.mlproject.pipeline.stage_4_model_trainer import ModelTrainingPipeline
from src.mlproject.pipeline.stage_5_model_evaluation import ModelEvaluationPipeline

stage_name = "Data_Ingestion Stage"
try:
    logger.info(f"\n\n>>>>>>>>>> STAGE {stage_name} STARTED <<<<<<<<<<\n\n")
    obj  = DataIngestionPipeline()
    obj.main()
    logger.info(f"\n\n>>>>>>>>>> STAGE {stage_name} ENDED <<<<<<<<<<\n\n")

except Exception as e:
    logger.exception(e)
    raise e
    

stage_name = "Data Validation Stage"
try:
    logger.info(f"\n\n>>>>>>>>>> STAGE {stage_name} STARTED <<<<<<<<<<\n\n")
    obj = DataValidationPipeline()
    obj.main()
    logger.info(f"\n\n>>>>>>>>>> STAGE {stage_name} ENDED <<<<<<<<<<\n\n")

except Exception as e:
    logger.exception(e)
    raise e


stage_name = "Data Transformation Stage"
try:
    logger.info(f"\n\n>>>>>>>>>> STAGE {stage_name} STARTED <<<<<<<<<<\n\n")
    obj = DataTransformationPipeline()
    obj.main()
    logger.info(f"\n\n>>>>>>>>>> STAGE {stage_name} ENDED <<<<<<<<<<\n\n")

except Exception as e:
    logger.exception(e)
    raise e


stage_name = "Model Training Stage"
try:
    logger.info(f"\n\n>>>>>>>>>> STAGE {stage_name} STARTED <<<<<<<<<<\n\n")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f"\n\n>>>>>>>>>> STAGE {stage_name} ENDED <<<<<<<<<<\n\n")

except Exception as e:
    logger.exception(e)
    raise e


stage_name = "Model Evaluation Stage"
try:
    logger.info(f"\n\n>>>>>>>>>> STAGE {stage_name} STARTED <<<<<<<<<<\n\n")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f"\n\n>>>>>>>>>> STAGE {stage_name} ENDED <<<<<<<<<<\n\n")

except Exception as e:
    logger.exception(e)
    raise e