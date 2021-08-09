import os
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from tqdm import tqdm

plt.figure(figsize=(5, 5))
plt.grid(True)
plt.xlabel('width')
plt.ylabel('height')
plt.title('scale analysis')

IMG_PATH = '../trainData/Images/'
IMG_LIST = os.listdir(IMG_PATH)
shape = []
w = []
h = []

n = 0
for img in tqdm(IMG_LIST):
    img = Image.open(IMG_PATH + img)
    w.append(img.size[0])
    h.append(img.size[1])
    if (img.size[0] > 2000) or (img.size[1] > 2000):
        n += 1
print(n)
shape = np.array([w, h]).transpose()
# print(shape)
plt.plot(w, h, 'o')
plt.show()
# plt.savefig('./fig.jpg', format='jpg')
