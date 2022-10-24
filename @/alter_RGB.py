from PIL import Image
import numpy as np

im = Image.open('img/colorful_cat.png').convert('RGB')

arr = np.array(im, dtype=float)

arr_R = arr.copy()
arr_G = arr.copy()
arr_B = arr.copy()
arr_D = arr.copy()

arr_R[:, :, 0] *= 0.0
arr_R[:, :, 1] *= 1.0
arr_R[:, :, 2] *= 1.0

arr_G[:, :, 0] *= 1.0
arr_G[:, :, 1] *= 0.0
arr_G[:, :, 2] *= 1.0

arr_B[:, :, 0] *= 1.0
arr_B[:, :, 1] *= 1.0
arr_B[:, :, 2] *= 0.0

arr_D[:, :, 0] *= 0.1
arr_D[:, :, 1] *= 0.1
arr_D[:, :, 2] *= 0.1

Image.fromarray(arr_R.astype(np.uint8)).save('cyan_cat.png')

Image.fromarray(arr_G.astype(np.uint8)).save('magent_cat.png')

Image.fromarray(arr_B.astype(np.uint8)).save('yellow_cat.png')

Image.fromarray(arr_D.astype(np.uint8)).save('dark_cat.png')
