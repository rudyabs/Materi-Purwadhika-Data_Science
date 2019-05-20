# GET API https://jsonplaceholder.typicode.com/users
# request
# ================================================================

'''
Mac
sudo apt-get install python3-pip
win
python -m pip install -U pip setuptools
python -m pip --version
py -m pip install (namaPackage)
python -m pip install (namaPackage)
'''
# =================================================================
'''
import requests
import json

url = 'https://jsonplaceholder.typicode.com/users'

data_users = requests.get(url)

# print(data_users)
# print(type(data_users.json()))
# print(data_users.json()[1])
# print(data_users.json())

hasil_json = json.dumps(data_users.json())
file_json = open('datauser.json', 'w')
file_json.write(hasil_json)
'''
# ============================================================
import requests
import json

nama_klub = input('Masukan nama klub: ')
# untuk membuat input menggunakan spasi terbaca
if nama_klub.count(' ')>=1:
    nama_klub.replace(' ', '_')
url = 'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t=' + nama_klub

players = requests.get(url)
# print(player.json())
# print(player.json()['player'])

for player in players.json()['player']:
    print(player['strPlayer'], '(', player['strNationality'], ')')

# ============================================================
