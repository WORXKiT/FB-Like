#!/usr/bin/env bash
sudo apt update
sudo apt-get install python3-pip
sudo pip3 install virtualenv
source ./venv/bin/activate
pip install -r requirements.txt
deactivate
