import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [2,3,4,5,4,6,5,7,7,8]
n = len(x)

df = pd.DataFrame({
    'x':np.array(x),
    'y':np.array(y),
    'x2':np.array(x)**2,
    'y2':np.array(y)**2,
    'xy':np.array(x)*np.array(y)
})

x_sum = df.sum(axis=0)[0]
y_sum = df.sum(axis=0)[1]
x2_sum = df.sum(axis=0)[2]
y2_sum = df.sum(axis=0)[3]
xy_sum = df.sum(axis=0)[4]

# Slope / Gradient
m = (((n*xy_sum))-(x_sum*y_sum))/(((n*x2_sum))-(x_sum**2))

# Intercept / titik potong
c = ((y_sum*x2_sum)-(x_sum*xy_sum))/((n*x2_sum)-(x_sum**2))

# y best fit line (y = mx+c)
df['ybest']=m*np.array(x)+c

print(m)
print(c)
print(df)

plt.plot(
    df['x'],df['y'],'g-',
    df['x'],df['ybest'],'r-'
)
plt.grid()

plt.tight_layout()
plt.show()