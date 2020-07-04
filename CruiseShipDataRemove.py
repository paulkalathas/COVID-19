#Imported Modules
import pandas as pd

full_table = pd.read_csv('full_table.csv', index_col = 0)

ship_rows = full_table['Province/State'].str.contains('Grand Princess') \
            | full_table['Province/State'].str.contains('Diamond Princess') \
            | full_table['Country/Region'].str.contains('Diamond Princess') \
            | full_table['Country/Region'].str.contains('MS Zaandam')

full_ship = full_table[ship_rows]

full_table = full_table[~(ship_rows)]

full_table.to_csv('full_table.csv')


