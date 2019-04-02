import tkinter
from tkinter import *
from tkinter.filedialog import askdirectory

# 实例化tkinter创建主窗口
win = tkinter.Tk()

# 标题
win.title('视频上传')

# 得到屏幕宽度
sw = win.winfo_screenwidth()
# 得到屏幕高度
sh = win.winfo_screenheight()

# 窗口高宽
ww = 900
wh = 600

# # 设置窗口大小
# win.geometry('600x400+300+200')
x = (sw-ww)/2
y = (sh-wh)/2
win.geometry('%dx%d+%d+%d' % (ww, wh, x, y))  # 设置屏幕大小并居中

def login():
    win1 = tkinter.Tk()
    win1.title('登录')
    sw1 = win.winfo_screenwidth()
    sh1 = win.winfo_screenheight()
    ww1 = 600
    wh1 = 400
    x1 = (sw1 - ww1) / 2
    y1 = (sh1 - wh1) / 2
    win1.geometry('%dx%d+%d+%d' % (ww1, wh1, x1, y1))

    def reg():
        User = ''
        Pwd = ''
        win1.destroy()
        return User, Pwd


    # 第一行，用户名标签及输入框
    l_user = Label(win1, text='Access Key(AK)')
    l_user.grid(row=0, sticky=W)
    e_user = Entry(win1)
    e_user.grid(row=0, column=1, sticky=E)
    # 第二行，密码标签及输入框
    l_pwd = Label(win1, text='Secret Key(SK)')
    l_pwd.grid(row=1, sticky=W)
    e_pwd = Entry(win1)
    e_pwd['show'] = '*'
    e_pwd.grid(row=1, column=1, sticky=E)
    # 第三行登陆按扭，command绑定事件
    b_login = Button(win1, text='保存', command=reg)
    b_login.grid(row=2, column=1, sticky=E)
    # 登陆是否成功提示
    l_msg = Label(win1, text='')
    l_msg.grid(row=3)
    win1.mainloop()


# 创建登录按钮
b1 = Button(win, text='账号设置', font=None, width=8, height=1, command=login)
b1.grid(row=0, column=1, sticky=W, padx=830, pady=5)

# 选择文件路径
def selectPath():
    path_ = askdirectory()
    path.set(path_)
path = StringVar()
Label(win, text="本地目录:").grid(row=1, column=1, sticky=W, padx=18, pady=20)
Entry(win, textvariable=path).grid(row=1, column=1, sticky=W, padx=78, pady=20)
Button(win, text="路径选择", command=selectPath).grid(row=1, column=1)

# 上传七牛云服务器路径
Label(win, text='目标空间:').grid(row=2, column=1, sticky=W, padx=18, pady=0)
Entry(win, textvariable=path).grid(row=2, column=1, sticky=W, padx=78, pady=0)
Button(win, text="路径选择", command=selectPath).grid(row=2, column=1)

# 一键命名按钮，检查命名是否重名，如果重名，更改文件名称
b2 = Button(win, text='一键命名', width=15, height=1)
b2.grid(row=3, column=1, sticky=W, padx=50, pady=70)

# 检查文件名称是否存在七牛云，如果存在，将文件名重命名,是否执行检查，打钩选择框
var = tkinter.StringVar()
l = tkinter.Label(win)
l.grid(row=3, column=1, sticky=W, padx=380, pady=0)
def print_selection():
    if var1.get() == 1:
        l.config(text='i love only python')
    else:
        l.config(text='i love both')
var1 = tkinter.IntVar()
c1 = tkinter.Checkbutton(win, text='检查文件名称是否存在', variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.grid(row=3, column=1, sticky=W, padx=380, pady=0)

# 一键上传
b3 = Button(win, text='一键上传', width=15, height=1, command='')
b3.grid(row=4, column=1, sticky=W, padx=770, pady=250)


# 执行
win.mainloop()


