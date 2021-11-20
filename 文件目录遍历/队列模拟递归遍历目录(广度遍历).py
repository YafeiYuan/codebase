'''
广度遍历(breadth) ：先把同级处理完，在往下走
队列：queue
'''
import os
import collections

def getAllDirBR(path):
    # 创建一个队列
    queue = collections.deque()

    # 进队
    queue.append(path)

    # 处理队列，临界条件：当队列为空的时候结束循环
    while len(queue) != 0:
        # 从队列里取出数据(路径)
        dirPath = queue.popleft()
        # print(dirPath)

        # 获取目录下所有文件
        filesList = os.listdir(dirPath)
        # print(filesList)

        # 循环处理文件：如果是目录将该目录的地址进队，如果是普通文件打印。
        for fileName in filesList:
            # 合成绝对路径
            fileAbsPath = os.path.join(dirPath, fileName)
            # 判断是否是目录
            if os.path.isdir(fileAbsPath):
                # 是目录就进队
                print("目录：", fileName)
                queue.append(fileAbsPath)
            else:
                # 打印普通文件
                print("普通文件："+fileName)

path = r"F:\python资料\text\记录学习python知识1\爬虫"
getAllDirBR(path)

