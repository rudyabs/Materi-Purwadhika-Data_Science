'''
pip install sqlalchemy
pip install pymysql
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlalchemy

mydb = sqlalchemy.create_engine(
    # namaDBsys://user:pass@host:port/namaDatabase
    'mysql+pymysql://rudyabs:Kecapi48@localhost:3306/digimon_db'
)

df = pd.read_sql('SELECT * FROM digimon', mydb)
print(df)