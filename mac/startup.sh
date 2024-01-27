#! /bin/bash
pip3 install poetry
cd ..
cd skybrush-server
poetry install
poetry run skybrushd