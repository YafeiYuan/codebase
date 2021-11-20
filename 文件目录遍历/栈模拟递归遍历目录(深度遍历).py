'''
深度遍历(deepness) ：一条道走到黑
栈：stack
'''
import os


def getAllDirDE(path):
    # 列表模拟栈
    stack = []
    # 入栈
    stack.append(path)

    # 处理栈，临界条件：当栈为空的时候结束循环
    while len(stack) != 0:
        # 从栈里取出数据(路径)
        dirPath = stack.pop()
        # print(dirPath)

        # 获取目录下所有文件
        filesList = os.listdir(dirPath)
        # print(filesList)

        # 循环处理文件：如果是目录将该目录的地址入栈，如果是普通文件打印。
        for fileName in filesList:
            # 合成绝对路径
            fileAbsPath = os.path.join(dirPath, fileName)
            # 判断是否是目录
            if os.path.isdir(fileAbsPath):
                # 是目录就入栈
                print("目录：", fileName)
                stack.append(fileAbsPath)
            else:
                # 打印普通文件
                if fileName[-3: ] == "pdf":

                    print(fileName[-3: ])
                # print("普通文件："+fileName)

path = r"C:\Users\PC\Desktop\学习编程相关的书籍"
getAllDirDE(path)

