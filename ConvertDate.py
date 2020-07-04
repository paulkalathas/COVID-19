#Imported Modules
import string

import pandas as pd
import datetime
import calendar


full_table = pd.read_csv('full_table.csv', index_col=0)

full_table['Date'] = pd.to_datetime(full_table['Date'])

full_table['Day'] = full_table['Date'].dt.day
full_table['Month'] = full_table['Date'].dt.month.apply(lambda x: calendar.month_name[x])
full_table['Year'] = full_table['Date'].dt.year

full_table.to_csv('full_table.csv')


