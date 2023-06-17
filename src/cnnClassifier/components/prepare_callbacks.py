""" 
This code defines a class called PrepareCallback that provides methods for creating TensorFlow callbacks used in model training. Let's break down the code and summarize its functionality:

Import statements:

os: For operating system-related functionalities.
urllib.request as request: For making HTTP requests to download files.
ZipFile: For working with ZIP archives.
tensorflow as tf: The TensorFlow library for deep learning.
time: For working with timestamps.
cnnClassifier.entity.config_entity.PrepareCallbacksConfig: A configuration entity specific to the project.
Class PrepareCallback:

Constructor: It initializes the PrepareCallback object with a config parameter of type PrepareCallbacksConfig.
Properties:
_create_tb_callbacks: This property creates a TensorBoard callback. It generates a timestamp, creates a log directory path based on the provided configuration, and returns a tf.keras.callbacks.TensorBoard instance with the log directory.
_create_ckpt_callbacks: This property creates a model checkpoint callback. It returns a tf.keras.callbacks.ModelCheckpoint instance with the provided checkpoint model file path and the save_best_only parameter set to True.
Method get_tb_ckpt_callbacks: It returns a list of callbacks for TensorBoard and model checkpointing. It includes the callbacks created by the _create_tb_callbacks and _create_ckpt_callbacks properties.
Overall, this code provides a convenient way to create and obtain TensorFlow callbacks for TensorBoard logging and model checkpointing during model training. The class can be instantiated with a configuration object, and the get_tb_ckpt_callbacks method can be called to retrieve the desired callbacks.





"""

import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from cnnClassifier.entity.config_entity import PrepareCallbacksConfig

class PrepareCallback:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config


    
    @property
    def _create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at_{timestamp}",
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    

    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True
        )


    def get_tb_ckpt_callbacks(self):
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]
        
""" 
import os: Imports the operating system module for interacting with the file system.

import urllib.request as request: Imports the urllib.request module and assigns it the name request to facilitate making HTTP requests.

from zipfile import ZipFile: Imports the ZipFile class from the zipfile module, allowing manipulation of ZIP archives.

import tensorflow as tf: Imports the TensorFlow library for deep learning.

import time: Imports the time module for working with timestamps.

from cnnClassifier.entity.config_entity import PrepareCallbacksConfig: Imports the PrepareCallbacksConfig class from the cnnClassifier.entity.config_entity module.

class PrepareCallback:: Defines a class called PrepareCallback.

def __init__(self, config: PrepareCallbacksConfig):: Defines the constructor method of PrepareCallback that takes a config parameter of type PrepareCallbacksConfig.

self.config = config: Assigns the provided config parameter to the self.config attribute.

@property: Decorator that defines the following method as a property.

def _create_tb_callbacks(self): Defines a method called _create_tb_callbacks.

timestamp = time.strftime("%Y-%m-%d-%H-%M-%S"): Generates a timestamp using the time.strftime function in the format "YYYY-MM-DD-HH-MM-SS".

tb_running_log_dir = os.path.join(...: Constructs a log directory path by joining the tensorboard_root_log_dir from the self.config attribute with a timestamp-based directory name.

return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir): Returns a tf.keras.callbacks.TensorBoard instance configured with the log directory.

@property: Decorator that defines the following method as a property.

def _create_ckpt_callbacks(self): Defines a method called _create_ckpt_callbacks.

return tf.keras.callbacks.ModelCheckpoint(...: Returns a tf.keras.callbacks.ModelCheckpoint instance configured with the checkpoint_model_filepath from the self.config attribute and save_best_only=True.

def get_tb_ckpt_callbacks(self):: Defines a method called get_tb_ckpt_callbacks.

return [self._create_tb_callbacks, self._create_ckpt_callbacks]: Returns a list containing the _create_tb_callbacks and _create_ckpt_callbacks methods as elements.

In summary, the code defines a class called PrepareCallback that encapsulates the creation of TensorFlow callbacks for TensorBoard logging and model checkpointing. It provides methods to create and retrieve these callbacks based on a provided configuration.
"""