#Imported Modules
import pandas as pd
import numpy as np

full_table = pd.read_csv('full_table.csv', index_col = 0)

full_table['Active'] = full_table['Confirmed'] - full_table['Recovered'] - full_table['Deaths']

full_grouped = full_table.groupby(['Date', 'Month', 'Year', 'Country/Region', 'Province/State'])[['Confirmed', 'Deaths', 'Recovered', 'Active']].sum().reset_index()

# new cases
temp = full_grouped.groupby(['Country/Region', 'Date'])[['Confirmed', 'Deaths', 'Recovered']]
temp = temp.sum().diff().reset_index()
mask = temp['Country/Region'] != temp['Country/Region'].shift(1)
temp.loc[mask, 'Confirmed'] = np.nan
temp.loc[mask, 'Deaths'] = np.nan
temp.loc[mask, 'Recovered'] = np.nan
# renaming columns
temp.columns = ['Country/Region', 'Date', 'New cases', 'New deaths', 'New recovered']
# merging new values
full_grouped = pd.merge(full_grouped, temp, on=['Country/Region', 'Date'])
# filling na with 0
full_grouped = full_grouped.fillna(0)
# fixing data types
cols = ['New cases', 'New deaths', 'New recovered']
full_grouped[cols] = full_grouped[cols].astype('int')
#
full_grouped['New cases'] = full_grouped['New cases'].apply(lambda x: 0 if x<0 else x)


#Final Completed Output
full_grouped.to_csv('COVID-19-Completed.csv')

