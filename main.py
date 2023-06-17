""" 
This code represents a pipeline that consists of multiple stages for a machine learning task. Each stage is executed sequentially, and exceptions are handled and logged. Here's a summary of each stage:

Data Ingestion Stage:

The stage name is set as "Data Ingestion stage."
The DataIngestionTrainingPipeline class is instantiated.
The main method of the pipeline is executed, which performs data ingestion tasks.
Logging messages are printed to indicate the start and completion of the stage.
Exceptions, if any, are logged and re-raised.
Prepare Base Model Stage:

The stage name is set as "Prepare base model."
The PrepareBaseModelTrainingPipeline class is instantiated.
The main method of the pipeline is executed, which prepares the base model.
Logging messages are printed to indicate the start and completion of the stage.
Exceptions, if any, are logged and re-raised.
Training Stage:

The stage name is set as "Training."
The ModelTrainingPipeline class is instantiated.
The main method of the pipeline is executed, which trains the model.
Logging messages are printed to indicate the start and completion of the stage.
Exceptions, if any, are logged and re-raised.
Evaluation Stage:

The stage name is set as "Evaluation stage."
The EvaluationPipeline class is instantiated.
The main method of the pipeline is executed, which performs model evaluation.
Logging messages are printed to indicate the start and completion of the stage.
Exceptions, if any, are logged and re-raised.
Overall, this code demonstrates the execution of a machine learning pipeline with different stages, allowing for modularity and error handling at each stage. The logger module is used to log the progress and any exceptions that occur during the pipeline execution.
"""

from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise 



STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise 