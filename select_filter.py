# We can connect to the existing SQLite database using the command below:

import sqlite3
conn = sqlite3.connect("himalayas.db")

# Now, we can use the connection conn to access the data in the database directly from pandas.

import pandas as pd
peaks = pd.read_sql('select * from peaks',conn)

# The most basic form of the SQL SELECT statement must include the SELECT and FROM keywords.

# SELECT - defines what we want to take from the source
# FROM - defines our data source (table)
pd.read_sql("""
            SELECT fname,
                lname,
                calcage,
                sex
            FROM members
            """
            ,conn)

# In addition, if we want to filter the result set of the query, we should use the WHERE keyword

pd.read_sql("""
            SELECT fname,
                lname,
                calcage,
                sex
            FROM members
            WHERE calcage >= 40
            """
            ,conn)

# We can use more than one filter:

pd.read_sql("""
            SELECT fname,
                lname,
                calcage,
                sex
            FROM members
            WHERE calcage >= 40
                AND sex = 'M'
                AND fname = 'Eric'
            """
            ,conn)
