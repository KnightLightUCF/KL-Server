#! /bin/bash
py -m pip install poetry
# cd ..
cd skybrush-server
poetry install
poetry run skybrushd