from Code.backCode.preFiltering import *
from Code.backCode.editingFiles import *
import pandas as pd
import os

finalfile_name = "Análise-ark-invest_" + getDate() + ".csv"
filesfinalDirectory_path = topPath + "\\" + "files" + "\\" + "filesFinal"
finalfile_path = os.path.join(filesFinal_path, finalfile_name)

df = pd.read_csv(finalfile_path)
pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', None)  # or 199

def intColumnValuesRedable(dataframe, columnName):
    roundedValue = []
    finalValues = []

    for value in dataframe[columnName]:
        value = int(value)
        value = round(value)
        roundedValue.append(value)

    for value in roundedValue:
        value = format(value, ',d')
        finalValues.append(value)

    dataframe[columnName] = finalValues
    dataframe.to_csv(finalfile_path, index= False)

def finalCSVedits():
    intColumnValuesRedable(df, "Market-value($)")
    intColumnValuesRedable(df, "Shares")

    del df["Index"]
    df.to_csv(finalfile_path, index= False)

def removeDirectory(path):
    os.rmdir(path)

def convertExcel():
    global finalexcelfile_path
    try:
        df = pd.read_csv(finalfile_path)
        finalexcelfile_path = os.path.join(filesfinalDirectory_path, "Análise-ark-invest_" + getDate() + ".xlsx")
        df.to_excel(finalexcelfile_path)
        os.remove(finalfile_path)
    except:
        print("Warning - Either the file has already been coverted or it has not been created")
    
    
def finalFunction():
    finalCSVedits()
    convertExcel()
    removeDirectory(filesRenamed_path)

if __name__ == "__main__":
    finalFunction()