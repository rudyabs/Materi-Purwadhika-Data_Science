'''
logistic regression

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('075-dataset.xlsx')

print(df.head())

# Logistic Regression
from sklearn.linear_model import LogisticRegression
logr = LogisticRegression(solver='lbfgs')
logr.fit(df[['umur']],df['status'])

# slope & intercept
print(logr.coef_)
print(logr.intercept_)

# prediction and score
print(logr.score(df[['umur']],df['status']))
print(logr.predict([[100]]))
print(logr.predict_proba([[24]]))