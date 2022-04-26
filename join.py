import sqlite3
import pandas as pd
conn = sqlite3.connect("himalayas.db")

# exped = pd.read_sql('select * from exped',conn)
# members = pd.read_sql('select * from members',conn)
# peaks = pd.read_sql('select * from peaks',conn)

# Challenge
# Answer following questions using our database:

# How many expeditions went to the peak of Everest?
# How many people went to the peak of Everest? (One person could have gone more than once)

# pd.merge()

# pd.read_sql("
#     select E.*, --all columns from the table E -> exped
#         M.fname, --this is from the table M -> members
#         M.calcage as age
#     from exped as E
#     inner join members as M
#         on E.expid = M.expid
# ",conn)

expedition = pd.read_sql("select count(DISTINCT exped.expid) from exped inner join peaks on exped.peakid = peaks.peakid where pkname = 'Everest'",conn)
expedition
 # pd.merge(exped,peaks,on='peakid')
 # 2161

 people_on_everest = pd.read_sql("select count(DISTINCT members.fname) from members inner join exped on members.expid = exped.expid inner join peaks on exped.peakid = peaks.peakid where pkname = 'Everest'",conn)

 #21900
 
