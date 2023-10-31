from dataclasses import dataclass
from pathlib import Path

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