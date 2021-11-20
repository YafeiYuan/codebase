import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

#随机生成验证码

#随机字母和数字
def random_char_and_num():
    # 随机生成大写字母  随机小写字母  随机生成数字并将其存在一个列表里
    random_tab=[]
    random_tab.append(chr(random.randint(65,90)))
    random_tab.append(chr(random.randint(97,122)))
    random_tab.append(str(random.randint(0,10)))

    # str= string.ascii_letters+string.digits #用字符串自带的方法也能得到想要的内容
    # printrandom.choice(str)
    print(random.choice(random_tab))
    return random.choice(random_tab)


def random_color_image():

    #RGB模式颜色 三个颜色通道  图片背景

    R=random.randint(0,135)
    G=random.randint(0, 135)
    B=random.randint(0, 135)

    return R,G,B

def random_color_text():
    # 同样RGB模式颜色 三个颜色通道

    R = random.randint(20, 255)
    G = random.randint(23, 135)
    B = random.randint(56, 188)
    return R,G,B

#创建一张新图片
image=Image.new("RGB",(200,100),random_color_image())

#创建绘图工具
image_draw=ImageDraw.Draw(image)

#选择字体
fnt=ImageFont.truetype("ygyxsziti2.0.ttf",38)

#填充像素
for i in range(image.size[0]): #长度方向上
    for j in range(image.size[1]): #宽度方向上
        image_draw.point((i,j),random_color_image())


#生成验证码
for i in range(4):
    image_draw.text((50*i+10,35),random_char_and_num(),random_color_text(),fnt)

# 模糊处理
image=image.filter(ImageFilter.BLUR)
image.show()
#还可以加干扰线 等等 大家可以思考下
