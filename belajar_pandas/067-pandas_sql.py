'''
membaca dataframe dari SQL menggunakan pandas
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='rudyabs',
    passwd='Kecapi48',
    database='digimon_db'
)

# mycursor = mydb.cursor()

# mycursor.execute('SELECT * FROM digimon LIMIT 5')
# hasil = mycursor.fetchall()
# print(hasil)

df = pd.read_sql('SELECT * FROM digimon', con=mydb, index_col='id')
print(df)