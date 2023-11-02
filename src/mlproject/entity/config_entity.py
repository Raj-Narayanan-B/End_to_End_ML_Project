from dataclasses import dataclass #type: ignore
from pathlib import Path #type: ignore

from numpy import source

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    data_unzip: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    data_path: Path
    data_val_status_path: str
    schema_path: dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: str
    train_path: str
    test_path: str

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train: Path
    test: Path
    model: str
    alpha: float
    l1_ratio: float
    target: str