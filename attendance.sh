#!/bin/bash
echo "Activating Virtual Environment..."
. env/bin/activate
echo "Starting Attendance Script..."
echo "-----------------------------------"
python attendance.py
echo "Exiting Attendance Script..."
echo "-----------------------------------"
