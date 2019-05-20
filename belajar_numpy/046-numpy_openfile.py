import numpy as np

x = np.loadtxt('046-test.csv', skiprows = 1, delimiter= ",", usecols=range(22), unpack=True) # file harus berisi angka
# saat csv di col terakhir teradapat delimiter gunakan "usecols=range(<jumlah_kolom>)"
print(x)
