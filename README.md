# Chicken-Disease-Classification--Project


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/Chicken-Disease-Classification--Project
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




# AZURE-CICD-Deployment-with-Github-Actions

## Save pass:

s3cEZKH5yytiVnJ3h+eI3qhhzf9q1vNwEi6+q+WGdd+ACRCZ7JD6


## Run from terminal:

docker build -t chickenapp.azurecr.io/chicken:latest .

docker login chickenapp.azurecr.io

docker push chickenapp.azurecr.io/chicken:latest


## Deployment Steps:

1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure 
4. Pull the Docker image from the container registry to Web App server and run 

# Chicken Disease Classification Project

This project aims to classify chicken diseases using machine learning techniques.

## Project Structure

- [config/](config)
  - [config.yaml](config/config.yaml): Configuration file for the project.
- [research/](research)
  - [01_data_ingestion.ipynb](research/01_data_ingestion.ipynb): Notebook for data ingestion.
  - [02_prepare_base_model.ipynb](research/02_prepare_base_model.ipynb): Notebook for preparing the base model.
  - [03_prepare_callbacks.ipynb](research/03_prepare_callbacks.ipynb): Notebook for preparing callbacks.
  - [04_training.ipynb](research/04_training.ipynb): Notebook for training the model.
  - [05_model_evaluation.ipynb](research/05_model_evaluation.ipynb): Notebook for model evaluation.
  - [trials.ipynb](research/trials.ipynb): Notebook for experimental trials.
- [src/cnnClassifier/](src/cnnClassifier)
  - [components/](src/cnnClassifier/components)
    - [__init__.py](src/cnnClassifier/components/__init__.py)
    - [data_ingestion.py](src/cnnClassifier/components/data_ingestion.py): Data ingestion component.
    - [evaluation.py](src/cnnClassifier/components/evaluation.py): Evaluation component.
    - [prepare_base_model.py](src/cnnClassifier/components/prepare_base_model.py): Base model preparation component.
    - [prepare_callbacks.py](src/cnnClassifier/components/prepare_callbacks.py): Callbacks preparation component.
    - [training.py](src/cnnClassifier/components/training.py): Training component.
  - [config/](src/cnnClassifier/config)
    - [__init__.py](src/cnnClassifier/config/__init__.py)
    - [configuration.py](src/cnnClassifier/config/configuration.py): Configuration module.
  - [constants/](src/cnnClassifier/constants)
    - [__init__.py](src/cnnClassifier/constants/__init__.py)
    - [entity/](src/cnnClassifier/constants/entity)
      - [__init__.py](src/cnnClassifier/constants/entity/__init__.py)
      - [config_entity.py](src/cnnClassifier/constants/entity/config_entity.py): Configuration entity module.
  - [pipeline/](src/cnnClassifier/pipeline)
    - [__init__.py](src/cnnClassifier/pipeline/__init__.py)
    - [predict.py](src/cnnClassifier/pipeline/predict.py): Prediction pipeline.
    - [stage_01_data_ingestion.py](src/cnnClassifier/pipeline/stage_01_data_ingestion.py): Data ingestion stage of the pipeline.
    - [stage_02_prepare_base_model.py](src/cnnClassifier/pipeline/stage_02_prepare_base_model.py): Base model preparation stage of the pipeline.
    - [stage_03_training.py](src/cnnClassifier/pipeline/stage_03_training.py): Training stage of the pipeline.
    - [stage_04_evaluation.py](src/cnnClassifier/pipeline/stage_04_evaluation.py): Evaluation stage of the pipeline.
  - [utils/](src/cnnClassifier/utils)
    - [__init__.py](src/cnnClassifier/utils/__init__.py)
    - [common.py](src/cnnClassifier/utils/common.py): Common utility functions.
- [templates/](templates)
  - [index.html](templates/index.html): HTML template.
- [.dvcignore](.dvcignore): DVC ignore file.
- [.gitignore](.gitignore): Git ignore file.
- [Dockerfile](Dockerfile): Docker configuration file.
- [LICENSE](LICENSE): License file.
- [README.md](README.md): Project documentation (you are here!).
- [app.py](app.py): Main application file.
- [dvc.lock](dvc.lock): DVC lock file.
- [dvc.yaml](dvc.yaml): DVC configuration file.
- [inputImage.jpg](inputImage.jpg): Sample input image.
- [main.py](main.py): Main script.
- [params.yaml](params.yaml): Parameters file.
- [requirements.txt](requirements.txt): Project dependencies.
- [scores.json](scores.json): Model evaluation scores.
- [setup.py](setup.py): Project setup file.
- [template.py](template.py): Template file.

## License

This project is licensed under the [MIT License](LICENSE).