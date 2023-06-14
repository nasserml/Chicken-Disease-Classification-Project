""" This code is a setup script for a Python package using setuptools. It defines the package metadata and configuration for the package installation. Here's a summary and explanation for each part of the code:

Importing the setuptools module for packaging and distribution.

Opening and reading the contents of the "README.md" file, which serves as the long description for the package.

Defining the version of the package. The current version is set to "0.0.0".

Defining variables for the repository name, author's username, source repository name, and author's email.

Calling the setup() function from setuptools to configure the package installation.

Providing various metadata and settings:
name: The name of the package (set to SRC_REPO).
version: The version of the package.
author: The author's username.
author_email: The author's email.
description: A brief description of the package.
long_description: The contents of the "README.md" file.
long_description_content: The type of content in the long description (set to "text/markdown").
url: The URL of the repository.
project_urls: Additional URLs related to the project (in this case, the Bug Tracker URL).
package_dir: A dictionary specifying the package directory (set to "": "src" to indicate that the packages are located in the "src" directory).
packages: Automatically finding and including all packages under the "src" directory using setuptools.find_packages().
This setup script sets up the package metadata, including its name, version, author information, and description. It also specifies the package's directory structure and includes the necessary packages for distribution. The long description is provided from the contents of the "README.md" file, and the package URL and Bug Tracker URL are set accordingly. """

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Chicken-Disease-Classification-Project"
AUTHOR_USER_NAME = "nasserml"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "mnasserone@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

""" 
This code is a setup script for a Python package using setuptools. It defines the package metadata and configuration for the package installation. Here's an explanation for each line of the code:

python
 
import setuptools
Importing the setuptools module for packaging and distribution.
python
 
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
Opening and reading the contents of the "README.md" file, which serves as the long description for the package.
python
 
__version__ = "0.0.0"
Defining the version of the package. The current version is set to "0.0.0".
python
 
REPO_NAME = "Chicken-Disease-Classification-Project"
AUTHOR_USER_NAME = "nasserml"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "mnasserone@gmail.com"
Defining variables for the repository name, author's username, source repository name, and author's email.
python
 
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
Calling the setup() function from setuptools to configure the package installation.
Providing various metadata and settings:
name: The name of the package (set to SRC_REPO).
version: The version of the package.
author: The author's username.
author_email: The author's email.
description: A brief description of the package.
long_description: The contents of the "README.md" file.
long_description_content: The type of content in the long description (set to "text/markdown").
url: The URL of the repository.
project_urls: Additional URLs related to the project (in this case, the Bug Tracker URL).
package_dir: A dictionary specifying the package directory (set to "": "src" to indicate that the packages are located in the "src" directory).
packages: Automatically finding and including all packages under the "src" directory using setuptools.find_packages().
This setup script defines the package metadata, including its name, version, author information, and description. It also specifies the package's directory structure and includes the necessary packages for distribution.
"""