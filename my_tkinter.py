import tkinter
import tkinter as tk
import json
import time
import os
import random
from tkinter import *
from tkinter.filedialog import askdirectory
from qiniu import Auth, put_file, etag

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
    sw1 = win.winfo_screenwidth()
    sh1 = win.winfo_screenheight()
    ww1 = 600
    wh1 = 400
    x1 = (sw1 - ww1) / 2
    y1 = (sh1 - wh1) / 2
    window_sign_up = tk.Toplevel(win)
    window_sign_up.geometry('%dx%d+%d+%d' % (ww1, wh1, x1, y1))
    window_sign_up.title('账号设置')

    def sign_to_Mofan_Python():
        ak = new_name.get()
        sk = new_pwd.get()
        mydict = {ak: sk}
        with open('usrs_info.json', 'w') as usr_file:
            json.dump(mydict, usr_file)
            window_sign_up.destroy()

    # AK 输入框
    new_name = tk.StringVar()
    new_name.set('')
    tk.Label(window_sign_up, text='Access Key(AK)').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10, width=320)

    # SK 输入框
    new_pwd = tk.StringVar()
    new_pwd.set('')
    tk.Label(window_sign_up, text='Secret Key(SK)').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd)
    entry_usr_pwd.place(x=150, y=50, width=320)

    # Sign up按钮
    btn_comfirm_sign_up = tk.Button(window_sign_up, text='保存', command=sign_to_Mofan_Python)
    btn_comfirm_sign_up.place(x=450, y=130)


# 读取json文件获取到ak和sk的值
def aaa():
    f = open("usrs_info.json", 'r', encoding='utf-8')
    setting = json.load(f)
    access = [ak for ak in setting.keys()]
    secret = [sk for sk in setting.values()]
    access_key = str(access).replace("[", "").replace("]", "").replace("'", "")
    secret_key = str(secret).replace("[", "").replace("]", "").replace("'", "")
    return access_key, secret_key
    # 构建鉴权对象
    # q = Auth(access_key, secret_key)

# 创建登录按钮
b1 = Button(win, text='账号设置', font=None, width=8, height=1, command=login)
b1.grid(row=0, column=1, sticky=W, padx=830, pady=5)


# 选择文件路径
def selectPath():
    global path_
    path_ = askdirectory()
    # print(path_)
    # return path_
    path.set(path_)
path = StringVar()
Label(win, text="本地目录:").grid(row=1, column=1, sticky=W, padx=18, pady=20)
bendi_path = Entry(win, textvariable=path)
bendi_path.place(x=90, y=62, width=420)
Button(win, text="路径选择", command=selectPath).grid(row=1, column=1)
# print(path)

# 上传七牛云服务器路径
def getname():
    bucketname = bucketName.get()
    return bucketname

Label(win, text='目标空间:').grid(row=2, column=1, sticky=W, padx=18, pady=0)
bucketName = Entry(win)
bucketName.place(x=90, y=104, width=420)
# print(bucketName)
# Button(win, text="确定", command=getname).grid(row=2, column=1)

# 一键命名按钮，检查命名是否重名，如果重名，更改文件名称
# b2 = Button(win, text='一键命名', width=15, height=1)
# b2.grid(row=3, column=1, sticky=W, padx=50, pady=70)

# 检查文件名称是否存在七牛云，如果存在，将文件名重命名,是否执行检查，打钩选择框
# b4 = Button(win, text='本地与服务器查重处理', width=25, height=1)
# b4.grid(row=3, column=1, sticky=W, padx=450, pady=70)


# 生成新的文件名称
def generate_random_str(randomlength=10):
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str


def upload():
    sw2 = win.winfo_screenwidth()
    sh2 = win.winfo_screenheight()
    ww2 = 600
    wh2 = 400
    x2 = (sw2 - ww2) / 2
    y2 = (sh2 - wh2) / 2
    progre = tk.Toplevel(win)
    progre.geometry('%dx%d+%d+%d' % (ww2, wh2, x2, y2))
    progre.title('上传进度')

    tk.Label(progre, text='上传进度:', ).place(x=50, y=60)
    canvas = tk.Canvas(progre, width=465, height=22, bg="white")
    canvas.place(x=110, y=60)

    # 显示下载进度
    def progress():
        # 填充进度条
        fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
        x = 500  # 未知变量，可更改
        n = 465 / x  # 465是矩形填充满的次数
        for i in range(x):
            n = n + 465 / x
            canvas.coords(fill_line, (0, 0, n, 60))
            progre.update()
            time.sleep(0.02)  # 控制进度条流动的速度
        progre.destroy()  # 关闭窗口
    btn_download = tk.Button(progre, text='开始', command=progress)
    btn_download.place(x=550, y=105)

    # 构建鉴权对象
    access_key = aaa()[0]
    secret_key = aaa()[1]
    q = Auth(access_key, secret_key)
    # 要上传的空间
    bucket_name = getname()

    # 要上传文件的本地路径列表
    file_path_list = []
    filelist = os.listdir(path_)
    for file in filelist:
        file_path_list.append(path_ + "/" + file)

    # 生成的新的文件名称的列表
    keylist = []
    num = len(file_path_list)
    for k in range(num):
        ke = generate_random_str() + '.mp4'
        keylist.append(ke)

    mydict = dict(zip(file_path_list, keylist))

    for file_path, key in mydict.items():
        # 生成上传 Token，可以指定过期时间等
        token = q.upload_token(bucket_name, key, 3600)
        # localfile = r'D:\公司文件\中国成语故事补录\045chirenshuomeng.mp4'
        # 写文件命名对应关系的日志
        localfile = file_path
        f, p = os.path.split(file_path)
        content = p + '  --------------------->  ' + key + u'\n'
        with open('log.txt', 'a+', encoding='utf-8') as fp:
            fp.write(content)
        ret, info = put_file(token, key, localfile)
        print(info)
        # if ret:
        assert ret['key'] == key
        assert ret['hash'] == etag(localfile)
        # else:
        #     '上传失败'

# 一键上传
b3 = Button(win, text='一键上传', width=15, height=1, command=upload)
b3.grid(row=4, column=1, sticky=W, padx=770, pady=250)

# 执行
win.mainloop()


