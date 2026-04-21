from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
# from network_security.components.data_transformation import DataTransformation
# from network_security.components.model_trainer import ModelTrainer

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys

if __name__ == '__main__':
    try:
        training_pipeline_conifg = TrainingPipelineConfig()
        data_ingestion_conifg = DataIngestionConfig(training_pipeline_conifg)
        data_ingestion = DataIngestion(data_ingestion_conifg)
        logging.info('Initiate data ingestion')
        dataingestionartifact = data_ingestion.initiate_data_ingestion()        
        print(dataingestionartifact) 
        logging.info('Data initation completed')
        data_validation_conifg = DataValidationConfig(training_pipeline_conifg)
        data_validation = DataValidation(dataingestionartifact,data_validation_conifg)
        logging.info('Initiate the data validation ')
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info('Data validation completed')
        print(data_validation)

    except Exception as e:
        raise NetworkSecurityException(e,sys)