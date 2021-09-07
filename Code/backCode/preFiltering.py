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

def createDirectory(pathToDirectory, directoryName):
    try:
        finalPath = os.path.join(pathToDirectory, directoryName)
        os.mkdir(finalPath)
    except:
        if os.path.isdir(finalPath) == True:
            print("Directories already exists")
            
    return finalPath


def getFiles():
    global filesRenamed_name
    global filesRenamed_path
    global numofFile
    
    #create directory with new directory for new files
    createDirectory(topPath + "\\" + "files", 'filesRenamed')
    createDirectory(topPath + "\\" + "files", 'filesFinal')

    numofFile = 1
    files = os.listdir(filesPath)

    for file in files:    
        os.rename(filesPath+'/' + file,  filesPath +str(numofFile)+'.csv')
        #delete "files directory"

        try:
            shutil.move(os.path.join(filesPath, filesPath+str(numofFile)+'.csv'), topPath + "\\" + "files" + "\\" +  "filesRenamed")
        except:
            if os.path.isdir('filesRenamed') and  os.path.isdir('filesFinal') == True:
                print("Directory already exists")

        numofFile = numofFile +1


if __name__ == "__main__":
    getFiles()
