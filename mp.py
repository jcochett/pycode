#!/usr/bin/python
import os
import sys


cmd = os.popen('which python')
iline = "#!" + cmd.read()
sys.argv.pop(0)

for filename in sys.argv:
    print("Creating: " + filename)
    with open(filename, 'w') as file_object:
        file_object.write(iline)
    chmod = "chmod +x " + filename
    os.system(chmod)
