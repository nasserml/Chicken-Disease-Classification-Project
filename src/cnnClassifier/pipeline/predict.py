""" 
code defines a PredictionPipeline class that performs image prediction using a trained model. Here's a summary of the code:

The code imports necessary libraries: numpy for array operations, load_model from tensorflow.keras.models to load a pre-trained model, image from tensorflow.keras.preprocessing for image preprocessing, and os for file path manipulation.

The PredictionPipeline class is defined, which takes a filename parameter representing the path of the image to be predicted.

The predict method is defined within the PredictionPipeline class. It performs the following steps:

Loads the trained model using load_model function, assuming the model file is located at "artifacts/training/model.h5".

Loads the image specified by self.filename using image.load_img and resizes it to the target size of (224, 224).

Converts the image to an array using image.img_to_array.

Expands the dimensions of the image array using np.expand_dims to match the expected input shape of the model.

Uses the model to predict the class probabilities for the input image using model.predict. The argmax function is used to determine the index of the predicted class with the highest probability.

Prints the predicted class index (result) to the console.

Based on the predicted class, the method assigns a human-readable label (Healthy or Coccidiosis) to the prediction variable.

Returns a list containing a dictionary with the predicted label, in the format [{ "image" : prediction}].

Overall, this code defines a pipeline for image prediction using a trained model. Given an image file, it loads the model, preprocesses the image, performs the prediction, and returns the predicted label.





"""

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        # load model
        model = load_model(os.path.join("artifacts","training", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Healthy'
            return [{ "image" : prediction}]
        else:
            prediction = 'Coccidiosis'
            return [{ "image" : prediction}]
        


""" 
import numpy as np: Imports the NumPy library and assigns it the alias np. NumPy is a popular library for numerical operations in Python.

from tensorflow.keras.models import load_model: Imports the load_model function from the tensorflow.keras.models module. This function is used to load a pre-trained model saved in the HDF5 format.

from tensorflow.keras.preprocessing import image: Imports the image module from tensorflow.keras.preprocessing. This module provides functions for image preprocessing tasks.

import os: Imports the os module, which provides functions for interacting with the operating system, including file path manipulation.

class PredictionPipeline:: Defines a class named PredictionPipeline.

def __init__(self, filename):: Defines the constructor method of the PredictionPipeline class. It takes a filename parameter and assigns it to the instance variable self.filename.

def predict(self):: Defines the predict method of the PredictionPipeline class.

model = load_model(os.path.join("artifacts", "training", "model.h5")): Loads a pre-trained model by calling the load_model function. The model file is assumed to be located at the path "artifacts/training/model.h5". The loaded model is assigned to the model variable.

imagename = self.filename: Assigns the value of self.filename to the imagename variable.

test_image = image.load_img(imagename, target_size=(224, 224)): Loads the image specified by imagename using the load_img function from the image module. The image is resized to the target size of (224, 224) pixels and assigned to the test_image variable.

test_image = image.img_to_array(test_image): Converts the test_image from a PIL image object to a NumPy array using the img_to_array function. This step is necessary to prepare the image for input to the model.

test_image = np.expand_dims(test_image, axis=0): Adds an extra dimension to the test_image array using np.expand_dims. This is done to match the expected input shape of the model, which typically requires a batch dimension.

result = np.argmax(model.predict(test_image), axis=1): Uses the model to predict the class probabilities for the test_image using model.predict. The argmax function from NumPy is applied to the result to obtain the index of the predicted class with the highest probability. The predicted class index is assigned to the result variable.

print(result): Prints the result (predicted class index) to the console.

if result[0] == 1: ... else: ...: Checks if the predicted class index (result[0]) is equal to 1. Based on the condition, a prediction label is assigned to the prediction variable. If the condition is true, the label is set to 'Healthy'; otherwise, it is set to 'Coccidiosis'.

return [{ "image" : prediction }]: Returns a list containing a dictionary with the predicted label. The label is assigned to the key "image". The returned value has the format [{ "image" : prediction }].

Overall, this code defines a PredictionPipeline class that takes an image file as input, loads a pre-trained model, performs prediction on the input image, and returns the predicted label.
"""