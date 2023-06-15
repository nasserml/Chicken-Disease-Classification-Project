""" 
This code represents a data ingestion stage in a training pipeline. Here's a summary and explanation of each part:

python
 
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger
The code imports the ConfigurationManager class from the cnnClassifier.config.configuration module, the DataIngestion class from the cnnClassifier.components.data_ingestion module, and the logger object from the cnnClassifier module.
python
 
STAGE_NAME = "Data Ingestion stage"
This line defines a constant variable STAGE_NAME with the value "Data Ingestion stage".
python
 
class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
This class represents the data ingestion stage in the training pipeline.
The main method is the entry point of this stage.
It creates an instance of ConfigurationManager to obtain the data ingestion configuration.
It uses the configuration to create an instance of DataIngestion.
It then calls the download_file method of the DataIngestion instance to download a file.
Finally, it calls the extract_zip_file method of the DataIngestion instance to extract the contents of the zip file.
python
 
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
This block of code is executed when the script is run as the main program.
It wraps the execution in a try-except block to handle and log any exceptions that occur during the execution.
It logs a message indicating the start of the data ingestion stage.
It creates an instance of the DataIngestionTrainingPipeline class and calls its main method.
After the successful completion of the main method, it logs a message indicating the completion of the data ingestion stage.
If an exception occurs, it logs the exception and raises it again.
Overall, this code sets up the data ingestion stage of the training pipeline by creating instances of the ConfigurationManager and DataIngestion classes and calling their respective methods to download a file and extract its contents. It provides logging information to track the start and completion of the data ingestion stage.
"""

from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger



STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
""" 
explanation of each line in the code:

python
 
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger
These lines import the ConfigurationManager class from the cnnClassifier.config.configuration module, the DataIngestion class from the cnnClassifier.components.data_ingestion module, and the logger object from the cnnClassifier module.
python
 
STAGE_NAME = "Data Ingestion stage"
This line assigns the string value "Data Ingestion stage" to the constant variable STAGE_NAME.
python
 
class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
This code defines a class named DataIngestionTrainingPipeline.
The class has an empty __init__ method and a main method.
The main method creates an instance of ConfigurationManager to obtain the data ingestion configuration.
It uses the configuration to create an instance of DataIngestion.
Then, it calls the download_file method of the DataIngestion instance to download a file.
Finally, it calls the extract_zip_file method of the DataIngestion instance to extract the contents of the zip file.
python
 
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
This block of code is executed when the script is run as the main program.
It checks if the current module is being run as the main program (__name__ variable is equal to '__main__').
If it is, the code inside the block is executed.
It logs a message indicating the start of the data ingestion stage using the logger.info method.
It creates an instance of the DataIngestionTrainingPipeline class.
The main method of the DataIngestionTrainingPipeline instance is called.
After the successful completion of the main method, it logs a message indicating the completion of the data ingestion stage.
If an exception occurs during execution, it logs the exception using the logger.exception method and re-raises the exception.
Certainly! Here's the continuation:

python
 
except Exception as e:
    logger.exception(e)
    raise e
If an exception occurs during the execution of the code within the try block, it is caught in the except block.
The exception is logged using the logger.exception method, which prints the exception traceback.
Finally, the exception is re-raised using the raise statement to propagate it further.
Overall, this code sets up a data ingestion pipeline by using the DataIngestionTrainingPipeline class. It initializes the necessary configurations, performs data ingestion tasks such as downloading a file and extracting its contents, and logs the progress and completion of the data ingestion stage.

"""