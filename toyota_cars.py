import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('toyota_cars.csv')

# Category	Year	Make	Model
# 0	Pickup	2020	Toyota	Tacoma Double Cab
# 1	Coupe	2020	Toyota	GR Supra
# 2	SUV	2020	Toyota	RAV4 Hybrid
# 3	SUV	2020	Toyota	Sequoia
# 4	Sedan	2020	Toyota	Corolla

# What were the two most popular Toyota vehicle categories in 2020?

# model count
# print(df.groupby(['Make', 'Model']).size().sort_values(ascending=False))

#categories in 2020
# print(df.groupby(['Category', 'Year']).size().sort_values(ascending=False))

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('toyota_cars.csv')

df = df[df.Year == 2020]
grouped_df = df.groupby('Category').size()

plt.figure()
plt.bar(x = grouped_df.index, height = grouped_df.values)
plt.show()