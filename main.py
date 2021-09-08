from Code.backCode.editingFiles import *
from Code.backCode.preFiltering import *
from Code.backCode.makeOtherFiles import *
import time



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




"""
def createFilesDirectory():
    if not os.path.exists(topPath + "\\" + "files"):
        os.makedirs(topPath + "\\" + "files")
        os.makedirs(topPath + "\\" + "files" + "\\" + "filesUnsorted")
        time.sleep(2000)
    else:
        pass
    
    if os.path.exists(topPath + "\\" + "files"):
        try:
            removeDirectory(finalfile_path)
        except:
            print("No finalFiles folder exists")   
            
             
        if not os.path.exists(topPath + "\\" + "files" + "\\" + "filesUnsorted"):
            os.makedirs(topPath + "\\" + "files" + "\\" + "filesUnsorted")
            time.sleep(2000)
        else:
            pass
"""