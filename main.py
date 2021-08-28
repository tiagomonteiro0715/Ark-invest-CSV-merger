import pandas as pd
import numpy as np
import os
from os import path
import shutil

"""
file questions:

next() function 
os.walk function
why[2]?
array = np.arange(1, numofFiles + 1) - dont use numpy or other modules
understand how the lambda function works
what is shutil module?

Syntax: os.mkdir(path, mode = 0o777, *, dir_fd = None)


understand well parameters:
Parameter:
path: A path-like object representing a file system path. A path-like object is either a string or bytes object representing a path.
mode (optional): A Integer value representing mode of the directory to be created. If this parameter is omitted then default value Oo777 is used.
dir_fd (optional): A file descriptor referring to a directory. The default value of this parameter is None.
If the specified path is absolute then dir_fd is ignored.


"""

""""


"""

path = "."
pathtoFiles = "./files"

onlyfiles = next(os.walk(pathtoFiles))[2] #dir is your directory path as string
numofFiles = len(onlyfiles)

listnumFiles = np.arange(1, numofFiles + 1)
listnumFiles = list(map(str, listnumFiles))

filesName = ["file"] * numofFiles
filesName = list(map(lambda x, y:x + y, filesName, listnumFiles))

#create directory with new directory for new files
try:
    filesRenamed_name = "filesRenamed"
    filesRenamed_path = os.path.join(path, filesRenamed_name)
    os.mkdir(filesRenamed_path)
except:
    if os.path.isdir(filesRenamed_name) == True:
        print("Directory already exists")


#rename files -- ver se usi mkdir() ou mkdirs()
numofFile = 0
for file in os.listdir(pathtoFiles):
    os.rename(pathtoFiles+'/'+file, pathtoFiles+str(numofFile)+'.csv')
    numofFile = numofFile +1

"""
minha ideia - usar um for loop para aceder a todos os ficheiros e usar if and else para filtrar todos os ficheiros csv

move files


for file in os.walk(path): 
    if :
        shutil.move(path,filesRenamed_path)
    else:
        if 
"""

def getFiles():
    return 0

    #create past with shorted values 
    #create a list of values - list >> something that can´t be changed
    #values and files - in a dictionary
    #after everything - elmininate all used files
