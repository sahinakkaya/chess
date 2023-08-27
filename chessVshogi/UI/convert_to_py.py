import glob
import os

files = glob.glob("*.ui")
resourcefiles = glob.glob("*.qrc")
for file in files:
    file_out = file[:-2]+"py"
    os.system("python -m PyQt6.uic.pyuic {} -o {}".format(file, file_out))

for file in resourcefiles:
    file_out = file[:-4]+"_rc.py"
    os.system("python -m PyQt6.pyrcc_main {} -o ../../{}".format(file, file_out))

print("Done.")
