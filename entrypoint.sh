#!/bin/bash
set -e

export RED='\033[1;31m'
export BLUE='\033[1;34m'
export GREEN='\033[1;32m'
export NOCOLOR='\033[0m'

if [ -f /.dockerenv ]; then
    echo -e "${GREEN}"
    echo "This script is running inside docker, as it should 🤩"
    echo -e "${NOCOLOR}"
    python -m scanvulnpy -r /home/little-scripts/scanvulnpy/scanvulnpy-local-requirements.txt --verbose package
else
    echo -e "${RED}"
    echo "This script is not running inside docker, as it should 😢"
    echo -e "${NOCOLOR}"
    exit 1
fi
