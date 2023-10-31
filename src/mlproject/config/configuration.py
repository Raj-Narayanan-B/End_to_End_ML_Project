from json import load
from pathlib import Path
from src.mlproject.constants import *
from src.mlproject.utils.common import load_yaml,create_directories
from src.mlproject.entity.config_entity import DataIngestionConfig,DataValidationConfig

class ConfigurationManager:
    def __init__(self,
                 config_path = CONFIG_PATH,
                 params_path = PARAMS_PATH,
                 schema_path = SCHEMA_PATH):
        
        self.config = load_yaml(config_path)
        self.params = load_yaml(params_path)
        self.schema = load_yaml(schema_path)

        create_directories(self.config.artifacts_root)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories(config.root_dir)

        data_ingestion = DataIngestionConfig(root_dir = config.root_dir,
                                             source_url = config.source_url,
                                             local_data_file = config.local_data_file,
                                             data_unzip = config.unzip_dir)

        return (data_ingestion)
    
    def get_data_validation_config(self):

        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories(config.root_dir)

        data_validation_config = DataValidationConfig(root_dir=config.root_dir,
                                                      data_path=config.data_path,
                                                      data_val_status_path=config.validation_status_path,
                                                      schema_path=schema)
        
        return(data_validation_config)