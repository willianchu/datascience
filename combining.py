# We will be using data that contains traffic information for New Zealand during the year 2020.
import pandas as pd
df = pd.read_csv('nz_car_traffic.csv')
df.head()

# 	startDate	regionName	classWeight	flowDirection	trafficCount	month
# 0	2020-01-01	03 - Waikato	Heavy	2	436.0	2020-01
# 1	2020-01-01	03 - Waikato	Light	2	9700.0	2020-01
# 2	2020-01-01	03 - Waikato	Light	1	9398.5	2020-01
# 3	2020-01-01	03 - Waikato	Heavy	1	486.5	2020-01
# 4	2020-01-01	11 - Canterbury	Light	2	494.5	2020-01

# Challenge
# Find the region (using variable regionName) with the lowest total amount of light (using variable classWeight) traffic, and the region with the lowest total amount of heavy (using variable classWeight) traffic

# Print the region name and the total traffic count for the light and heavy traffic
%matplotlib notebook

import matplotlib.pyplot as plt

graph = df.groupby(['month']).sum().sort_values(['trafficCount'])
graph.plot(kind='bar')

plt.show ()

# Using a bar chart, which month had the lowest amount of total traffic in 2020?
df.groupby(['month']).sum().sort_values(['trafficCount'])
df.plot.bar(x='month', y='trafficCount')

# Direct answer: April
df.groupby(['month']).sum().sort_values(['trafficCount']).sort_values('trafficCount')

# What percent of New Zealand’s traffic (using variable trafficCount) was classified as heavy (using variable classWeight) in 2020?
view = df.groupby(['classWeight']).sum()
percentage = view['trafficCount'] / view['trafficCount'].sum()
percentage

