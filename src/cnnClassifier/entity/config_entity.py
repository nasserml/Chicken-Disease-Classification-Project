""" 
This code defines several data classes using the @dataclass decorator from the dataclasses module. Data classes are a convenient way to create classes that primarily hold data. The frozen=True argument ensures that the data within the class instances is immutable.

Here's a summary of each data class:

DataIngestionConfig: This class represents the configuration for data ingestion. It contains the following attributes:

root_dir: A Path object representing the root directory.
source_URL: A string representing the source URL.
local_data_file: A Path object representing the local data file.
unzip_dir: A Path object representing the directory for unzipped files.
PrepareBaseModelConfig: This class represents the configuration for preparing the base model. It contains the following attributes:

root_dir: A Path object representing the root directory.
base_model_path: A Path object representing the path to the base model.
updated_base_model_path: A Path object representing the path to the updated base model.
params_image_size: A list representing image sizes.
params_learning_rate: A float representing the learning rate.
params_include_top: A bool indicating whether to include the top layer.
params_weights: A string representing the weights.
params_classes: An integer representing the number of classes.
PrepareCallbacksConfig: This class represents the configuration for preparing callbacks. It contains the following attributes:

root_dir: A Path object representing the root directory.
tensorboard_root_log_dir: A Path object representing the root directory for TensorBoard logs.
checkpoint_model_filepath: A Path object representing the file path for checkpointing.
TrainingConfig: This class represents the configuration for training. It contains the following attributes:

root_dir: A Path object representing the root directory.
trained_model_path: A Path object representing the path to the trained model.
updated_base_model_path: A Path object representing the path to the updated base model.
training_data: A Path object representing the path to the training data.
params_epochs: An integer representing the number of epochs.
params_batch_size: An integer representing the batch size.
params_is_augmentation: A bool indicating whether to use data augmentation.
params_image_size: A list representing image sizes.
EvaluationConfig: This class represents the configuration for evaluation. It contains the following attributes:

path_of_model: A Path object representing the path to the model.
training_data: A Path object representing the path to the training data.
all_params: A dictionary containing all parameters.
params_image_size: A list representing image sizes.
params_batch_size: An integer representing the batch size.
Each data class provides a convenient way to store and access the configuration data for different components of the application. The use of data classes with the @dataclass decorator simplifies the code and automatically generates several useful methods, such as __init__, __repr__, and __eq__.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int
    

@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path
    
    
""" 
from dataclasses import dataclass: This line imports the dataclass decorator from the dataclasses module. The dataclass decorator simplifies the creation of classes that primarily hold data.

from pathlib import Path: This line imports the Path class from the pathlib module. The Path class provides an object-oriented interface for working with file system paths.

@dataclass(frozen=True): This is a decorator that is used to define a data class. The frozen=True argument makes the class instances immutable, meaning that their attributes cannot be changed after initialization.

class DataIngestionConfig: This line begins the definition of the DataIngestionConfig class.

root_dir: Path: This line defines an attribute named root_dir with the type Path. It represents the root directory.

source_URL: str: This line defines an attribute named source_URL with the type str. It represents the source URL.

local_data_file: Path: This line defines an attribute named local_data_file with the type Path. It represents the path to the local data file.

unzip_dir: Path: This line defines an attribute named unzip_dir with the type Path. It represents the directory where the files will be unzipped.

The following lines define similar classes (PrepareBaseModelConfig, PrepareCallbacksConfig, TrainingConfig, EvaluationConfig) with their respective attributes.

Each class represents a specific configuration entity and uses data classes to define the attributes of that entity. The attributes are defined with their names, types, and sometimes initial values. The data classes automatically generate several useful methods, such as __init__, __repr__, and __eq__, based on the defined attributes. The frozen=True argument ensures that the instances of these classes are immutable.

class PrepareBaseModelConfig: This line begins the definition of the PrepareBaseModelConfig class.

The subsequent lines define the attributes of the PrepareBaseModelConfig class. Here are the attributes and their types:

root_dir: Path: Represents the root directory (type: Path).
base_model_path: Path: Represents the path to the base model (type: Path).
updated_base_model_path: Path: Represents the path to the updated base model (type: Path).
params_image_size: list: Represents a list of image sizes.
params_learning_rate: float: Represents the learning rate (type: float).
params_include_top: bool: Indicates whether to include the top layer (type: bool).
params_weights: str: Represents the weights (type: str).
params_classes: int: Represents the number of classes (type: int).
The remaining lines of code follow a similar structure, defining classes for different configuration entities (PrepareCallbacksConfig, TrainingConfig, EvaluationConfig) and their respective attributes. Each class represents a distinct configuration entity with specific attributes, types, and sometimes initial values.

The use of data classes simplifies the code by automatically generating methods such as __init__, __repr__, and __eq__ based on the defined attributes. Additionally, the frozen=True argument ensures that instances of these classes are immutable, preventing accidental modifications to the configuration data.

class PrepareCallbacksConfig: This line begins the definition of the PrepareCallbacksConfig class.

The subsequent lines define the attributes of the PrepareCallbacksConfig class. Here are the attributes and their types:

root_dir: Path: Represents the root directory (type: Path).
tensorboard_root_log_dir: Path: Represents the root directory for TensorBoard logs (type: Path).
checkpoint_model_filepath: Path: Represents the file path for checkpointing (type: Path).
class TrainingConfig: This line begins the definition of the TrainingConfig class.

The subsequent lines define the attributes of the TrainingConfig class. Here are the attributes and their types:

root_dir: Path: Represents the root directory (type: Path).
trained_model_path: Path: Represents the path to the trained model (type: Path).
updated_base_model_path: Path: Represents the path to the updated base model (type: Path).
training_data: Path: Represents the path to the training data (type: Path).
params_epochs: int: Represents the number of epochs (type: int).
params_batch_size: int: Represents the batch size (type: int).
params_is_augmentation: bool: Indicates whether to use data augmentation (type: bool).
params_image_size: list: Represents a list of image sizes.
class EvaluationConfig: This line begins the definition of the EvaluationConfig class.

The subsequent lines define the attributes of the EvaluationConfig class. Here are the attributes and their types:

path_of_model: Path: Represents the path to the model (type: Path).
training_data: Path: Represents the path to the training data (type: Path).
all_params: dict: Represents a dictionary containing all parameters.
params_image_size: list: Represents a list of image sizes.
params_batch_size: int: Represents the batch size (type: int).
These classes define the configuration entities for different aspects of the application, such as data ingestion, model preparation, callbacks, training, and evaluation. Each class has specific attributes that capture the relevant information for its corresponding configuration entity.

By utilizing data classes, the code becomes more concise, and common methods like object initialization and string representation (__init__ and __repr__) are automatically generated. Additionally, the frozen=True argument ensures that instances of these classes are immutable, providing data integrity and preventing accidental modifications to the configuration data.

"""