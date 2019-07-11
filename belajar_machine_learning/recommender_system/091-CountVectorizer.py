import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')
# print(df.head())

# print(df.columns.values)
# print(df.isnull().sum())
# print(df[df['Genre'].isnull()])
# print(df.iloc[659])
# print(df.iloc[14246])

# buang genre di iloc 659 dan 14246
df = df.dropna(subset=['Genre'])
# print(df.isnull().sum())

# content based filtering, feture: 'Genre'
df_game = df[['Name','Platform','Genre']]

# print(df_game.head())

from sklearn.feature_extraction.text import CountVectorizer
CV = CountVectorizer(
    # ngram_range=(1,2), # min 2 kata, max 2 kata
    tokenizer= lambda x:x.split('@')
    analyzer='word',
)

matrix_genre = CV.fit_transform(df_game['Genre'])
jumlah_genre = CV.get_feature_names()
event_genre = matrix_genre.toarray()

# print(matrix_genre)
# print(jumlah_genre)
# print(event_genre)

# cosinus similarity
from sklearn.metrics.pairwise import cosine_similarity
cos_score = cosine_similarity(matrix_genre)
# print(cos_score)

# test model
fav_game = 'Pokemon Red/Pokemon Blue'
# print(df_game[df_game['Name']=='Crash Bandicoot'])

index_fav_game = df_game[df_game['Name']==fav_game].index.values[0] # mencari index dari game favorite
# print(index_fav_game)

# list all games + cos similarity score
all_game = list(enumerate(cos_score[index_fav_game]))
# print(game_mirip)

mirip_game = sorted(all_game, key=lambda x: x[1], reverse=True)
# print(mirip_game[:5]) # 5 game paling mirip

# for i in mirip_game[:5]:
#     print(df_game.iloc[i[0]]['Name'])

# show 5 data, cos sim score > 50%
game_sama50 = []
for i in mirip_game:
    if i[1]>0.5:
        game_sama50.append(i)

# print(game_sama50)

import random
rekomendasi = random.choices(game_sama50,k=5)
# print(rekomendasi)
for i in rekomendasi:
    print('Game :',df_game.iloc[i[0]]['Name'],
    'Platform :',df_game.iloc[i[0]]['Platform'],
    'Genre :',df_game.iloc[i[0]]['Genre'] )