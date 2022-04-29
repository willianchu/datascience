import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('thai_tourism.csv')
df.head()

# What kind of correlation is there between Receipts (bn $) and % of GNP?
plt.figure()
plt.scatter(x = df['Receipts (bn $)'], y = df['% of GNP'])
plt.show()



#pd.DataFrame.corr()

df['Receipts (bn $)'].corr(df['% of GNP'])
# 0.9324892611735859

# Which columns have the highest correlation?
# columns
# Year	Number of tourists (m)	Receipts (bn $)	% of GNP	Income per tourist ($)

higher_correlation_columns = df.corr()
higher_correlation_columns