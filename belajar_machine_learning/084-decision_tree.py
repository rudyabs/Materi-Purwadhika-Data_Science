'''
Tutorial Decision Tree
- Decision tree - hanya melihat value tanpa membandingkan valuenya
- Bisa tanpa OHE
'''

# import standard libraries
import numpy as np
import pandas as pd

# import visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

# dataframe (csv)
df = pd.read_csv('084-job.csv')
# print(df.head()) # check dataframe

# choosing input and output variable
x = df.drop('gaji>10jt', axis=1)
y = df['gaji>10jt']
# print(x)
# print(y)

# input label encoder
from sklearn.preprocessing import LabelEncoder
label_kantor = LabelEncoder()
label_job = LabelEncoder()
label_title = LabelEncoder()

# ['Gojek' 'Tokopedia' 'Traveloka']
x['kantor'] = label_kantor.fit_transform(x['kantor'])
# ['Backend' 'Datasc' 'Frontend']
x['job'] = label_job.fit_transform(x['job'])
# ['S1' 'S2']
x['title'] = label_title.fit_transform(x['title'])

# lihat classes dari labeling
print(label_kantor.classes_)
print(label_job.classes_)
print(label_title.classes_)

'''
OHE : jika dilakukan maka 3 var => 8 var
'''
# train test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=1)

# print(X_train)
# print(y_train)

# import Decision Tree Model
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X_train,y_train)
print('Keakuratan model :',round(model.score(X_train,y_train)))

t_kerja = 0
posisi = 0 
pend = 0
print(model.predict([[t_kerja,posisi,pend]]))

if model.predict([[t_kerja,posisi,pend]]) == [1]:
    print('Gaji anda di atas 10 jt')
else:
    print('Gaji anda di bawah 10 jt')

# draw tree
export_graphviz(model.fit(X_train,y_train),out_file='085-tree.dot',feature_names=['kantor','job','title'],class_names=['gaji<10','gaji>10'])

# http://dreampuf.github.io/GraphvizOnline

