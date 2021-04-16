import pandas as pd
import os

# Get all the files in directory
files = os.listdir()

# Identify all csv files in the directory
csv_files = []
for file in files:
    if file[-4:] == ".csv":
        csv_files.append(file)
data = pd.DataFrame()
for file in csv_files:
    data = data.append(pd.read_csv(file))

pd.set_option('display.max_rows', None)
print(data)
# Data is a pandas dataframe that has all the data from the csv files merged into 1 big data frame
