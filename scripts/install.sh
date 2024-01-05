#!/bin/bash
sudo apt-get update
sudo apt-get install python3.8 python3-pip
python -m venv venv
pip install "fastapi[all]"
pip install -r requirements.txt

echo "installed all"
