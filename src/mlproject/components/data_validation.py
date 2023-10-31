from src.mlproject.entity.config_entity import DataValidationConfig
import pandas as pd

class data_validation:
    def __init__(self,config: DataValidationConfig) -> None:
        self.config = config

    def data_validation(self):
        try:
            validation_status = None

            df = pd.read_csv(self.config.data_path)
            schema_keys = self.config.schema_path.keys()
            for i in df.columns:
                if i not in schema_keys:
                    validation_status=False
                    with open(self.config.data_val_status_path,'w') as file:
                        file.write(f"Validation Status: {validation_status}")

                else:
                    validation_status=True
                    with open(self.config.data_val_status_path,'w') as file:
                        file.write(f"Validation Status: {validation_status}")
            
            return validation_status

        except Exception as e:
            raise e