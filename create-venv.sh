#!/bin/bash

if [ -d ".venv" ]; then
    echo ".venv folder already exists. Skipping."
    exit 0
fi

echo "Checking global Python version..."

echo $(python --version)

if [ ! "$(python --version | grep '3.10')" ]; then
    echo "ERROR: Python 3.10 is required!"
    exit 1
fi

echo "Creating virtual environment..."

python -m venv .venv

echo ".venv created!"
