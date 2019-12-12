import PyQt5.uic as uic
from PyQt5.pyrcc_main import *
import glob

files = glob.glob("*.ui")
resourcefiles = glob.glob("*.qrc")
for file in files:
    filename = file[:-2]+"py"
    fp = open(filename, "w", encoding="utf-8")
    uic.compileUi(file,fp, from_imports=True)
    fp.close()

# for file in resourcefiles:
#     print(file)
#     filename = file[:-4]+"_rc.py"
#     print(filename)
#     processResourceFile(file, filename, True)

print("Done.")