peaks_above_8k = pd.read_sql('select COUNT() from peaks where heightm > 8000  ',conn)

import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect("world.db")

# Pull the data from the worldcities table in the world.db database to the pandas DataFrame

pd = pd.read_sql('select * from worldcities',conn)

pd.groupby('country').count()

# the population of the top 10 most populated countries
top10 = pd.read_sql('select * from worldcities order by population desc limit 10',conn)

top10sql = pd.read_sql('select * from worldcities order by population desc limit 10',conn)

# 10 countries with the highest population

population_by_country = pd.read_sql('select * from worldcities group by country order by population desc limit 10',conn)

# ignoring NaN values and none values
valid_population = pd.read_sql('select * from worldcities where population is not null',conn)

#Using a Matplotlib histogram, visualize the distribution of population across all cities. What do you observe?

plt.figure()
plt.hist(df[df['city_ascii']]['population'], bins = 30) #Play around with the bin sizes when plotting your histogram
plt.show()

# sorting
# Series.sort_values(axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')
