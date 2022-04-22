import pandas as pd

df = pd.DataFrame([["Southern", "Southern","Southern","Southern"], 
                   ["Austria", "Australia", "New Zealand", "New Zealand"], 
                   ["Sydney", "Melbourne","Auckland","Wellington"],
                   [5.312, 5.078,1.463,0.215]],
                  index=["hemisphere","country", "city","population"] 
                  ).transpose()

print (df)

# print (df.transpose()) rotate the dataframe

# convert column population to float
# after transpose the type changed to object
df["population"] = df["population"].astype(float)

grouped = df.groupby(["hemisphere","country"])["population"].mean()

print (grouped)

print(grouped.index)

# print(grouped.index.get_level_values(0))

# print(grouped.index.get_level_values(1))

print(grouped.unstack(level=1))
