import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

kepala = ['ID','NAMA','NILAI']
df = pd.read_csv('059-test.csv', skiprows=3, header=None, names=kepala) # custom header 
# df = pd.read_csv('059-test.csv', skiprows=3, header=None) # default header = [0,1,2,...]
print(df)


