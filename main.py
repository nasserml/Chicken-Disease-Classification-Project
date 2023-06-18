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
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
     


STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e



""" 
from cnnClassifier import logger: This imports the logger object from the cnnClassifier module. It is used to log information, warnings, and errors during the execution of the code.

from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline: This imports the DataIngestionTrainingPipeline class from the cnnClassifier.pipeline.stage_01_data_ingestion module. It represents the data ingestion stage of the pipeline.

from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline: This imports the PrepareBaseModelTrainingPipeline class from the cnnClassifier.pipeline.stage_02_prepare_base_model module. It represents the preparation of the base model stage of the pipeline.

from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline: This imports the ModelTrainingPipeline class from the cnnClassifier.pipeline.stage_03_training module. It represents the training stage of the pipeline.

from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline: This imports the EvaluationPipeline class from the cnnClassifier.pipeline.stage_04_evaluation module. It represents the evaluation stage of the pipeline.

STAGE_NAME = "Data Ingestion stage": This sets the value of the STAGE_NAME variable to "Data Ingestion stage". It represents the name of the current stage.

logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<"): This logs an information message indicating the start of the current stage.

data_ingestion = DataIngestionTrainingPipeline(): This creates an instance of the DataIngestionTrainingPipeline class.

data_ingestion.main(): This calls the main method of the DataIngestionTrainingPipeline class, which executes the data ingestion stage.

logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x"): This logs an information message indicating the completion of the current stage.

except Exception as e:: This starts an exception handling block to catch any exceptions that occur within the try block.

logger.exception(e): This logs the exception information using the logger object.

raise e: This re-raises the exception to propagate it further.

The code between lines 21 and 39 follows a similar structure as explained above but represents different stages of the pipeline (Prepare base model, Training, Evaluation stage). Each stage is logged, the respective pipeline class is instantiated, the main method is called, and any exceptions are logged and re-raised.

Overall, this code represents a pipeline that includes multiple stages (Data Ingestion, Prepare base model, Training, Evaluation), and each stage is executed sequentially. The logger object is used to log the progress and any exceptions that occur during the execution of each stage.

STAGE_NAME = "Evaluation stage": This sets the value of the STAGE_NAME variable to "Evaluation stage". It represents the name of the current stage.

logger.info(f"*******************"): This logs an information message to provide a visual separation between stages.

logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<"): This logs an information message indicating the start of the current stage.

model_evaluation = EvaluationPipeline(): This creates an instance of the EvaluationPipeline class.

model_evaluation.main(): This calls the main method of the EvaluationPipeline class, which executes the evaluation stage.

logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x"): This logs an information message indicating the completion of the current stage.

except Exception as e:: This starts an exception handling block to catch any exceptions that occur within the try block.

logger.exception(e): This logs the exception information using the logger object.

raise e: This re-raises the exception to propagate it further.

In summary, the code represents the execution of a multi-stage pipeline for a CNN classifier. Each stage is performed sequentially, and the logger is used to provide information about the start and completion of each stage. If an exception occurs during any stage, it is logged, and the exception is re-raised to propagate the error.



"""