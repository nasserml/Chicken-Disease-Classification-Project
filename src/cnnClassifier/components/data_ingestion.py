""" 
explanation of the code:

python
 
import os
import urllib.request as request
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path
The code begins with importing necessary modules and packages. It imports os for operating system-related functions, urllib.request as request for handling HTTP requests, zipfile for working with zip files, logger from cnnClassifier module for logging purposes, get_size function from cnnClassifier.utils.common module, DataIngestionConfig entity from cnnClassifier.entity.config_entity, and Path from pathlib for working with file paths.

python
 
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
The code defines a class named DataIngestion. It has an __init__ method that takes a DataIngestionConfig object as a parameter and assigns it to the self.config attribute.

python
 
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
The download_file method is responsible for downloading a file from a specified URL. It first checks if the file already exists in the local directory (self.config.local_data_file). If it doesn't exist, it uses request.urlretrieve to download the file from the specified URL (self.config.source_URL) and saves it with the specified filename (self.config.local_data_file). It then logs the information about the downloaded file. If the file already exists, it logs the information about the existing file size.

python
 
    def extract_zip_file(self):
        
        zip_file_path: str
        Extracts the zip file into the data directory
        Functon returns None
        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
The extract_zip_file method is responsible for extracting a zip file. It first creates the directory path (unzip_path) where the contents of the zip file will be extracted. It uses os.makedirs to create the directory if it doesn't exist. Then, it uses zipfile.ZipFile to open the zip file (self.config.local_data_file) in read mode. It extracts all the contents of the zip file into the specified directory path (unzip_path) using zip_ref.extractall.

Overall, this code defines a DataIngestion class that handles downloading a file from a URL and extracting the contents of a zip file into a directory. It utilizes the provided DataIngestionConfig object to determine the file paths and URLs.
"""


import os
import urllib.request as request
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  


    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)


""" 
an explanation of each line of the code:

python
 
import os
import urllib.request as request
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path
The first line imports the os module, which provides functions for interacting with the operating system.
The second line imports the request module from urllib as request, which allows making HTTP requests.
The third line imports the zipfile module, which provides functionality for working with zip files.
The fourth line imports the logger object from the cnnClassifier module, which is used for logging.
The fifth line imports the get_size function from the cnnClassifier.utils.common module, which calculates the size of a file.
The sixth line imports the DataIngestionConfig entity from the cnnClassifier.entity.config_entity module, which represents the configuration for data ingestion.
The seventh line imports the Path class from the pathlib module, which represents a file or directory path.
python
 
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
This block defines a class named DataIngestion.
The __init__ method is the constructor for the class, which takes a DataIngestionConfig object as a parameter and assigns it to the self.config attribute.
python
 
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
This method, download_file, is responsible for downloading a file from a specified URL.
It checks if the file already exists in the local directory (self.config.local_data_file) using os.path.exists.
If the file doesn't exist, it uses request.urlretrieve to download the file from the specified URL (self.config.source_URL) and saves it with the specified filename (self.config.local_data_file).
It then logs the information about the downloaded file using the logger.info function.
If the file already exists, it logs the information about the existing file size using the logger.info function and get_size function.
python
 
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
This method, extract_zip_file, is responsible for extracting the contents of a zip file into a directory.
It sets the path for extracting the zip file contents to unzip_path (self.config.unzip_dir).
It creates the directory path if it doesn't exist using os.makedirs.
It opens the zip file (self.config.local_data_file) in read mode using zipfile.ZipFile.
It extracts all the contents of the zip file into the specified directory path (unzip_path) using zip_ref.extractall.
Overall, this code defines a DataIngestion class that handles downloading a file from a URL and extracting the contents of a zip file into a directory. It utilizes
"""