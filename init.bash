#!/bin/bash

# sets up the venv for first time cloned repo
pip install virtualenv

env_name=daemona_env

echo $env_name

# create venv
virtualenv "$env_name"

# activate the env
source "$env_name"/bin/activate 

# update pip
pip install --upgrade pip

# install required packages
pip install -r requirements.txt

# install wordnet for natural language processing
python3 init.py