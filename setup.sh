#!/bin/bash
echo "-----------------------------------"
echo "Creating Virtual Environment..."
python3 -m venv env
echo "Activate Virtual Environment..."
. env/bin/activate
echo "Installing Requirements..."
pip install -r requirements.txt
echo "Requirements Installed Successfully!"
echo "-----------------------------------"
