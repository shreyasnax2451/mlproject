import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split

class DataIngestionConfig:
    def __init__(self):
        self.train_data_path: str = os.path.join('artifacts','train.csv')
        self.test_data_path: str = os.path.join('artifacts','test.csv')
        self.raw_data_path: str = os.path.join('artifacts','raw.csv')
    
class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info('Entered Data Ingestion')
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info('Read Data from CSV')

            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.data_ingestion_config.raw_data_path, index = False, header = True)
            train_data, test_data = train_test_split(df, test_size = 0.25, random_state = 42)
            train_data.to_csv(self.data_ingestion_config.train_data_path, index = False, header = True)
            test_data.to_csv(self.data_ingestion_config.test_data_path, index = False, header = True)
            logging.info('Train Test split done from data')
            return(
                    self.data_ingestion_config.train_data_path,
                    self.data_ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == '__main__':
    data_ingestion_obj = DataIngestion()
    train_data,test_data = data_ingestion_obj.initiate_data_ingestion()