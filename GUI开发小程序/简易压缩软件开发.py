# 过程化开发

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

# 创建主界面对象
root = tkinter.Tk()
# 主界面大小
root.geometry('500x500')
# 主界面标题
root.title('压缩/解压缩软件')

# 设置文件路径保存的变量【全局变量】
baocun = []


# 添加文件导入函数
def daoru():
    # 全局化声明
    global baocun
    # 弹窗 用户选择需要的文件
    paths = tkinter.filedialog.askopenfilenames(title='文件对话框')
    # 保存用户选着的文件  方便后续操作
    # 遍历路径元组，逐个添加
    for i in paths:
        baocun.append(i)
    # 显示用户选取的文件
    label['text'] = '\n'.join(baocun)


# 压缩文件函数
def yasuo():
    # 全局化声明
    global baocun
    # 设置压缩文件保存路径
    zip = tkinter.filedialog.asksaveasfilename()
    # 1.创建并且打开压缩文件
    zp = zipfile.ZipFile(zip, 'a')
    # 2.压缩
    for b in baocun:
        zp.write(b, os.path.basename(b))
    # 3.关闭压缩文件
    zp.close()
    # 4.信息提示
    tkinter.messagebox.showinfo(title='操作结果', message=f'压缩成功了{zip}')


# 解压缩操作函数
def jieya():
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


btn1 = tkinter.Button(root, text='导入文件', fg='red', command=daoru)
btn1.place(x=40, y=15, width=90, height=30)

btn2 = tkinter.Button(root, text='压缩文件', fg='green', command=yasuo)
btn2.place(x=210, y=15, width=90, height=30)

btn3 = tkinter.Button(root, text='解压文件', fg='purple', command=jieya)
btn3.place(x=370, y=15, width=90, height=30)

# 创建信息显示区域
label = tkinter.Label(root, bg='white', text='', anchor='nw', justify='left')
label.place(x=60, y=80, width=380, height=380)

# 将主界面加入消息循环
root.mainloop()
