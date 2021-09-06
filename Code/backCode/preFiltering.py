import numpy as np
import os
import shutil


topPath = os.getcwd()
filesPath = topPath + "\\" + "files" + "\\" + "filesUnsorted"

onlyfiles = next(os.walk(filesPath))[2] #dir is your directory path as string
numofFiles = len(onlyfiles)

lenFiles = np.arange(1, numofFiles + 1)
listnumFiles = list(map(str, lenFiles))

filesName = ["file"] * numofFiles
filesName = list(map(lambda x, y:x + y, filesName, listnumFiles))


def getFiles():
    global filesRenamed_name
    global filesRenamed_path
    global numofFile


#create directory with new directory for new files

    try:
        filesRenamed_name = "filesRenamed"
        filesRenamed_path = os.path.join(topPath + "\\" + "files", filesRenamed_name)
        os.mkdir(filesRenamed_path)
    except:
        if os.path.isdir(filesRenamed_name) == True:
            print("Directory already exists")

    numofFile = 1
    files = os.listdir(filesPath)

    for file in files:    
        os.rename(filesPath+'/' + file,  filesPath +str(numofFile)+'.csv')
        #delete "files directory"

        try:
            shutil.move(os.path.join(filesPath, filesPath+str(numofFile)+'.csv'), filesRenamed_path)
        except:
            if os.path.isdir(filesRenamed_name) == True:
                print("Directory already exists")

        numofFile = numofFile +1

if __name__ == "__main__":
    getFiles()