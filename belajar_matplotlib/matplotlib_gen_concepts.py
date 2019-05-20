# standard import scripts
import matplotlib.pyplot as plt  
import numpy as np

# basic membuat figure
'''
fig = plt.figure() # figure kosong tanpa axes
fig.suptitle('No axes on this figure') #memberi judul
fig, ax_1st = plt.subplots(2,2)  # membuat figure dengan 2x2 grid dari Axes
'''


# membuat figure sederhana
'''
x = np.linspace(0,2,100)

plt.plot(x, x, label='linear') 
plt.plot(x,x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label') # memberi label
plt.ylabel('ylabel')

plt.title('Simple Plot') # memberi judul

plt.legend() # memberi legend

plt.show() # menampilkan figure
'''
# function untuk buat plotting
# agar tidak perlu membuat ulang plot dr awal

# contoh fungsi buat plotting
def my_plotter(ax, data1, data2, param_dict):
    '''
    Function untuk membuat graph

    Parameters
    ----------
    ax : Axes
        Axes utk menggambar

    data1 : array
        x data

    data2 : array
        y data
    
    param_dict : dict
        dictionary dari key argument(kwargs) untuk pass ke ax.plot
    
    Returns
    -------
    out : List
        List dari artists added
    '''
    out = ax.plot(data1, data2, **param_dict)
    return out

# penerapan fungsi 
data1, data2, data3, data4 = np.random.randn(4, 10) # contoh data yang digunakan

# buat 1 plot dengan 2 data
'''
fig, ax = plt.subplots(1,1) # buat figure dengan row 1 column 1
my_plotter(ax, data1, data2, {'marker':'x'}) # buat 1 plot dengan 2 data
'''

# buat 2 sub-plot dengan 4 data
'''
fig, (ax1, ax2) = plt.subplots(1,2)
my_plotter(ax1, data1, data2, {'marker': 'x'}) # subplot1
my_plotter(ax2, data3, data4, {'marker': 'o'}) # subplot2
'''

plt.show() # menampilkan figure





