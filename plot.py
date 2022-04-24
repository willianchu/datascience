import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# we load the DataFrame
df = pd.read_csv('aus_weather.csv')
df.head()

# we can call plot() method directly on the column we want to show
df["MaxTemp"].plot()
plt.show()

# Using a histogram, what is the most likely temperature at 9am (Temp9am) in Melbourne?

%matplotlib notebook

import matplotlib.pyplot as plt

df["Temp9am"].plot(kind='hist')
plt.show()

# %matplotlib notebook

# import matplotlib.pyplot as plt

# df["Temp9am"].hist(bins=25)
# plt.show()


# Using a boxplot, does it ever rain (using variable Rainfall) in Melbourne? If yes, what was the highest daily amount recorded?

%matplotlib notebook

import matplotlib.pyplot as plt

df["Rainfall"].plot(kind='box')
plt.show ()
