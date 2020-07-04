#Imported Modules
import pandas as pd

# Read CSV Files
confirmed_df = pd.read_csv('time_series_covid19_confirmed_global.csv')
deaths_df = pd.read_csv('time_series_covid19_deaths_global.csv')
recovered_df = pd.read_csv('time_series_covid19_recovered_global.csv')

#Review first 10 rows of dataframes
print(confirmed_df.head(10))
print(deaths_df.head(10))
print(recovered_df.head(10))

#Review Columns to ensure column count for all dataframes are the same
print(confirmed_df.columns)
print(deaths_df.columns)
print(recovered_df.columns)




