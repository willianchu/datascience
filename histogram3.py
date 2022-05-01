# Challenge

# Pull the data from the worldcities table in the world.db database to the pandas DataFrame, then answer the following questions:

import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect("world.db")

countries_population = pd.read_sql('select * from worldcities',conn)

# Using a Matplotlib histogram, visualize the distribution of population across all cities. What do you observe? Japan is the most populated country. the average population of the top 10 most populated countries is around 3.5 million.

plt.figure()
plt.hist(countries_population['population'], bins = 30) #Play around with the bin sizes when plotting your histogram
plt.show()

# Create a bar chart with the population of the top 10 most populated countries. Which country is most populated?

population_by_country = pd.read_sql('select * from worldcities group by country order by population desc limit 10',conn)

plt.figure()
plt.bar(population_by_country['country'], population_by_country['population'])
plt.show()

# What is the difference in population between the most populated city and the least populated city?

#forcing x-axis to be in millions
plt.ticklabel_format(axis="x", style="sci", scilimits=(6,6))
