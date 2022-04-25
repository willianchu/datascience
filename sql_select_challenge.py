# Challenge
# Use our database to answer the following questions:

# How many peaks are higher than 8000 metres? Use the len() function to count the number of rows of the DataFrame that were returned by the pd.read_sql() function.

# How many women (sex = 'F') were part of the expeditions?

import sqlite3
import pandas as pd
conn = sqlite3.connect("himalayas.db")

peaks_above_8k = pd.read_sql('select COUNT() from peaks where heightm > 8000  ',conn)

# version2

peaks = pd.read_sql('select * from peaks where heightm > 8000  ',conn)
len(peaks)

# distinct
peaks = pd.read_sql('select count(DISTINCT expid) from members where sex = \'F\'',conn)
peaks