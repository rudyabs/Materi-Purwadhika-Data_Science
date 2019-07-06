import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_digits

data_digit = load_digits()

# print(dir(data_digit))
# print(data_digit['data'][42])
# print(data_digit['images'][42])
# print(data_digit['target'][42])

# plt.gray()
# plt.imshow(data_digit['images'][42])
# plt.show()

for i in range(10):
    plt.subplot(2,5,i+1)
    plt.imshow(data_digit['images'][i])
    plt.title('Ini angka = {}'.format(data_digit['target'][i]))

plt.show()

