from PIL import Image
from torchvision import transforms

# 数据增强对深度神经网络的训练来说是非常重要的，尤其是在数据量较小的情况下能起到扩充数据的效果。

# 总结了pytorch中使用torchvision提供的transform模块，进行数据增强常用的7种方式，并将每种操作封装为函数，
# 共包含以下8个部分（如果觉得有用请点个赞呀！！！）：

# （1）获取PIL.Image类型图片（准备数据）
# （2）中心裁剪
# （3）随机裁剪
# （4）Resize图像
# （5）随机长宽比裁剪
# （6）随机水平翻转
# （7）随机垂直翻转
# （8）随机旋转

# 实际上上述操作是可以compose（组合）使用的，但是为了能清晰的展示每种增强方式的效果，就单独的介绍了。


# 1、获取PIL.Image类型图片（准备数据）
# pytorch提供的torchvision主要使用PIL的Image类进行处理，所以它数据增强函数大多数都是以PIL作为输入，并且以PIL作为输出。
# 因此，第一件事应该是将自己的图片读取为PIL.Image类对象：
def read_PIL(image_path):
    """ read image in specific path
    and return PIL.Image instance"""
    image = Image.open(image_path)
    return image
# 这个函数非常简单，是用PIL打开图片的常用操作。
# 后面的12种操作函数的输入都是read_PIL()返回的image对象！！！选取PIL库是因为这是python的原生库，兼容性比较强。


# 2、中心裁剪
# 中心裁剪的目的是从图片的中心开始，裁剪出其四周指定长度和宽度的图片，也就是获取原图的中心部分，核心类是transforms.CenterCrop(size)，其中size参数是表示我们希望裁剪的尺寸的大小：
def center_crop(image):
    CenterCrop = transforms.CenterCrop(size=(200, 200))
    cropped_image= CenterCrop(image)
    return cropped_image


# 3、随机裁剪
# 随机裁剪和中心裁剪是有区别的，中心裁剪需要围绕图片中心点进行，但是随机裁剪的结果来自图片的哪个部分是随机的。所使用的核心函数为transforms.RandomCrop(size)，其中size表示自己希望获得裁剪后图片的尺寸：
def random_crop(image):
    RandomCrop = transforms.RandomCrop(size=(200, 200))
    random_image = RandomCrop(image)
    return random_image


# 4、Resize图像
# 图像的resize是最为常见的操作，尤其是当手中数据尺寸和网络结构不匹配时，比如网络只有3个池化层的进行降低特征图尺寸，但是手里的数据为1024x1024时，就需要降低图像的长和宽。核心函数为Resize = transforms.Resize(size)，其中size依旧表示目标图像尺寸：
def resize(image):
    Resize = transforms.Resize(size=(100, 50))
    resized_image = Resize(image)
    return resized_image


# 5、随机长宽比裁剪
# 随机长宽比裁剪的实现借助于transforms.RandomResizedCrop类，可以看出这个功能是Resize和Crop的随机组合，这在Inception网络的训练中比较有用。
# 这个类的初始化包含3个参数（size， scale， ratio），size参数为目标图片的尺寸，其中scale参数代表输出图片占原始图片的百分比区间，ratio表示长宽比的取值区间，随机的意思就是在这两个区间中随机选取两个参数值：
def random_resized_crop(image):
    RSC = transforms.RandomResizedCrop(size=200, scale=(0.2, 0.5), ratio=(1, 5))
    rsc_image = RSC(image)
    return rsc_image

# 6、随机水平翻转
# 随机水平翻转意思是有一半的可能性翻转，也有一半的可能性不翻转。使用的是transforms.RandomHorizontalFlip()类：
def horizontal_flip(image):
    HF = transforms.RandomHorizontalFlip()
    hf_image = HF(image)
    return hf_image

# 7、随机垂直翻转
# 随机垂直翻转和上面的随机水平翻转原理相同，只不过是在垂直方向上进行，使用的类为transforms.RandomVerticalFlip()：
def vertical_flip(image):
    VF = transforms.RandomVerticalFlip()
    vf_image = VF(image)
    return vf_image

# 8、随机旋转
# 随机旋转仍然是图像像素位置变换的一种常用操作，我们可以设定自己希望旋转的角度区间，transforms.RandomRotation(degrees)中的degrees参数表示旋转角度的选择范围：
def random_rotation(image):
    RR = transforms.RandomRotation(degrees=(10, 80))
    rr_image = RR(image)
    return rr_image

# 总结：
# 实际上，数据增强的方式还有很多，上面介绍的仅仅是很小的一部分。
# 在训练模型时，是否需要使用数据增强以及使用哪些种数据增强，是需要根据经验或者实验结果来确定的。










