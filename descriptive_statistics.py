# using pandas to calculate descriptive statistics

import pandas

list_of_num = [1,2,3,4,5]

series = pandas.Series(list_of_num) #converting our list_of_num to a pandas series variable
                                #we need to do this to use some of pandas' useful descriptive statistics functions

print(series.max())
    #outputs maximum value in Pandas Series
print(series.min())
    #outputs minimum value in Pandas Series
print(series.mean())   #outputs average value in Pandas Series

print(series.median())
 #outputs median value in Pandas Series
print(series.mode())   #outputs mode value in Pandas Series

df = pandas.DataFrame({"A": [1,2,3,4,5], "B": [1,2,3,4,5]})
# return max value in column
col = "A"
max_x = df.loc[df[col].idxmax()]

# remove nan values
df2 = df.dropna()

# calculationg average ignoring nan values
df2.mean()

# max games
col = "MP"
max_games = df.loc[df[col].idxmax()]
print(max_games)

#Attendance average
atendance_average = df.mean()

print(atendance_average)


#specificcolumn

print(df["MP"].mean())

# difference between average of wins and losses

print(df["W"].mean()-df["L"].mean())


points = df.Pts
games_played = df.MP
wins = df.W
losses = df.L
attendance = df.Attendance.dropna() # skipping missing values (NaN) because there were no fans during 2020-2021 season because of COVID

# Difference between Max and Min Pts
print(points.max())

print(points.min())

print(games_played.max())
print(attendance.mean())
print(wins.median() - losses.median())
print(wins.min())
print(points.max() - points.min())

series.max()    #outputs maximum value in Pandas Series
series.min()    #outputs minimum value in Pandas Series
series.mean()   #outputs average value in Pandas Series
series.median() #outputs median value in Pandas Series
series.mode()   #outputs mode value in Pandas Series

df.mode() # will output the dataframe without the NaN values and index
df.mode(dropna=False) # will output the dataframe with the NaN values 
df.mode(numeric_only=True) # will output the dataframe with numeric values only including the NaN values
df.mode(axis='columns', numeric_only=True) #  will output the dataframe with numeric values only including the NaN valueswith the index



