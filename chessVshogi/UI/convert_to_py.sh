#!/usr/bin/env bash
if [ "$#" -ne 1 ]; then
  c=0
  for f in *.ui
  do
    ui_file=$(basename -- "$f")
    python_file="${ui_file%.*}.py"
    pyuic5 ${ui_file} -o ${python_file}
    ((c+=1))
  done
  echo "Converted $c files succesfully"
else
  ui_file=$(basename -- "$1")
  python_file="${ui_file%.*}.py"

  pyuic5 ${ui_file} -o ${python_file}
  echo "Converted ${ui_file} to a python file succesfully"
fi