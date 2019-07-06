import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('MSFT.csv', parse_dates=['Date'], index_col='Date')

# print(df.head())

print(df['Close'].resample('M').mean())
print(df['Close'].resample('W').mean())
print(df['Close'].resample('Q').mean())
print(df['Close'].resample('Y').mean())