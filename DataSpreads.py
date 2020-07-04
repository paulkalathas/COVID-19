import pandas as pd

full_grouped = pd.read_csv('COVID-19-Completed.csv', parse_dates=['Date'])
countries = ['US', 'Italy', 'China', 'Spain', 'Germany', 'France', 'Iran', 'United Kingdom', 'Australia']
selected_countries = full_grouped[full_grouped['Country/Region'].isin(countries)]

print(selected_countries)