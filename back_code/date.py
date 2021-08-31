from datetime import datetime
from pre_filtering import * #imports variables and code like Im using this file
import pandas as pd

def getDate():
    filesRenamed_path = path + "\\filesRenamed"
    onlyfiles = next(os.walk(filesRenamed_path))[2] #dir is your directory path as string

    filetogetDate = filesRenamed_path + "\\" + "files1.csv"
    datedf = pd.read_csv(filetogetDate)
    datefromFile = datedf.iloc[5]["date"]

    date_list = list(datefromFile)
    date_list = ["-" if value=="/" else value for value in date_list] 
    unsortedDate = "".join(map(str,date_list))#8-27-2021

    datetimeobject = datetime.strptime(unsortedDate,'%m-%d-%Y')
    title_date = datetimeobject.strftime('%d-%m-%Y') # date I will use as a name for csv file

    return title_date
    
if __name__ == "__main__":
    getDate()