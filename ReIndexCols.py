import pandas as pd

full_table = pd.read_csv('full_table.csv', index_col=0)

full_table = full_table[['Province/State', 'Country/Region', 'Lat', 'Long', 'Date', 'Day', 'Month', 'Year', 'Confirmed', 'Deaths', 'Recovered']]

full_table.to_csv('full_table.csv')