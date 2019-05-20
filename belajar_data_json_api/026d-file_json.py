# membaca file json
# convert dict jadi json
'''
import json
x = {
    'nama': 'Andi',
    'usia': '25'
}

y = json.dumps(x)

print(x)
print(y)
print(type(y))
'''
# JSON hanya menerima file yang mirip dictionaries, list, list berisi dictionaries

# =========================================
'''
import json

x2 = ['andi','budi']
y2 = json.dumps(x2)

print(x2)
print(y2)

z1 = 'aku hanyalah string biasa'
z2 = json.dumps(z1)

print(z2)
'''
# ==============================
'''
import json

x = '{"nama": "andi"}'
x2 = '["andi", "budi", "caca"]'
y = json.loads(x)
y2 = json.loads(x2)

print(x)
print(y)
print(y['nama'])

print(x2)
print(y2)
print(y2[1])
'''
# ===========================================
# membuka dan membaca file JSON
'''
import json

with open('028ext-data.json') as dataku:
    data = json.load(dataku)

print(data)
print(type(data))
print(data[0]['nama'])
'''
# ===========================================
# membuat file json

import json
x = {
    'id':2,
    'kota':'medan'
}

x2 = json.dumps(x)
json_saya = open('contoh4.json','w')
json_saya.write(x2)