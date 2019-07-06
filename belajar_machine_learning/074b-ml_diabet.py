import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_diabetes

data_diabetes = load_diabetes()

# print(dir(data_diabetes))
# print(data_diabetes['data_filename'])
# print(data_diabetes['target_filename'])
# print(data_diabetes['feature_names'])

# print(data_diabetes['target'])
# print(len(data_diabetes['target']))

# print(data_diabetes['data'])
# print(data_diabetes['data'].shape)

df_diabet = pd.DataFrame(data_diabetes['data'],columns= data_diabetes['feature_names'])

df_diabet['y'] = data_diabetes['target']
print(df_diabet.head(3))