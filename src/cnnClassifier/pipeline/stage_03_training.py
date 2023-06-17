""" 
a summary of the code:

It imports the necessary modules and classes: ConfigurationManager from cnnClassifier.config.configuration, PrepareCallback from cnnClassifier.components.prepare_callbacks, Training from cnnClassifier.components.training, and logger from cnnClassifier.
It defines a constant STAGE_NAME with the value "Training".
It defines a class called ModelTrainingPipeline with an empty constructor.
It has a main method within ModelTrainingPipeline that serves as the entry point for the pipeline.
Inside the main method:
It initializes a ConfigurationManager object to retrieve configuration settings.
It gets the prepare callbacks configuration from the ConfigurationManager and creates an instance of PrepareCallback with the obtained configuration.
It retrieves the TensorBoard and checkpoint callbacks list from the PrepareCallback instance.
It gets the training configuration from the ConfigurationManager and creates an instance of Training with the obtained configuration.
It loads the base model for training using the get_base_model method of the Training instance.
It sets up the data generators for training and validation using the train_valid_generator method of the Training instance.
It performs the training process by calling the train method of the Training instance and passing the callback list obtained earlier.
The if __name__ == '__main__': block ensures that the following code is only executed when the script is run directly and not imported as a module.
Inside the if __name__ == '__main__': block:
It logs the start of the training stage.
It creates an instance of ModelTrainingPipeline.
It calls the main method of the ModelTrainingPipeline instance to start the training pipeline.
It logs the completion of the training stage.
If any exception occurs during the execution, it logs the exception and raises it.
In summary, this code sets up and executes a model training pipeline. It retrieves configurations, prepares callbacks, initializes the training process, and logs the progress and completion of the training stage.
"""

from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_callbacks import PrepareCallback
from cnnClassifier.components.training import Training
from cnnClassifier import logger



STAGE_NAME = "Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()


        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )




if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

""" 
from cnnClassifier.config.configuration import ConfigurationManager: It imports the ConfigurationManager class from the cnnClassifier.config.configuration module.
from cnnClassifier.components.prepare_callbacks import PrepareCallback: It imports the PrepareCallback class from the cnnClassifier.components.prepare_callbacks module.
from cnnClassifier.components.training import Training: It imports the Training class from the cnnClassifier.components.training module.
from cnnClassifier import logger: It imports the logger object from the cnnClassifier module.
STAGE_NAME = "Training": It defines a constant variable STAGE_NAME with the value "Training".
class ModelTrainingPipeline:: It defines a class called ModelTrainingPipeline.
def __init__(self):: It defines the constructor of the ModelTrainingPipeline class.
pass: It is a placeholder statement indicating an empty block of code.
def main(self):: It defines a method called main within the ModelTrainingPipeline class.
config = ConfigurationManager(): It creates an instance of the ConfigurationManager class and assigns it to the config variable.
prepare_callbacks_config = config.get_prepare_callback_config(): It retrieves the prepare callbacks configuration using the get_prepare_callback_config method of the config object and assigns it to the prepare_callbacks_config variable.
prepare_callbacks = PrepareCallback(config=prepare_callbacks_config): It creates an instance of the PrepareCallback class with the prepare_callbacks_config as the configuration and assigns it to the prepare_callbacks variable.
callback_list = prepare_callbacks.get_tb_ckpt_callbacks(): It retrieves the TensorBoard and checkpoint callbacks list using the get_tb_ckpt_callbacks method of the prepare_callbacks object and assigns it to the callback_list variable.
training_config = config.get_training_config(): It retrieves the training configuration using the get_training_config method of the config object and assigns it to the training_config variable.
training = Training(config=training_config): It creates an instance of the Training class with the training_config as the configuration and assigns it to the training variable.
training.get_base_model(): It calls the get_base_model method of the training object to load the base model for training.
training.train_valid_generator(): It calls the train_valid_generator method of the training object to set up the data generators for training and validation.
training.train(callback_list=callback_list): It calls the train method of the training object to perform the training process, passing the callback_list as an argument.
if __name__ == '__main__':: It checks if the script is being run directly as the main module.
try:: It begins a try block for exception handling.
logger.info(f"*******************"): It logs an informational message using the logger object.
logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<"): It logs an informational message indicating the start of the training stage.
obj = ModelTrainingPipeline(): It creates an instance of the ModelTrainingPipeline class and assigns it to the obj variable.
obj.main(): It calls the main method of the obj object to start the training pipeline.
logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x"): It logs an informational message indicating the completion of the training stage.
except Exception as e:: It catches any exception that occurred within the try block and assigns it to the variable e.
logger.exception(e): It logs the exception traceback using the logger object.
raise e: It re-raises the exception to propagate it further.
The code above demonstrates a training pipeline for a machine learning model. It follows a modular approach where different components and configurations are imported and used to perform the training process.

The ModelTrainingPipeline class serves as the main entry point for the training pipeline. It initializes the necessary configurations and objects, such as the ConfigurationManager, PrepareCallback, and Training.

Within the main method of the ModelTrainingPipeline class, the prepare callbacks configuration is retrieved, an instance of the PrepareCallback class is created, and the TensorBoard and checkpoint callbacks are obtained.

Similarly, the training configuration is retrieved, and an instance of the Training class is created. The base model is loaded, data generators for training and validation are set up, and the training process is initiated by calling the train method.

If the script is run directly as the main module, the training pipeline is executed. A try-except block is used for exception handling, where any exceptions raised during the training process are logged using the logger object.

Overall, this code encapsulates the training stage of a machine learning pipeline, utilizing separate components for preparing callbacks, managing configurations, and executing the training process.
"""