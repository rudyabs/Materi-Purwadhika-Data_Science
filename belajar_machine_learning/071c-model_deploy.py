import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('071-harga_rumah.csv')
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(df[['usia','kamar','luas']],df['harga'])

# save model with pickle - sudah terinstall standard library
# import pickle

# with open('071-model_pickle.pkl','wb') as file_saya071: 
#     pickle.dump(lm, file_saya071) # lm = nama model ML, file_saya071 variable untuk save

# save model with joblib - pip install joblib
from sklearn.externals import joblib
joblib.dump(lm,'071-model_joblib')