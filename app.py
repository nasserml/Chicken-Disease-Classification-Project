from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.predict import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully!"



@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)


if __name__ == "__main__":
    clApp = ClientApp()
    # app.run(host='0.0.0.0', port=8080) #local host
    # app.run(host='0.0.0.0', port=8080) #for AWS
    app.run(host='0.0.0.0', port=80) #for AZURE
    
    
"""

from flask import Flask, request, jsonify, render_template: Imports the necessary classes and functions from the Flask library for building a web application.

import os: Imports the os module for interacting with the operating system.

from flask_cors import CORS, cross_origin: Imports the CORS and cross_origin classes from the Flask-CORS extension. These classes enable Cross-Origin Resource Sharing (CORS) support in the application.

from cnnClassifier.utils.common import decodeImage: Imports the decodeImage function from the cnnClassifier.utils.common module.

from cnnClassifier.pipeline.predict import PredictionPipeline: Imports the PredictionPipeline class from the cnnClassifier.pipeline.predict module.

os.putenv('LANG', 'en_US.UTF-8') and os.putenv('LC_ALL', 'en_US.UTF-8'): Sets the environment variables 'LANG' and 'LC_ALL' to 'en_US.UTF-8'. This is done to ensure proper character encoding.

app = Flask(__name__): Creates a Flask application instance.

CORS(app): Enables CORS support for the Flask application.

class ClientApp:: Defines a class named ClientApp.

def __init__(self):: Defines the constructor method of the ClientApp class. It initializes the filename attribute to "inputImage.jpg" and creates an instance of the PredictionPipeline class, assigning it to the classifier attribute.

@app.route("/", methods=['GET']) and @app.route("/train", methods=['GET','POST']) and @app.route("/predict", methods=['POST']): Define the routes of the Flask application and specify the HTTP methods allowed for each route.

def home(): and def trainRoute(): and def predictRoute():: Define the handler functions for each route.

return render_template('index.html'): Returns the rendered HTML template named 'index.html' for the home route.

os.system("python main.py"): Executes the command "python main.py" in the system shell. This is performed when the '/train' route is accessed, triggering the training process.

image = request.json['image']: Retrieves the 'image' value from the JSON data sent in the request body.

decodeImage(image, clApp.filename): Decodes the image data using the decodeImage function, passing the image data and the filename attribute of the ClientApp instance.

result = clApp.classifier.predict(): Calls the predict method of the PredictionPipeline instance stored in the classifier attribute of the ClientApp instance.

return jsonify(result): Returns the result as a JSON response.

if __name__ == "__main__":: Checks if the script is being run directly (not imported as a module).

clApp = ClientApp(): Creates an instance of the ClientApp class and assigns it to the clApp variable.

app.run(host='0.0.0.0', port=80): Starts the Flask application, running it on the specified host and port (0.0.0.0:80). This makes the application accessible over the network.

The code sets up a Flask web application with routes for the home page, training, and prediction. It uses the PredictionPipeline class to handle image prediction based on the received requests.
"""