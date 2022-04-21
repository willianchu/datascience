# group by  quality average of all numerical attributes
# df.groupby(['quality']).mean()

import pandas as pd

df = pd.read_csv('dubai_properties_data.csv', index_col = 0)

df.groupby(['quality']).mean()

# count() – Number of non-null observations
# sum() – Sum of values
# mean() – Mean of values
# median() – Arithmetic median of values
# min() – Minimum
# max() – Maximum
# mode() – Mode
# std() – Standard deviation
# var() – Variance
# size() - Number of rows

# We can specify the columns we want to group by:

df.groupby(['quality'])[['price','size_in_sqft','no_of_bedrooms']].mean()

df.groupby(['view_of_landmark','view_of_water'])[['price','no_of_bedrooms']].mean()~

# Challenge
# Which neighborhood has the highest average property price and the highest size_in_sqft?
#id	neighborhood	latitude	longitude	price	size_in_sqft	price_per_sqft	no_of_bedrooms	no_of_bathrooms	quality	...	private_pool	security	shared_gym	shared_pool	shared_spa	study	vastu_compliant	view_of_landmark	view_of_water	walk_in_closet

import pandas as pd
df = pd.read_csv('dubai_properties_data.csv')
df.groupby(['neighborhood']).mean()
df.groupby(['neighborhood']).mean()['price']
df.groupby(['neighborhood']).mean()['size_in_sqft']

.size().sort_values(ascending=False))

# challenge21
df.groupby(['neighborhood']).mean()['price'].sort_values(ascending=False).head(1)

df.groupby(['neighborhood']).max()['size_in_sqft'].sort_values(ascending=False).head(1)

