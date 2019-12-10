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
  echo "Converted $c UI files succesfully"
  c=0
  for f in *.qrc
  do
    resource_file=$(basename -- "$f")
    python_file="${resource_file%.*}_rc.py"
    pyrcc5 ${resource_file} -o ${python_file}
    ((c+=1))
  done

  echo "Converted $c resource files succesfully"
else
  ui_file=$(basename -- "$1")
  python_file="${ui_file%.*}.py"

  pyuic5 ${ui_file} -o ${python_file}
  echo "Converted ${ui_file} to a python file succesfully"
fi