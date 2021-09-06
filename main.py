from Code.backCode.preFiltering import getFiles
from Code.backCode.editingFiles import editFile
from Code.backCode.makeOtherFiles import finalFunction

def mainFunc():
    getFiles()
    editFile()
    finalFunction()

if __name__ == "__main__":
    mainFunc()