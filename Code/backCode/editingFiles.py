from preFiltering import *
import pandas as pd
import numpy as np
import glob
import os

filesRenamed_path = topPath + "\\" + "files" + "\\" + "filesRenamed"
filesFinal_path = topPath + "\\" + "files" + "\\" + "filesFinal"
np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)

pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', None)  # or 199

def delColumns(dataFrame):
    del dataFrame["fund"]
    del dataFrame["date"]
    del dataFrame["ticker"]
    del dataFrame["cusip"]
    del dataFrame["weight(%)"]

def joinCSVs():
    global finalfile_name
    global finalfile_path
    global finalfileHeader

    #li = []

    # merging the files
    joined_files = os.path.join(filesRenamed_path, "*.csv")
    # A list of all joined files is returned
    joined_list = glob.glob(joined_files)
    # Finally, the files are joined
    df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)

    delColumns(df)

    df.drop(df.tail(3).index,inplace=True) # drop last 4 rows
    df.dropna(axis=0, how='all', thresh=None, subset=None, inplace=True)

    finalfile_name = "Análise-ark-invest.csv"
    finalfile_path = os.path.join(filesFinal_path, finalfile_name)

#turn this in an actual CSV file
    finalfileHeader= ['Index', 'Companies', 'Shares', 'Market-value($)']
    df.reset_index(inplace=True)

    df.to_csv(finalfile_path, index= False, header=finalfileHeader)


def removeSpacesColumnsVals(dataFrame):
    #remove spaces from companies names
    fileCompanies = dataFrame["Companies"]
    finallistCompanies = []
    for company in fileCompanies:
        companyUnsorted = list(company)
        companySorted = ["-" if character==" " else character for character in companyUnsorted ]
        company = "".join(map(str,companySorted))
        finallistCompanies.append(company)
    dataFrame.Companies = finallistCompanies
    dataFrame.to_csv(finalfile_path, index= False)


def sortByMarketVal(dataFrame):
    dataFrame = dataFrame.sort_values(by = 'Market-value($)', ascending=False)
    dataFrame.to_csv(finalfile_path, index= False)
    dataFrame.to_csv(finalfile_path, index= False)


def editCSV():
    global df
    df = pd.read_csv(finalfile_path)
    duplicateRowsDF = df[df.duplicated(["Companies"])]["Companies"] #we add ["Companies"] to the end, to say(I only want Companies collum)
    listofDupli = list(set(duplicateRowsDF))#set removes duplicates of list. We get a list of duplicated companies names

    removeSpacesColumnsVals(df)

    #Add and join summed values to rows
    for company in listofDupli:
        duplicatedcompaniesData = [len(df.index), company,  df[df['Companies']==company]['Shares'].sum(), df[df['Companies']==company]['Market-value($)'].sum()]
    df = df.drop_duplicates(subset=["Companies"])
    df.to_csv(finalfile_path, index= False)
    df.loc[len(duplicatedcompaniesData)] = duplicatedcompaniesData
    df.to_csv(finalfile_path, index= False)

    sortByMarketVal(df)
  
    
if __name__ == "__main__":
    joinCSVs()
    editCSV()