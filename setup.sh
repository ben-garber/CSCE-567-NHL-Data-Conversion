#!/usr/bin/env bash


pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
