import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


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


# Average Congruent vs Incongruent Time
congruent = np.array([])
incongruent = np.array([])
for i in data.iterrows():
    if i[1]['Correct']:
        if i[1]['Word'] != i[1]['Ink']:
            congruent = np.append(congruent, i[1]['Response Time'])
        else:
            incongruent = np.append(incongruent, i[1]['Response Time'])

print(np.average(congruent))
print(np.average(incongruent))
print("DONE")

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
state = ['Congruent', 'Incongruent']
average = [np.average(congruent)*1000, np.average(incongruent)*1000]
ax.bar(state, average)
plt.show()


# Correct and incorrect count
correct = 0
wrong = 0
for i in data.iterrows():
    if not i[1]['Correct']:
        if i[1]['Word'] == i[1]['Ink']:
            correct+=1
        else:
            wrong+=1

print("DONE")
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
correctness = ['Correct', 'Incorrect']
count = [correct, wrong]
ax.bar(correctness, count)
plt.show()