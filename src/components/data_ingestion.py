import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd 



from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts","train.csv")  
    test_data_path: str = os.path.join("artifacts","test.csv") 
    raw_data_path: str = os.path.join("artifacts","data.csv")
    
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or components")
        try:
            df = pd.read_csv("notebook/data/heart_disease.csv")
            logging.info("Read the datset as dataframe")
            
            
            
            
        except Exception as e:
            raise CustomException(e,sys)
        
    
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
        