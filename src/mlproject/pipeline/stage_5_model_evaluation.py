from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.model_evaluation import model_evaluation
from src.mlproject import logger

class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_eval_config = config.get_model_evaluation_config()
        model_eval_obj = model_evaluation(config=model_eval_config)
        model_eval_obj.ml_flow_logging()

stage_name = "Model Evaluation Stage"
if __name__ == '__main__':
    try:
        logger.info(f"\n\n>>>>>{stage_name} Started<<<<<\n\n")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f"\n\n>>>>>{stage_name} Ended<<<<<\n\n")

    except Exception as e:
        logger.exception(e)
        raise e