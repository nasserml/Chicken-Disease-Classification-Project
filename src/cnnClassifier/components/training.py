
""" 
from cnnClassifier.entity.config_entity import TrainingConfig: Imports the TrainingConfig class from the cnnClassifier.entity.config_entity module.

import tensorflow as tf: Imports the TensorFlow library for deep learning.

from pathlib import Path: Imports the Path class from the pathlib module for working with file paths.

class Training:: Defines a class called Training.

def __init__(self, config: TrainingConfig):: Defines the constructor method of Training that takes a config parameter of type TrainingConfig.

self.config = config: Assigns the provided config parameter to the self.config attribute.

def get_base_model(self):: Defines a method called get_base_model.

self.model = tf.keras.models.load_model(...: Loads a pre-trained model from the updated_base_model_path specified in the self.config attribute and assigns it to the self.model attribute.

def train_valid_generator(self):: Defines a method called train_valid_generator.
15-16. Sets up keyword arguments (datagenerator_kwargs) for the data generators used for validation and training data.
18-22. Sets up keyword arguments (dataflow_kwargs) for the data flow parameters used by the data generators.
24-31. Creates an instance of tf.keras.preprocessing.image.ImageDataGenerator for the validation data, configures it with the datagenerator_kwargs, and generates a flow of data from the validation directory using the specified dataflow_kwargs.
34-47. Creates an instance of tf.keras.preprocessing.image.ImageDataGenerator for the training data, configures it with the datagenerator_kwargs, and generates a flow of data from the training directory using the specified dataflow_kwargs. If params_is_augmentation is True, additional data augmentation parameters are applied.

@staticmethod: Decorator indicating that the following method is a static method.

def save_model(path: Path, model: tf.keras.Model):: Defines a static method called save_model that takes a path parameter of type Path and a model parameter of type tf.keras.Model.

model.save(path): Saves the provided model to the specified path.

def train(self, callback_list: list):: Defines a method called train that takes a callback_list parameter of type list.
57-58. Calculates the number of steps per epoch and validation steps based on the number of samples and batch size of the training and validation generators.
60-70. Trains the model using the fit method of self.model, providing the training and validation generators, number of epochs, steps per epoch, validation steps, validation data, and the list of callbacks.
73-75. Saves the trained model to the specified trained_model_path in the self.config attribute using the save_model static method.

In summary, the code defines a class called Training that encapsulates the training process of a model. It provides methods to load a pre-trained model, set up data generators for training and validation data, train the model using the provided callbacks, and save the trained model to a specified path.

"""

from cnnClassifier.entity.config_entity import TrainingConfig
import tensorflow as tf
from pathlib import Path


class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config
    
    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )
    
    def train_valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)


    def train(self, callback_list: list):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator,
            callbacks=callback_list
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )