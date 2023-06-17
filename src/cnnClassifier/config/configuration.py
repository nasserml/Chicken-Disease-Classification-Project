""" 
The code in configuration.py defines a ConfigurationManager class that handles the retrieval of various configuration entities used in a CNN classifier application. Let's summarize and explain the code:

The code starts with importing necessary modules and classes from different files.

The ConfigurationManager class is defined. It serves as a central component for managing and retrieving different configuration entities.

The __init__ method initializes an instance of ConfigurationManager with optional file paths for the configuration and parameters files.

Inside the __init__ method, the configuration and parameters are read using the read_yaml function from the common module. The resulting configurations are stored in the self.config and self.params attributes.

The create_directories function is called to create necessary directories using the artifacts_root path from the configuration.

The get_data_ingestion_config method retrieves the data ingestion configuration entity. It creates directories based on the configuration, and then initializes and returns an instance of DataIngestionConfig with the corresponding configuration values.

The get_prepare_base_model_config method retrieves the prepare base model configuration entity. It creates directories based on the configuration, and then initializes and returns an instance of PrepareBaseModelConfig with the corresponding configuration values and parameters.

The get_prepare_callback_config method retrieves the prepare callbacks configuration entity. It creates directories based on the configuration, and then initializes and returns an instance of PrepareCallbacksConfig with the corresponding configuration values.

The get_training_config method retrieves the training configuration entity. It creates directories based on the configuration, prepares the training data path, and then initializes and returns an instance of TrainingConfig with the corresponding configuration values and parameters.

The get_validation_config method retrieves the evaluation configuration entity. It initializes and returns an instance of EvaluationConfig with predetermined paths and the parameters.

The ConfigurationManager class encapsulates the logic for retrieving different configuration entities by parsing the configuration and parameters files. It ensures that the necessary directories are created and returns instances of the respective configuration classes with the appropriate attribute values.

"""

from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml,create_directories
from cnnClassifier.entity.config_entity import (DataIngestionConfig,
                                                PrepareBaseModelConfig)
class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config
    
""" 
an explanation of each line of the code:

python
 
from cnnClassifier.constants import *
This line imports all the constants defined in the cnnClassifier.constants module. The * is a wildcard that includes all the constants from that module in the current namespace.

python
 
import os
This line imports the os module, which provides functions for interacting with the operating system.

python
 
from pathlib import Path
This line imports the Path class from the pathlib module. The Path class provides an object-oriented interface to manipulate file paths.

python
 
from cnnClassifier.utils.common import read_yaml, create_directories
This line imports the read_yaml and create_directories functions from the cnnClassifier.utils.common module. These functions are used for reading YAML files and creating directories, respectively.

python
 
from cnnClassifier.entity.config_entity import (DataIngestionConfig, PrepareBaseModelConfig, PrepareCallbacksConfig, TrainingConfig, EvaluationConfig)
This line imports the DataIngestionConfig, PrepareBaseModelConfig, PrepareCallbacksConfig, TrainingConfig, and EvaluationConfig classes from the cnnClassifier.entity.config_entity module. These classes represent different configuration entities used in the CNN classifier application.

python
 
class ConfigurationManager:
This line defines the ConfigurationManager class, which serves as a manager for retrieving different configuration entities.

python
 
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
This line defines the __init__ method of the ConfigurationManager class. It takes two optional arguments, config_filepath and params_filepath, with default values CONFIG_FILE_PATH and PARAMS_FILE_PATH, respectively.

python
 
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
These two lines read the YAML files specified by config_filepath and params_filepath using the read_yaml function. The resulting configurations are stored in the self.config and self.params attributes.

python
 
        create_directories([self.config.artifacts_root])
This line calls the create_directories function with a list containing the artifacts_root path from the self.config object. It creates the necessary directories based on the configuration.

The rest of the code defines several methods that retrieve different configuration entities by initializing the corresponding classes with the appropriate configuration values and returning the instances.


python
 
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
This method get_data_ingestion_config retrieves the DataIngestionConfig entity. It starts by accessing the data_ingestion attribute from the self.config object, which represents the configuration for data ingestion. It then creates the necessary directories based on the root_dir value from the configuration. Finally, it initializes a DataIngestionConfig instance using the configuration values and returns it.

python
 
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config
This method get_prepare_base_model_config retrieves the PrepareBaseModelConfig entity. It begins by accessing the prepare_base_model attribute from the self.config object, which represents the configuration for preparing the base model. It then creates the necessary directories based on the root_dir value from the configuration. Afterwards, it initializes a PrepareBaseModelConfig instance using the configuration values and the parameter values from self.params. Finally, it returns the initialized PrepareBaseModelConfig instance.

python
 
    def get_prepare_callback_config(self) -> PrepareCallbacksConfig:
        config = self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directories([
            Path(model_ckpt_dir),
            Path(config.tensorboard_root_log_dir)
        ])

        prepare_callback_config = PrepareCallbacksConfig(
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath)
        )

        return prepare_callback_config
This method get_prepare_callback_config retrieves the PrepareCallbacksConfig entity. It starts by accessing the prepare_callbacks attribute from the self.config object, which represents the configuration for preparing callbacks. It also extracts the directory path from the checkpoint_model_filepath and creates the necessary directories for both the model checkpoint and tensorboard log directories. Then, it initializes a PrepareCallbacksConfig instance using the configuration values and returns it.

python
 
    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "Chicken-fecal-images")
        create_directories([
            Path(training.root_dir)
        ])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )

        return training_config
This method get_training_config retrieves the TrainingConfig entity. It first accesses the training and prepare_base_model attributes from the self.config object, representing the configuration for training and preparing the base model, respectively. It also assigns the self.params object to the params variable. Additionally, it constructs the path for the training data by joining the unzip_dir path from the data_ingestion configuration with the "Chicken-fecal-images" string. It then creates the necessary directories based on the root_dir value from the training configuration. Finally, it initializes a TrainingConfig instance using the configuration values, the prepared base model path, the training data path, and the parameter values, and returns it.

python
 
    def get_validation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model=Path("artifacts/training/model.h5"),
            training_data=Path("artifacts/data_ingestion/Chicken-fecal-images"),
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
        return eval_config
This method get_validation_config retrieves the EvaluationConfig entity. It directly initializes an EvaluationConfig instance with fixed paths and parameter values from the self.params object and returns it.


"""