# #Example - Loading Data
# user_filter = pd.read_csv('wine.csv')
# df.head()

# #Step 1: Create filter
# user_filter = df['Alcohol'] >= 14

# #Step 2: Feed the filter to the original DataFrame and store the result in a new variable
# filtered_df = df[user_filter]

# #Step 3: Display Variable
# filtered_df

# combined
# # Step 1 and 2
# filtered_df_2 = df[df['Alcohol'] >= 14]

# How many Italian wines have a lower percentage of alcohol than 13%
# How many wines are there in class 3?

import pandas as pd
df = pd.read_csv('wine.csv')
df.head()

# italian wines
italian_filter = df['Country'] == 'Italy'

# count rows
# len() .shape .count()
# How many Italian wines have a lower percentage of alcohol than 13%
len(df[df['Alcohol'] < 13])

# How many wines are there in class 3?
len(df[df['Class'] == 3]) 

# How many wines have a level of magnesium between 90 and 100?
len(df[(df['Magnesium'] >= 90) & (df['Magnesium'] <= 100)])

df[(df['Alcohol'] >= 11) & (df['Alcohol'] <= 13)]

# How many wines have a level of magnesium higher than 90, and a percentage of alcohol lower than 13.5%?
len(df[(df['Magnesium'] > 90) & (df['Alcohol'] < 13.5)])

