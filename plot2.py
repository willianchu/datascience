from ctypes.wintypes import HINSTANCE


# color of Histogram
.plot(kind="hist", edgecolor="black", linedwith=1.2)


kind='line' : line chart (default value)
kind='box' : boxplot # retrieve the max and min of each column
kind='hist' : histogram # counts how many times each value appears
kind='bar' : bar chart # reflects the line chart but bars are used

import pandas as pd

df = pd.read_csv('aus_weather.csv')
df = df[df["Location"] == "Melbourne"]
df.head()


