# 面向对象开发

# 制作软件界面
# 导入tkinter模块
import tkinter
# 导入tkinter子模块filedialog文件对话框
import tkinter.filedialog
# 导入tkinter子模块messagebox消息对话框
import tkinter.messagebox
# 导入压缩文件模块
import zipfile
# 导入os模块
import os


# 创建压缩软件类
class CompressedSoftware():
    # 成员属性
    # 设置文件路径保存的变量
    baocun = []

    # 成员方法
    # 初始化成员方法
    def __init__(self):
        # 创建主界面对象
        self.root = tkinter.Tk()
        # 主界面大小
        self.root.geometry('500x500')
        # 主界面标题
        self.root.title('压缩/解压缩软件')

        # 调用所有按钮方法
        self.module()

        # 将主界面加入消息循环
        self.root.mainloop()

    # 所有按钮方法
    def module(self):
        # 按钮组价(导入文件)
        self.btn1 = tkinter.Button(self.root, text='导入文件', fg='red', command=self.daoru)
        self.btn1.place(x=40, y=15, width=90, height=30)
        # 按钮组价(压缩文件)
        self.btn2 = tkinter.Button(self.root, text='压缩文件', fg='green', command=self.yasuo)
        self.btn2.place(x=210, y=15, width=90, height=30)
        # 按钮组价(解压文件)
        self.btn3 = tkinter.Button(self.root, text='解压文件', fg='purple', command=self.jieya)
        self.btn3.place(x=370, y=15, width=90, height=30)

        # 创建信息显示区域
        self.label = tkinter.Label(self.root, bg='white', anchor='nw', justify='left')
        self.label.place(x=60, y=80, width=380, height=380)

    # 添加文件导入方法
    def daoru(self):
        # 弹窗 用户选择需要的文件
        paths = tkinter.filedialog.askopenfilenames(title='文件对话框')
        # 保存用户选着的文件  方便后续操作
        # 遍历路径元组，逐个添加
        for i in paths:
            self.baocun.append(i)
        # 显示用户选取的文件
        self.label['text'] = '\n'.join(self.baocun)

    # 压缩文件方法
    def yasuo(self):
        # 设置压缩文件保存路径
        zip = tkinter.filedialog.asksaveasfilename()
        # 1.创建并且打开压缩文件
        zp = zipfile.ZipFile(zip, 'a')
        # 2.压缩
        for b in self.baocun:
            zp.write(b, os.path.basename(b))
        # 3.关闭压缩文件
        zp.close()
        # 4.信息提示
        tkinter.messagebox.showinfo(title='操作结果', message=f'压缩成功了{zip}')

    # 解压缩操作方法
    def jieya(self):
        # 1.获取压缩文件的位置
        zipath = tkinter.filedialog.askopenfilename()
        # 2.打开压缩文件
        zp = zipfile.ZipFile(zipath, 'r')
        # 3.解压
        dirpath = tkinter.filedialog.askdirectory()
        zp.extractall(dirpath)
        # 4.关闭压缩文件
        zp.close()
        # 信息提示
        tkinter.messagebox.showinfo(title='解压提示', message=f'解压成功{dirpath}')


# 实例化对象
file = CompressedSoftware()
