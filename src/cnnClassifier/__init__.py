""" 
This code sets up a logging configuration for a CNN classifier. Here's a breakdown of what it does:

Importing the necessary modules:

os: Provides functions for interacting with the operating system.
sys: Provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter.
logging: Provides a flexible framework for emitting log messages from Python programs.
Defining the logging format:

The logging_str variable defines the format of the log messages using a specific pattern. It includes the timestamp, log level, module name, and log message.
Setting up the log directory:

The log_dir variable specifies the directory where the log files will be stored.
The log_filepath variable defines the complete file path of the log file by joining the log directory path with the log file name.
The os.makedirs() function is used to create the log directory if it doesn't already exist. The exist_ok=True argument ensures that the function does not raise an exception if the directory already exists.
Configuring the logging:

The basicConfig() function from the logging module is called to configure the logging system.
The level=logging.INFO parameter sets the logging level to INFO, which means that log messages with a severity level of INFO or higher will be logged.
The format=logging_str parameter sets the log message format to the value specified in the logging_str variable.
The handlers parameter specifies the handlers to be used for logging. In this case, it includes two handlers:
logging.FileHandler(log_filepath): Writes log messages to the file specified by log_filepath.
logging.StreamHandler(sys.stdout): Writes log messages to the standard output (console).
Creating the logger:

The getLogger() function is called to create a logger object named "cnnClassifierLogger". This logger can be used to emit log messages throughout the program.
Overall, this code sets up a logging configuration that logs messages to both a file and the console, with the log format specified in logging_str. The log files are stored in the "logs" directory, and the logger object named "cnnClassifierLogger" can be used to emit log messages in the program.
"""



import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")

""" 
import os: Imports the os module, which provides functions for interacting with the operating system.

import sys: Imports the sys module, which provides access to some variables used or maintained by the interpreter and functions that interact with the interpreter.

import logging: Imports the logging module, which provides a flexible framework for emitting log messages from Python programs.

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]": Defines a string format for log messages using a specific pattern. It includes placeholders for the timestamp (asctime), log level (levelname), module name (module), and log message (message).

log_dir = "logs": Specifies the name of the log directory where log files will be stored.

log_filepath = os.path.join(log_dir,"running_logs.log"): Constructs the file path of the log file by joining the log directory path (log_dir) with the log file name (running_logs.log).

os.makedirs(log_dir, exist_ok=True): Creates the log directory specified by log_dir. The exist_ok=True argument ensures that the function does not raise an exception if the directory already exists.

logging.basicConfig(...): Configures the logging system using the basicConfig() function from the logging module. It sets the logging level, log format, and handlers.

level=logging.INFO: Sets the logging level to INFO, which means that log messages with a severity level of INFO or higher will be logged.
format=logging_str: Sets the log message format to the value specified in the logging_str variable.
handlers=[...]: Specifies the handlers to be used for logging. In this case, it includes two handlers:
logging.FileHandler(log_filepath): Writes log messages to the file specified by log_filepath.
logging.StreamHandler(sys.stdout): Writes log messages to the standard output (console).
logger = logging.getLogger("cnnClassifierLogger"): Creates a logger object named "cnnClassifierLogger" using the getLogger() function from the logging module. This logger can be used to emit log messages throughout the program.

Overall, this code sets up a logging configuration that logs messages to both a file and the console, with the log format specified in logging_str. The log files are stored in the "logs" directory, and the logger object named "cnnClassifierLogger" can be used to emit log messages in the program.
"""