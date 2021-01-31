import pandas as pd
contents = pd.read_csv('data/CRDC2013_14content.csv')
print(contents.head())

tot_data = pd.read_csv('data/CRDC2013_14.csv')
print(tot_data.columns.tolist())

print('SCH_ENR_AM_M' in tot_data.columns.tolist())