import os
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

plt.figure(figsize=(5, 5))
plt.grid(True)
plt.xlabel('width')
plt.ylabel('height')
plt.title('scale analysis')

IMG_PATH = './train2017/'
IMG_LIST = os.listdir(IMG_PATH)
shape = []
w = []
h = []

for img in IMG_LIST:
    img = Image.open(IMG_PATH + img)
    w.append(img.size[0])
    h.append(img.size[1])

shape = np.array([w, h]).transpose()
print(shape)
plt.plot(w, h, 'o')
plt.show()
# plt.savefig('./fig.jpg', format='jpg')
