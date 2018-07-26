#!/usr/bin/env bash
source ./venv/bin/activate
pip freeze > requirements.txt
pip install -r requirements.txt
deactivate
