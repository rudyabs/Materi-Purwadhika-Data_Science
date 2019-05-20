import matplotlib.pyplot as plt
import matplotlib.image as mimg
import numpy as np
from PIL import Image

# membuka gambar
'''
gambar = mimg.imread('052-smiley.png')
gambar = gambar[:,:,0]
print(gambar)
print(len(gambar))
print(len(gambar[0]))

gbrplot = plt.imshow(gambar, cmap='hot')
plt.axis('off')
'''

# membuka gambar dengan pillow
# black/white = 'L' / 'RGBA' / 'CMYK'
gambar = Image.open('052-smiley.png').convert('L')
gambar = np.array(gambar)
print(gambar)

# tampilkan gambar dgn matplotlib
'''
plt.imshow(gambar, cmap='gray')
plt.show()
'''

# tampil gambar dengan pillow
gbr = Image.fromarray(gambar, 'L')
gbr.show()