from preFiltering import *
from editingFiles import *
import pandas as pd
import os
import shutil
finalfile_name = "Análise-ark-invest.csv"
filesRenamed_path = topPath + "\\" + "files" + "\\" + "filesRenamed"
filesFinal_path = topPath + "\\" + "files" + "\\" + "filesFinal"


finalfile_path = os.path.join(filesFinal_path, finalfile_name)

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
    df = pd.read_csv(finalfile_path)

    intColumnValuesRedable(df, "Market-value($)")
    intColumnValuesRedable(df, "Shares")

    del df["Index"]
    df.to_csv(finalfile_path, index= False)
    os.remove(finalfile_path)
    
def removeDirectory(path):
    shutil.rmtree(path)

def convertExcel():
    global finalexcelfile_path
    try:
        df = pd.read_csv(finalfile_path)
        finalexcelfile_path = os.path.join(filesFinal_path, "Análise-ark-invest.xlsx")
        df.to_excel(finalexcelfile_path)
    except:
        print("Warning - Either the file has already been coverted or it has not been created")

    removeDirectory(filesRenamed_path)