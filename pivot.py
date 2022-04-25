#Load data
 
import pandas as pd
data = pd.read_csv('titanic.csv')

#Group data by 'sex' and aggregation function as sum
 
data.groupby('Sex')[['Survived']].sum()

#            Survived
# Sex 
# female       233
# male         109

#Group data by 'sex' and aggregation function as mean
 
data.groupby('Sex')[['Survived']].mean()

#           Survived
# Sex 
# female    0.742038
# male      0.188908


#Group by multidimensionality 
 
data.groupby(['Sex', 'Pclass'])['Survived'].mean()

#   S      Pclass
# female    1         0.968085
#           2         0.921053
#           3         0.500000
# male      1         0.368852
#           2         0.157407
#           3         0.135447
 
# Name: Survived, dtype: float64

#Unstacking the output
 
data.groupby(['Sex', 'Pclass'])['Survived'].mean().unstack()

# Pclass      1           2           3
# Sex         
# female  0.968085    0.921053    0.500000
# male    0.368852    0.157407    0.135447


# THE PIVOT

#pivot_table
 
data.pivot_table('Survived', 'Sex', 'Pclass')

# OR

data.pivot_table('Survived', index='Sex', columns = 'Pclass')

# Pclass      1           2          3
# Sex         
# female  0.968085    0.921053    0.500000
# male    0.368852    0.157407    0.135447

#Multi-level pivoting 
 
attribute_age = pd.cut(data['Age'],[0,18,60])  #pd.cut do the "magic"
 
data.pivot_table('Survived', ['Sex',attribute_age], 'Pclass')

# Pclass                 1                2            3
# Sex Age         
# female  (0, 18]     0.909091        1.000000      0.511628
#         (18, 60]    0.972222        0.900000      0.413793
# male    (0, 18]     0.800000        0.600000      0.215686
#         (18, 60]    0.416667        0.061728      0.136364

# Pandas Pivot Table – Aggfunc
#Using aggfunc
 
data.pivot_table(index='Sex', columns='Pclass',
 aggfunc={'Survived':sum, 'Fare':'mean'})

#                         Fare                  Survived
# Pclass      1           2           3       1   2   3
# Sex                     
# female  106.125798  21.970121   16.118810   91  70  72
# male    67.226127   19.741782   12.661633   45  17  47

# Pandas Pivot table – Margins()
#Adding margins parameter
 
data.pivot_table('Survived', index='Sex', columns='Pclass', margins=True)

# Pclass      1           2          3          All
# Sex             
# female  0.968085    0.921053    0.500000    0.742038
# male    0.368852    0.157407    0.135447    0.188908
# All     0.629630    0.472826    0.242363    0.383838

#complete syntax
# The syntax of the .pivot_table() function
import pandas as pd
pd.pivot_table(
    data=,
    values=None, 
    index=None, 
    columns=None, 
    aggfunc='mean', 
    fill_value=None, 
    margins=False, 
    dropna=True, 
    margins_name='All', 
    observed=False,
    sort=True
) 


# Loading a Sample Pandas DataFrame
#It reads the data from the CSV file and creates a Pandas DataFrame.

import pandas as pd
df = pd.read_excel('https://github.com/datagy/mediumdata/raw/master/sample_pivot.xlsx', parse_dates=['Date'])
print(df.head())

# Returns:
#         Date Region                 Type  Units  Sales
# 0 2020-07-11   East  Children's Clothing   18.0    306
# 1 2020-09-23  North  Children's Clothing   14.0    448
# 2 2020-04-02  South     Women's Clothing   17.0    425
# 3 2020-02-28   East  Children's Clothing   26.0    832
# 4 2020-03-19   West     Women's Clothing    3.0     33

