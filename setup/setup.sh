#!/bin/bash

echo "Project Setup Script for macOS"

# create virtual environment
echo "Creating virtual environment"
python3 -m venv myenv

# Activate virtual environment
echo "Activating virtual environment"
source myenv/bin/activate

# Install packages
echo "Installing project requirements"
pip install -r requirements.txt