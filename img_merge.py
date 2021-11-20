import cv2
import os
import numpy as np
import random

# 例子为：在NEU-CLS数据集上操作的。
# 在合成后数据集中随机选取若干张数据作为新的数据集。

image_dir = '/content/drive/MyDrive/colab/multiClass/NEU-CLS'

# 打乱原始数据集顺序
img_path = []
for name in os.listdir(image_dir):
    img_path.append(os.path.join(image_dir, name))

random.shuffle(img_path)
new_types = ['PS', 'RS', 'Cr', 'In', 'Pa', 'Sc']


# 处理type
def str_to_defect_types(s):
    defect_types = []
    for t in new_types:
        defect_types.append(s.count(t))

    return defect_types


s = []
y = []
dataset_list = img_path  # 训练或测试需要修改 列表 训练：train_dataset; 测试：test_dataset
# size_4_1 = int(len(dataset_list)/4) # 合成图像个数new_dataset_path
# randvector = list(range(len(dataset_list)))
randvector = list(range(1000))  # 3400  2800  1440

for i in randvector:
    # img2 = dataset_list[i]
    img2 = random.choice(dataset_list)  # 路径
    imgx = img2.split("/")[-1].split("_")[0]  # 类别
    s.append(imgx)
    y.append(img2)


def to_matrix(x_y, n):
    ls_4 = []
    for i in range(0, len(x_y), n):
        ls_4.append(x_y[i: i + n])
    return ls_4


s = to_matrix(s, 4)
y = to_matrix(y, 4)

# 合成图片 4 -> 1
img_data = []
img_type = []
num = 0
for i in range(250):
    x1 = cv2.imread(y[i][0])  # ,as_gray=True)
    x2 = cv2.imread(y[i][1])  # ,as_gray=True)
    x3 = cv2.imread(y[i][2])  # ,as_gray=True)
    x4 = cv2.imread(y[i][3])  # ,as_gray=True)
    im_h1 = cv2.hconcat([x1, x2])  # 合并函数
    im_h2 = cv2.hconcat([x3, x4])
    im_f = cv2.vconcat([im_h1, im_h2])
    img_data.append(np.array(im_f))
    img_type.append(str_to_defect_types(s[i]))  # 处理type

root_path = '/content/drive/MyDrive/colab/multiClass/Defects'  # 保存至此文件夹下
# 类型转换
img_data_np = np.array(img_data)
img_type_np = np.array(img_type)

# 合成保存文件绝对路径
img_data_file = os.path.join(root_path, 'data文件名.npy')
img_types = os.path.join(root_path, 'type文件名.npy')
# 保存
np.save(img_data_file, img_data_np)
np.save(img_types, img_type_np)
