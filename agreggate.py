# import pandas as pd
# df = pd.read_csv('dubai_properties_data.csv')

# # old way - averages of both columns were computed for each neighborhood
# df.groupby(['neighborhood'])[["price","price_per_sqft"]].mean()

# # new way - using the aggregate function .agg()
# df.groupby(['neighborhood']).agg({'price' : 'mean', 'price_per_sqft' : 'max'})
# We can use the aggregate function .agg() to select the aggregation we want to do for each column. We are using a Python dictionary as a parameter of the .agg() function, where the keys of the dictionary are column names, and the values are functions we want to apply. Furthermore, we can even do two aggregations on one column:

# df.groupby(['neighborhood']).agg({'price' : ['mean','max']})

import pandas as pd
df = pd.read_csv('dubai_properties_data.csv')
df.head()

# Challenge
# Using the functions described above, which neighborhood has the biggest difference between maximum and minimum property price?

df.groupby(['neighborhood']).agg({'price' : ['max','min']})

import numpy as np
#sorting return the first row
df.groupby('neighborhood')['price'].agg(np.ptp).sort_values(ascending=False).head(1)

#same above without using numpy
df.groupby('neighborhood')['price'].agg(lambda x: x.max() - x.min()).sort_values(ascending=False).head(1)

%%timeit
#assign adds a collumn called price_diff to the dataframe
df.assign(price_diff = lambda x: x.price.max() - x.price.min())

#sort by price_diff
# df.sort_values(by='price_diff', ascending=False).head(1)
df.assign(price_diff = lambda x: x.price.max() - x.price.min()).sort_values(by='price_diff', ascending=False).head(1)

# get the row of max value
df.loc[df['Score'].idxmax()]


# get the row of minimum value
df.loc[df['Score'].idxmin()]