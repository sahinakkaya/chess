#!/usr/bin/env bash

ui_file=$(basename -- "$1")
python_file="${ui_file%.*}.py"

pyuic5 ${ui_file} -o ${python_file}