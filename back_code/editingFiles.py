from os import path
import pandas as pd
from pre_filtering import * #imports variables and code like Im using this file
import numpy as np
import glob
import os
from datetime import datetime
#variables are like this: "path". Not this:"pre_filtering.path"

"""
what is glob and datetime module?
explore map function algorithm
"""

filesRenamed_path = path + "\\filesRenamed"
onlyfiles = next(os.walk(filesRenamed_path))[2] #dir is your directory path as string

all_files = glob.glob(filesRenamed_path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)


    del df["fund"]
    del df["date"]
    del df["ticker"]
    del df["cusip"]
    del df["weight(%)"]
    df.drop(df.tail(3).index,inplace=True) # drop last 4 rows

    li.append(df)