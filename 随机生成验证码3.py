

# 随机数字密码
import random

# 设出词库
ku_a = 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', \
       'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'

ku_A = 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', \
       'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M'



ku_ = '~', '@', '#', '%', '^', '&', '*', '(', ')', '-', '=', '+','>','<','|'




# 随机生成六位数密码
ku_0 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# 打乱序列顺序
random.shuffle(ku_0)
# 随机出来六位数
num2 = 0
# 存数据
list1 = []
while num2 < 6:
    for i in random.choice(ku_0):
        list1.append(i)
    num2 += 1
# 再次打乱
random.shuffle(list1)
# 转数字类型
list2 = []
for b in list1:
    list2.append(int(b))
# 再次打乱
random.shuffle(list2)
# 结果
print(list2)




# 随机生成验证码
str = ''
for i in range(6):
    ty = random.randrange(3)
    if ty == 0:
        # 随机生成一个大写字母
        ch = chr(random.randrange(ord('A'), ord('Z') + 1))
        str += ch
    elif ty == 1:
        # 随机生成一个小写字母
        ch = chr(random.randrange(ord('a'), ord('z') + 1))
        str += ch
    else:
        # 随机生成一个数字
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        str += ch

print(str)
