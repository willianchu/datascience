import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('air_traffic_data.csv')
df.head()

# columns
# PASSENGERS	DISTANCE	UNIQUE_CARRIER	UNIQUE_CARRIER_NAME	ORIGIN_AIRPORT_ID	ORIGIN	ORIGIN_CITY_NAME	DEST_AIRPORT_ID	DEST	DEST_CITY_NAME	YEAR	MONTH

# What is the origin city (using variable ORIGIN_CITY_NAME) with the highest total number of passengers who travelled to Vancouver?

#.match() to a partial match
# df[df['DEST_CITY_NAME'].str.match('Vancouver')]
# contains() partial match
# df[df['DEST_CITY_NAME'].str.contains("Vamcouver|Canada")]

flights_to_vancouver = df[df['DEST_CITY_NAME'].str.match('Vancouver')]

max_passengers_to_vancouver = flights_to_vancouver.groupby('ORIGIN_CITY_NAME').sum()['PASSENGERS'].max()

# plot histogram
plt.figure()
plt.hist(df[df['MONTH'] == 6]['DISTANCE'], bins = 30) #Play around with the bin sizes when plotting your histogram
plt.show()