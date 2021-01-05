import pandas as pd
import matplotlib.pyplot as plt


flights = pd.read_csv('flights.csv', parse_dates=['date']).loc[lambda df: df['date'] >= '2020-Apr']
users = pd.read_csv('users.csv', index_col='code').loc[lambda df: (df['gender'] == 'female') & (df['age'] > 35)]
hotels = pd.read_csv('hotels.csv', index_col='travelCode', parse_dates=['date'])

flightsUsers = pd.merge(flights, users, left_on='userCode', right_on='code')
flightsUsersHotels = pd.merge(flightsUsers, hotels, on="travelCode", suffixes=("_flight", "_hotel"))

flightsUsersHotels.to_parquet('result.parquet', engine="pyarrow", index=False)


