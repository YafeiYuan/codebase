'''
遍历文件目录：使用递归遍历结构
递归：recursion
'''

import os


def getAllDirRE(path, sp=""):
    filesList = os.listdir(path) # 得到此路径下所有文件和文件夹

    sp += "   "
    # 遍历filesList，判断是目录，还是普通文件。
    # 如果是目录，则继续查看此目录下的所有文件。
    # 如果是普通文件，则打印出来。
    for fileName in filesList:
        # 合成绝对路径
        fileAbsPath = os.path.join(path, fileName)
        if os.path.isdir(fileAbsPath): # 目录
            print(sp, "目录："+fileName)
            # 递归调用函数自身
            getAllDirRE(fileAbsPath, sp)
        else: # 普通文件
            print(sp, "普通文件："+fileName)






path = r"F:\python资料\text\记录学习python知识1\爬虫"

getAllDirRE(path)