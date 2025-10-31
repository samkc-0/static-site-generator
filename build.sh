#!/bin/bash

# this script build the repo for github pages
# make sure you have a .env with REPONAME set
# source .env
# if [ -z "$REPONAME" ]; then
#   echo "REPONAME is not set in .env"
#  exit 1
#fi

mkdir -p docs
python src/main.py "/" docs
