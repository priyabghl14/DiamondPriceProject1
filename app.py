import os
import sys
from src.Dimond_Pridiction_Project.logger import logging
from src.Dimond_Pridiction_Project.exception import CustomException
from src.Dimond_Pridiction_Project.components.data_ingestion import DataIngestion



if __name__ == "__main__":

    logging.info("The execution has started")
    
    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)