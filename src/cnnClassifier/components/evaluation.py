""" 
import tensorflow as tf: Imports the TensorFlow library for deep learning.

from pathlib import Path: Imports the Path class from the pathlib module for working with file paths.

from cnnClassifier.entity.config_entity import EvaluationConfig: Imports the EvaluationConfig class from the config_entity module in the cnnClassifier.entity package.

from cnnClassifier.utils.common import save_json: Imports the save_json function from the common module in the cnnClassifier.utils package.

class Evaluation: Defines a class called Evaluation to perform model evaluation.

def __init__(self, config: EvaluationConfig): Initializes an instance of the Evaluation class with a config parameter of type EvaluationConfig.

def _valid_generator(self): Defines a private method _valid_generator to prepare the validation data generator.

@staticmethod: Decorator indicating that the following method is a static method.

def load_model(path: Path) -> tf.keras.Model: Loads a saved model from the specified path and returns it as a tf.keras.Model object.

def evaluation(self): Performs model evaluation using the loaded model and the validation data generator.

def save_score(self): Saves the evaluation scores (loss and accuracy) as a JSON file.

In summary, the code defines a class Evaluation that handles model evaluation. It provides methods to load a saved model, prepare the validation data generator, perform evaluation, and save the evaluation scores. The class takes an EvaluationConfig object as a configuration parameter, which specifies the necessary parameters for evaluation, such as image size, batch size, and the path to the model.





"""

import tensorflow as tf
from pathlib import Path
from cnnClassifier.entity.config_entity import EvaluationConfig
from cnnClassifier.utils.common import save_json



class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    
    def _valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.30
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

    
    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    

    def evaluation(self):
        model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = model.evaluate(self.valid_generator)

    
    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)


""" 
import tensorflow as tf: Imports the TensorFlow library for deep learning.

from pathlib import Path: Imports the Path class from the pathlib module for working with file paths.

from cnnClassifier.entity.config_entity import EvaluationConfig: Imports the EvaluationConfig class from the config_entity module in the cnnClassifier.entity package.

from cnnClassifier.utils.common import save_json: Imports the save_json function from the common module in the cnnClassifier.utils package.

class Evaluation: Defines a class called Evaluation to perform model evaluation.

def __init__(self, config: EvaluationConfig): Initializes an instance of the Evaluation class with a config parameter of type EvaluationConfig.

def _valid_generator(self): Defines a private method _valid_generator to prepare the validation data generator.

datagenerator_kwargs = dict(...): Defines a dictionary datagenerator_kwargs that contains keyword arguments for configuring the data generator, such as rescaling and validation split.

dataflow_kwargs = dict(...): Defines a dictionary dataflow_kwargs that contains keyword arguments for configuring the data flow, such as target size, batch size, and interpolation method.

valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(...): Creates an instance of tf.keras.preprocessing.image.ImageDataGenerator for the validation data generator with the specified data generator keyword arguments.

self.valid_generator = valid_datagenerator.flow_from_directory(...): Generates the validation data generator using the previously created valid_datagenerator, specifying the directory, subset, shuffle option, and other data flow keyword arguments.

@staticmethod: Decorator indicating that the following method is a static method.

def load_model(path: Path) -> tf.keras.Model: Defines a static method load_model that takes a path of type Path and returns a loaded model as a tf.keras.Model object using the specified path.

def evaluation(self): Defines a method evaluation that performs model evaluation.

model = self.load_model(self.config.path_of_model): Loads a model using the load_model static method and the path_of_model from the configuration.

self._valid_generator(): Calls the _valid_generator method to prepare the validation data generator.

self.score = model.evaluate(self.valid_generator): Evaluates the loaded model using the validation data generator and assigns the evaluation scores to the score attribute.

def save_score(self): Defines a method save_score to save the evaluation scores.

scores = {"loss": self.score[0], "accuracy": self.score[1]}: Creates a dictionary scores with keys "loss" and "accuracy" and assigns the respective values from the score attribute.

save_json(path=Path("scores.json"), data=scores): Saves the scores dictionary as a JSON file named "scores.json" using the save_json function, specifying the path and data to be saved.

In summary, the code defines a class Evaluation that handles model evaluation. It includes methods to load a saved model, prepare the validation data generator, perform evaluation, and save the evaluation scores as a JSON file. The class takes an EvaluationConfig object as a configuration parameter, which contains information such as the path to the model, image size, batch size, and other parameters needed for evaluation.
"""