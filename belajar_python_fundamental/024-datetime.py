# date time
'''
import datetime

x = datetime.datetime.now()

print(type(x))
print(x)
print(x.year)           # tahun
print(x.strftime('%m')) # bulan index
print(x.strftime('%b')) # bulan nama
print(x.strftime('%a')) # hari
print(x.strftime('%d')) # tanggal
print(x.strftime('%h')) # jam 24h
print(x.strftime('%I')) # jam 12h
print(x.strftime('%M')) # menit
print(x.strftime('%S')) # detik

print(x.strftime('%c'))
'''
# ----------------------------------
from datetime import datetime # mengimport method pada datetime

'''
x ='12/04/2019'
y = '12 Apr 2019'
z = "12-04-19 21.45"
a ='Friday, 12 April 2019'
b = "Jum'at, 12 April 2019"

x_ke_date = datetime.strptime(x, "%d/%m/%Y")
y_ke_date = datetime.strptime(y, "%d %b %Y")
z_ke_date = datetime.strptime(z, '%d-%m-%y %H.%M')
a_ke_date = datetime.strptime(a, '%A, %d %B %Y')

print(x_ke_date)
print(y_ke_date)
print(z_ke_date)
print(a_ke_date.strftime('%A'))
'''

x = datetime.now()
'''
print(x.strftime('%A'))
print(type(x.strftime('%A')))
print(x.strftime('Sekarang hari %A tanggal %d-%B-%Y jam %H'))
'''

dictionaries_hari = {
    "Monday":"Senin",
    "Tuesday":"Selasa",
    "Wednesday":"Rabu",
    "Thursday":"Kamis",
    "Friday":"Jum'at",
    "Saturday":"Sabtu",
    "Sunday":"Minggu"
}


hari_ini = dictionaries_hari[x.strftime('%A')]
print(hari_ini)
