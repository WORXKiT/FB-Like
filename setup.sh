#!/usr/bin/env bash
update
sudo apt-get install python3-pip
sudo pip3 install virtualenv
source ./venv/bin/activate
pip freeze > requirements.txt
pip install -r requirements.txt
deactivate
