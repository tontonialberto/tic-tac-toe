#!/bin/bash

cd src && python -m coverage run -m unittest discover -s test -p Test*.py
coverage report