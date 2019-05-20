# 

import requests
import json

url = 'https://api.openweathermap.org/data/2.5/weather?q='
nama_kota = input('Masukan nama kota: ')
api_key = '&APPID=b1acdf65171ed040c18c6f0293f66e38'

data_cuaca = requests.get(url+nama_kota+api_key)

cuaca = data_cuaca.json()['weather'][0]['main']
suhu = data_cuaca.json()['main']['temp']
lembab = data_cuaca.json()['main']['humidity']

# print(data_cuaca.json())
print('Cuaca =', cuaca)
print('Suhu =', suhu-273, '*C')
print('Kelembaban =', lembab, '%')
