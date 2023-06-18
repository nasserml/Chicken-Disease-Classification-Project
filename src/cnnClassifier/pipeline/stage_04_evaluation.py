""" 
from cnnClassifier.config.configuration import ConfigurationManager: Imports the ConfigurationManager class from the configuration module in the cnnClassifier.config package.

from cnnClassifier.components.evaluation import Evaluation: Imports the Evaluation class from the evaluation module in the cnnClassifier.components package.

from cnnClassifier import logger: Imports the logger object from the cnnClassifier module.

STAGE_NAME = "Evaluation stage": Defines a constant variable STAGE_NAME with the value "Evaluation stage".

class EvaluationPipeline: Defines a class called EvaluationPipeline to orchestrate the evaluation process.

def __init__(self): Initializes an instance of the EvaluationPipeline class. The implementation is empty.

def main(self): Defines a method main that serves as the entry point for the evaluation process.

config = ConfigurationManager(): Creates an instance of ConfigurationManager to access the configuration settings.

val_config = config.get_validation_config(): Retrieves the validation configuration from the ConfigurationManager.

evaluation = Evaluation(val_config): Creates an instance of Evaluation with the validation configuration.

evaluation.evaluation(): Calls the evaluation method of the Evaluation object to perform model evaluation.

evaluation.save_score(): Calls the save_score method of the Evaluation object to save the evaluation scores.

if __name__ == '__main__':: Checks if the script is being run as the main program.

logger.info(f"*******************"): Logs a message to indicate the start of the evaluation stage.

logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<"): Logs a message to indicate the specific stage has started.

obj = EvaluationPipeline(): Creates an instance of EvaluationPipeline.

obj.main(): Calls the main method of the EvaluationPipeline object to start the evaluation process.

logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x"): Logs a message to indicate the completion of the evaluation stage.

except Exception as e:: Catches any exceptions that occur during the evaluation process.

logger.exception(e): Logs the exception that occurred.

raise e: Re-raises the exception to propagate it further.

In summary, this code sets up an evaluation pipeline by creating an instance of the Evaluation class and running the evaluation process. It retrieves the validation configuration, performs the evaluation, and saves the evaluation scores. The pipeline is orchestrated by the EvaluationPipeline class, which serves as the entry point for the evaluation stage. Logging is used to indicate the start and completion of the stage, and any exceptions that occur during the process are logged and re-raised for further handling.
"""

from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evaluation import Evaluation
from cnnClassifier import logger




STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()



if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise 