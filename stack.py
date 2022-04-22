# Stack and Unstack in Pandas

import pandas as pd

# we define the dataframe
df = pd.DataFrame([[25.69, 7692000], [5.084, 268021]],
            index=['Australia', 'New  Zealand'],
            columns=['population', 'area'])

print (df)
# we apply the function stack()
stacked = df.stack()
print(stacked)

print(stacked.index)
