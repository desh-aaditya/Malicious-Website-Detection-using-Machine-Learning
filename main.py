from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from networksecurity.components.data_validation import DataValidation, DataValidationConfig
import sys
from networksecurity.entity.config_entity import DataTransformationConfig, ModelTrainerConfig
from networksecurity.components.data_tranformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
if __name__ == "__main__":
    try:
        training_pipeline_config=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(training_pipeline_config)
        data_ingestion=DataIngestion(data_ingestion_config)
        logging.info("Starting data ingestion")
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        logging.info(f"Data Ingestion completed {data_ingestion_artifact}")
        print(data_ingestion_artifact)
        data_validation_config=DataValidationConfig(training_pipeline_config)
        data_validation=DataValidation(data_ingestion_artifact,data_validation_config)
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info(f"Data Validation completed")
        print(data_validation_artifact)

        data_transformation_config=DataTransformationConfig(training_pipeline_config)
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info(f"Data Transformation completed")
        
        logging.info("Model training started")
        model_trainer_config=ModelTrainerConfig(training_pipeline_config)
        model_trainer=ModelTrainer(model_trainer_config,data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()
        logging.info(f"Model Trainer completed {model_trainer_artifact}")

    except Exception as e:
        raise NetworkSecurityException(e,sys)