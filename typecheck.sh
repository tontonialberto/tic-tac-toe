#!/bin/bash

cd src && python -m mypy --install-types --non-interactive --explicit-package-bases \
    -m __main__ -p tictactoe -p test