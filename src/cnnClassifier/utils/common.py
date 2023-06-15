""" 
This code snippet includes several functions related to file and data manipulation. Here's a summary and explanation of each function:

read_yaml(path_to_yaml: Path) -> ConfigBox: Reads a YAML file from the given path and returns its content as a ConfigBox object. It handles exceptions for empty files and logs the successful loading of the YAML file.

create_directories(path_to_directories: list, verbose=True): Creates a list of directories specified by the path_to_directories parameter. It uses the os.makedirs() function to create the directories and logs the successful creation of each directory.

save_json(path: Path, data: dict): Saves a dictionary data as JSON to the file specified by path. It uses the json.dump() function to write the data to the file and logs the successful saving of the JSON file.

load_json(path: Path) -> ConfigBox: Loads a JSON file from the given path and returns its content as a ConfigBox object. It logs the successful loading of the JSON file.

save_bin(data: Any, path: Path): Saves binary data data to the file specified by path using the joblib.dump() function. It logs the successful saving of the binary file.

load_bin(path: Path) -> Any: Loads binary data from the given file path using the joblib.load() function and returns the loaded data. It logs the successful loading of the binary file.

get_size(path: Path) -> str: Calculates the size of a file specified by path in kilobytes (KB) and returns it as a string. It uses the os.path.getsize() function to get the file size.

decodeImage(imgstring, fileName): Decodes an image represented as a base64-encoded string imgstring and saves it as a file with the specified fileName.

encodeImageIntoBase64(croppedImagePath): Reads an image file from croppedImagePath and encodes it into a base64-encoded string using the base64.b64encode() function. The encoded string is then returned.

These functions provide utility for reading and writing YAML and JSON files, creating directories, saving and loading binary data, and handling image encoding and decoding using base64.
"""

import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64





@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns
    Args:
        path_to_yaml (str): path like input
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")



@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data
    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")




@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data
    Args:
        path (Path): path to json file
    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file
    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data
    Args:
        path (Path): path to binary file
    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    Args:
        path (Path): path of the file
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
    
""" 

import os: Imports the os module, which provides functions for interacting with the operating system.

from box.exceptions import BoxValueError: Imports the BoxValueError exception from the box.exceptions module.

import yaml: Imports the yaml module, which allows reading and writing YAML files.

from cnnClassifier import logger: Imports the logger object from the cnnClassifier module.

import json: Imports the json module, which provides functions for working with JSON data.

import joblib: Imports the joblib module, which provides functions for saving and loading Python objects in binary format.

from ensure import ensure_annotations: Imports the ensure_annotations decorator from the ensure module.

from box import ConfigBox: Imports the ConfigBox class from the box module.

from pathlib import Path: Imports the Path class from the pathlib module, which provides an object-oriented approach to working with file paths.

from typing import Any: Imports the Any type from the typing module, which represents an arbitrary type.

import base64: Imports the base64 module, which provides functions for encoding and decoding data in base64 format.

@ensure_annotations: This is a decorator that ensures the type annotations of the function arguments and return value are correctly specified.

def read_yaml(path_to_yaml: Path) -> ConfigBox: This function takes a Path object representing the path to a YAML file and returns a ConfigBox object. It reads the YAML file using the yaml.safe_load() function and logs a message indicating the successful loading of the file. If the YAML file is empty, it raises a ValueError with the message "yaml file is empty". If any other exception occurs, it raises that exception.

def create_directories(path_to_directories: list, verbose=True): This function takes a list of directory paths (path_to_directories) and creates the directories using os.makedirs(). If verbose is set to True, it logs a message for each created directory.

def save_json(path: Path, data: dict): This function takes a Path object representing the path to a JSON file and a dictionary (data) to be saved in the JSON file. It writes the dictionary to the file using the json.dump() function with an indentation of 4 spaces. It also logs a message indicating the successful saving of the JSON file.

def load_json(path: Path) -> ConfigBox: This function takes a Path object representing the path to a JSON file and returns a ConfigBox object. It reads the JSON file using json.load() and logs a message indicating the successful loading of the file.

def save_bin(data: Any, path: Path): This function takes any Python object (data) and a Path object representing the path to a binary file. It saves the object to the file using joblib.dump() and logs a message indicating the successful saving of the binary file.

def load_bin(path: Path) -> Any: This function takes a Path object representing the path to a binary file and returns the object stored in the file. It loads the object using joblib.load() and logs a message indicating the successful loading of the binary file.

def get_size(path: Path) -> str: This function takes a Path object representing the path of a file and returns a string representing the size of the file in kilobytes (KB). It calculates the size of the file using os.path.getsize() and divides it by 1024 to convert it to KB.

def decodeImage(imgstring, fileName): This function takes an image string (imgstring) and a file name (fileName). It decodes the base64-encoded image data using base64.b64decode() and writes it to a file with the given name.

def encodeImageIntoBase64(croppedImagePath): This function takes the path to a cropped image (croppedImagePath). It opens the image file in binary mode using open() and reads its content. Then, it encodes the image data into base64 format using base64.b64encode() and returns the encoded data.

These functions provide a set of utilities for handling file operations, including reading and writing YAML and JSON files, creating directories, saving and loading binary data, and encoding and decoding images using base64.
"""