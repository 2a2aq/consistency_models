import numpy as np
from PIL import Image
import os

npz_path = r'./image/samples_500x64x64x3.npz'
data = np.load(npz_path)

images = data['arr_0']

if not os.path.exists(r'./images1'):
    os.makedirs(r'./images1')
for i in range(len(images)):
    img = Image.fromarray(images[i])
    img_path = f'./images1/sample_{i+1}.png'
    img.save(img_path)