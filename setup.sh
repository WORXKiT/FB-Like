#!/usr/bin/env bash
sudo apt -f install
sudo apt update
sudo apt-get install python3-pip
pip install -r requirements.txt --user
