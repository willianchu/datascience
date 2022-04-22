# Challenge
# Step I: Using the season column, filter the DataFrame so it contains only rows for summer and winter.

# Step II:Using groupby() and unstack(), compute the difference between the average temperature in summer and winter(at 9am) for all locations.

# Question: What is the difference between the average summer temperatures (using variable Temp9am) and the average winter temperatures (using variable Temp9am) for Adelaide, Albany and Albury?

import pandas as pd
df = pd.read_csv('aus_weather.csv')
df.head()

filtered = df[(df['season'] == 'summer') | (df['season'] == 'winter')]
# filtered.head()

grouped = filtered.groupby(['Location','season'])['Temp9am'].mean()
organized = grouped.unstack(level=1) # rotate the dataframe inside the grouped

view = organized.assign(diff = organized['summer'] - organized['winter'])

# only Adelaide, Albany and Albury index
view.loc[['Adelaide','Albury','Albany']]
