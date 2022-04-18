#import the pandas plugin
from tkinter.tix import COLUMN
import pandas as pd # pd is the alias we have given to pandas.

# To Read a Dataset
# paris_landmarks.csv is stored into a Pandas DataFrame variable called df.
df = pd.read_csv('paris_landmarks.csv')

#df.head() function displays the first 5 rows of the dataset
df.head()

df.describe() # gives the summary of the dataset
df['column'].unique() # gives the unique values of the dataset
pd.unique(df)

print(df.name.unique())
print(pd.unique(df['year']))

or

c = "year"
pd.Series({c: df[c].unique() for c in df}) #query the unique values of the column


df.shape # gives the shape of the dataset
df.sort_values("column") # sorts the dataset based on the values

df.info # gives the information about the dataset
df.max() # gets the max value from a column
df.min() # gets the min value from a column
df.mean() # get the mean value from a column
df.idxmax() # gets the integer index position of the max value from a column
df.idxmin() # gets the integer index position of the min value from a column
df.loc() # gets rows (or columns) with particular labels from the index
df.iloc() # gets rows (or columns) with particular positions in the index (only takes integers)

df.sort_values(by=['column_name'], ascending = False)

# Challenge
# After playing around with the functions above, you can help Dot by answering following questions about Paris landmarks:

# What is the most expensive landmark in Paris?
# What is the average wait time for all landmarks?

sortByPrice = df.sort_values(by=['price'], ascending = False)
highest = sortByPrice.head(1)
highest.landmark

#OR

col = "price"
max_x = df.loc[df[col].idxmax()] # locate [ the max index of the column ]
print(max_x)

df["queue_time"].mean() # average wait time for all landmarks ignoring nan

#OR
sortByPrice = df.sort_values(by=['price'], ascending = False)
sortByPrice.iloc[0]

#OR
col = "price"
realIdx = df[col].idxmax() - 1 # locate [ the max index of the column ]
sortByPrice.iloc[realIdx]

#return the 10th indexed row
df = pd.read_csv('paris_landmarks.csv')
item_10 = df.iloc[10]

#return the price column of the 10th indexed row
item_10.['price']
>5


