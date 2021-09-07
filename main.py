from Code.backCode.preFiltering import *
from Code.backCode.editingFiles import *
from Code.backCode.makeOtherFiles import *
import time
import os.path

def createFilesDirectory(directoryName):
    if not os.path.exists(topPath + "\\" + "files"):
        os.makedirs(topPath + "\\" + "files")

    os.makedirs(filesPath)
    time.sleep(2000)
        
else:
    pass

def main():
    getFiles()
    time.sleep(1)
    joinCSVs()
    time.sleep(1)
    editCSV()
    time.sleep(1)
    finalCSVedits()
    time.sleep(1)
    convertExcel()



if __name__ == "__main__":
    main() 