#!/bin/bash
echo "Activating Virtual Environment..."
. env/bin/activate
echo "Starting Meet Script..."
echo "-----------------------------------"
python automeet.py
echo "Exiting Meet Script..."
echo "-----------------------------------"
