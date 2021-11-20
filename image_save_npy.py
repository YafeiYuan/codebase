import cv2
import os
import numpy as np
import random
from skimage import io, transform
import pandas as pd

# 例子为：在NEU-CLS数据集上操作的。

# 数据集路径
data_dir = r"/content/drive/MyDrive/colab/multiClass/imbalance-NEU-CLS"
image_names = []
for name in os.listdir(data_dir):  # 取出文件夹中所有图片文件名字
  image_names.append(name)

random.shuffle(image_names)  # 打乱


types = ['PS', 'RS', 'CR', 'IN', 'PA', 'SC']  # 类别列表
img_data = []
img_type = []
for i in range(len(image_names)):
  img = io.imread(os.path.join(data_dir, image_names[i]))  # 读取图像为ndarray

  typ = image_names[i].split("_")[0].upper()  # 处理类别
  typ_index = types.index(typ)

  img = np.array(img)
  img_data.append(img)

  img_type.append(typ_index)

img_data_np = np.array(img_data)
img_type_np = np.array(img_type)

# 保存路径 img and type
img_data_file = os.path.join('/content/drive/MyDrive/colab/multiClass/Defects', 'img_data_new_imbalance.npy')
img_types = os.path.join('/content/drive/MyDrive/colab/multiClass/Defects', 'img_types_new_imbalance.npy')

# 保存
np.save(img_data_file, img_data_np)
np.save(img_types, img_type_np)





