#!/bin/bash

cd src && python -m coverage run -m unittest discover -s test -p Test*.py --verbose
coverage html -d ../coverage
coverage json -o ../coverage.json