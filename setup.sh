#!/usr/bin/env bash
sudo apt update
sudo apt-get install python3-pip
sudo pip3 install virtualenv
virtualenv -p /usr/bin/python2.7 venv
source ./venv/bin/activate
pip freeze > requirements.txt
pip install -r requirements.txt
deactivate
