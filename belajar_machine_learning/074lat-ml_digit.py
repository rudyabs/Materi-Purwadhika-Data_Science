import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_digits

data_digit = load_digits()
tanggal_lahir = input('Masukan tanggal lahir anda:')
x = 0

for i in tanggal_lahir:
    plt.subplot(1,len(tanggal_lahir),x+1)
    plt.imshow(data_digit['images'][int(i)])
    plt.title('Ini angka = {}'.format(data_digit['target'][int(i)]))
    x = x + 1

plt.show()