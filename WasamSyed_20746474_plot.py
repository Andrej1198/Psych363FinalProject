import pandas as p
from pandas_read_csv import data
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Collecting experiment data from .csv and storing in a new dataframe with new index
newdat = data
newdat.index = list(range(len(data.index)))
i = 0
while (i < len(newdat.index)):
    if (newdat.iloc[i]['Correct'] == 0.0):
        newdat.drop(index = i, inplace=True)
        i += 1
    else: 
        i += 1
curr_len = len(newdat.index)
newdat.index = list(range(curr_len))

# Adding congruency column and cleaning the dataset  

newdat['Congruency'] = ''
ind2 = 0
while (ind2 < len(newdat.index)):
    if (newdat.iloc[ind2]['Word'] == newdat.iloc[ind2]['Ink']):
        newdat.iat[ind2,4] = 'Congruent'
        ind2 += 1
    else:
        newdat.iat[ind2,4] = 'Incongruent'
        ind2 += 1
        
newdat.drop(columns=['Word','Ink'], inplace = True)

# Creating the boxplot

sns.boxplot(x = newdat['Congruency'], y = newdat['Response Time'], data = newdat)
plt.ylim(0,3.0)
plt.show()

# T-test:

t_test_lst = stats.ttest_ind(newdat[newdat['Congruency']=='Congruent']['Response Time'],(newdat[newdat['Congruency']=='Incongruent']['Response Time'][0:174])) 
print(t_test_lst)

