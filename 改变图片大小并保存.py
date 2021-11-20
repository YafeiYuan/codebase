import os
from PIL import Image


filename = os.listdir(r"C:\Users\PC\Desktop\img_noisy\img")
base_dir = r"C:\Users\PC\Desktop\img_noisy\img"
new_dir = r"C:\Users\PC\Desktop\img_noisy\img_noisy"
size_m = 256
size_n = 256
for img in filename:
    print(img)
    image = Image.open(base_dir + img)
    print(image)
    image_size = image.resize((size_m, size_n), Image.ANTIALIAS)
    image_size.save(new_dir + img)



