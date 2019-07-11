'''
recommender system
- ranking: popularity based - paling banyak dibeli, banyak review, 
-
-
'''
import numpy as np
import pandas as pd

# Popularity Based
produk = [
    {'nama':'Tamiya','rating':5},
    {'nama':'Drone','rating':4},
    {'nama':'RC Car','rating':5},
    {'nama':'Action Figure','rating':3},
    {'nama':'Banya','rating':2},
    {'nama':'Guling','rating':5}
]

df = pd.DataFrame(produk)
# print(df)

rekomendasi_produk = df[df['rating']==df['rating']]
# print(rekomendasi_produk)

# Content Based Filtering
# cosinus similarity

data_buku = [
    'Buku Komik Sejarah',
    'Buku Komik Politik',
    'Buku Hobi Kuliner',
    'Buku Kuliner Hobi',
    'Sejarah Komik Buku',
]
from sklearn.feature_extraction.text import CountVectorizer

CV = CountVectorizer()

transformer = CV.fit_transform(data_buku)
# print(transformer.toarray())

from sklearn.metrics.pairwise import cosine_similarity

cos_similarity = cosine_similarity(transformer)

print('cosine_similarity :')
print(cos_similarity)

my_fav = 0

# print(cos_similarity[0])
# print(list(enumerate(cos_similarity[0])))

print(sorted(list(enumerate(cos_similarity[my_fav])),key=lambda x:x[1],reverse=True))