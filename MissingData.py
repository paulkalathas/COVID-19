#Imported Modules
import pandas as pd

full_table = pd.read_csv('full_table.csv', index_col=0)

full_table['Recovered'] = full_table['Recovered'].fillna(0)

print(full_table.isna().sum())

full_table.to_csv('full_table.csv')