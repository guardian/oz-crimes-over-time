
import pandas as pd 
import os

data_path = os.path.dirname(__file__) + "/data/"

# https://dataverse.ada.edu.au/dataverse/australian_historical_criminal_justice_data?q=&types=dataverses%3Adatasets&sort=dateSort&order=desc&page=3

one = f'{data_path}Prisoners_discharged_from_Victorian_prisons_1864-1869_.csv'
two = f'{data_path}Prisoners_discharged_from_Victorian_prisons_1870-1879.csv'
three = f'{data_path}Prisoners_discharged_from_Victorian_prisons_1880-1889.csv'
four = f'{data_path}Prisoners_discharged_from_Victorian_prisons_1890-1899.csv'

frames = [one, two, three, four]
frames = pd.concat([pd.read_csv(x) for x in frames])
print(frames)

frames = frames[['offence',]]

one = pd.read_csv(one, parse_dates=['trial_date'])
one = one[['offence', 'trial_date']]
print(one.columns)

two = pd.read_csv(two, parse_dates=['trial_date'])
two = two[['offence', 'trial_date']]
print(two.columns)

three = pd.read_csv(three, parse_dates=['trial_date'])
three = three[['offence', 'trial_date']]
print(three.columns)

four = pd.read_csv(four, parse_dates=['trial_date'])
four = four[['offence', 'trial_date']]
print(four.columns)

frames = [one, two, three, four]

concated = pd.concat(frames)

concated = concated.loc[concated['trial_date'] < "1900-01-01"]

concated['Year'] = pd.DatetimeIndex(concated['trial_date']).year
concated = concated.sort_values(by="Year", ascending=True)

print(concated)
# print(one['offence'].unique())

