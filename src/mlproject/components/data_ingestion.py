from urllib import request
from zipfile import ZipFile
from src.mlproject import logger
from src.mlproject.config import *
import gdown
from pathlib import Path
from src.mlproject.entity.config_entity import DataIngestionConfig
import os

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            gdown.download(self.config.source_url, self.config.local_data_file, quiet=False)
            # logger.info(f"{filename} downloaded with follow info: {headers}")
        else:
            logger.info(f"File already exists!")


    def extract_zipfile(self):
        with ZipFile(self.config.local_data_file, 'r') as zip_file:
            zip_file.extractall(self.config.data_unzip)
            