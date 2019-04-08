# import tkinter
# from  tkinter import ttk
#
# def go(*args):  # 处理事件，*args表示可变参数
#     print(comboxlist.get())  # 打印选中的值
#
# win = tkinter.Tk()  # 构造窗体
# comvalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
# comboxlist = ttk.Combobox(win, textvariable=comvalue)  # 初始化
# comboxlist["values"] = ("1", "2", "3", "4")
# comboxlist.current(0)  # 选择第一个
# comboxlist.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
# comboxlist.pack()
#
# win.mainloop()  # 进入消息循环


from tkinter import *
# # 初始化Tk()
# myWindow = Tk()
# # 设置标题
# myWindow.title('Python GUI Learning')
# # 创建两个按钮
# b1 = Button(myWindow, text='button1', bg="red", relief='raised', width=8, height=2)
# b1.grid(row=0, column=0, sticky=W, padx=5, pady=5)
# b2 = Button(myWindow, text='button2', font=('Helvetica 10 bold'), width=8, height=2)
# b2.grid(row=0, column=1, sticky=W, padx=5, pady=5)
# # 进入消息循环
# myWindow.mainloop()


# def printInfo():
#     # 清理entry2
#     entry2.delete(0, END)
#     # 根据输入半径计算面积
#     R = int(entry1.get())
#     S = 3.1415926 * R * R
#     entry2.insert(10, S)
#     # 清空entry2控件
#     entry1.delete(0, END)
#
# # 初始化Tk()
# myWindow = Tk()
# # 设置标题
# myWindow.title('Python GUI Learning')
#
# # 标签控件布局
# Label(myWindow, text="input").grid(row=0)
# Label(myWindow, text="output").grid(row=1)
#
# # Entry控件布局
# entry1 = Entry(myWindow)
# entry2 = Entry(myWindow)
# entry1.grid(row=0, column=1)
# entry2.grid(row=1, column=1)
#
# # Quit按钮退出；Run按钮打印计算结果
# Button(myWindow, text='Quit', command=myWindow.quit).grid(row=2, column=0, sticky=W, padx=5, pady=5)
# Button(myWindow, text='Run', command=printInfo).grid(row=2, column=1, sticky=W, padx=5, pady=5)
#
# # 进入消息循环
# myWindow.mainloop()


# from tkinter import *
# from tkinter.filedialog import askdirectory
#
# def selectPath():
#     path_ = askdirectory()
#     path.set(path_)
#
# root = Tk()
# path = StringVar()
#
# Label(root,text = "目标路径:").grid(row = 0, column = 0)
# Entry(root, textvariable = path).grid(row = 0, column = 1)
# Button(root, text = "路径选择", command = selectPath).grid(row = 0, column = 2)
#
# root.mainloop()


# from tkinter import *
# import tkinter.filedialog
#
# root = Tk()
#
# def xz():
#     filename = tkinter.filedialog.askopenfilename()
#     if filename != '':
#         lb.config(text = "您选择的文件是："+filename)
#     else:
#         lb.config(text = "您没有选择任何文件")
#
# lb = Label(root,text = '')
# lb.pack()
# btn = Button(root,text="弹出选择文件对话框",command=xz)
# btn.pack()
# root.mainloop()


# from tkinter import *
# import tkinter.filedialog
# root = Tk()
# def xz():
#     filenames = tkinter.filedialog.askopenfilenames()
#     if len(filenames) != 0:
#         string_filename = ""
#         for i in range(0, len(filenames)):
#             string_filename += str(filenames[i])+"\n"
#         lb.config(text="您选择的文件是："+string_filename)
#     else:
#         lb.config(text="您没有选择任何文件")
#
# lb = Label(root, text='')
# lb.pack()
# btn = Button(root, text="弹出选择文件对话框", command=xz)
# btn.pack()
# root.mainloop()


# import tkinter as tk
# window = tk.Tk()
# window.title('my window')
# window.geometry('800x600')
# var = tk.StringVar()
# l = tk.Label(window)
# # l.pack()
# def print_selection():
#     if var1.get() == 1:
#         l.config(text='检查')
#     else:
#         l.config(text='不检查')
# var1 = tk.IntVar()
# c1 = tk.Checkbutton(window, text='检查文件名称是否存在', variable=var1, command=print_selection)
# c1.grid()
# window.mainloop()


# from tkinter import *
# root = Tk()
# # 按扭调用的函数，
# def reg():
#     User = e_user.get()
#     Pwd = e_pwd.get()
#     len_user = len(User)
#     len_pwd = len(Pwd)
#     if User == '111' and Pwd == '222':
#         l_msg['text'] = '登陆成功'
#     else:
#         l_msg['text'] = '用户名或密码错误'
#         e_user.delete(0, len_user)
#         e_pwd.delete(0, len_pwd)
# # 第一行，用户名标签及输入框
# l_user = Label(root, text='用户名：')
# l_user.grid(row=0, sticky=W)
# e_user = Entry(root)
# e_user.grid(row=0, column=1, sticky=E)
# # 第二行，密码标签及输入框
# l_pwd = Label(root, text='密码：')
# l_pwd.grid(row=1, sticky=W)
# e_pwd = Entry(root)
# e_pwd['show'] = '*'
# e_pwd.grid(row=1, column=1, sticky=E)
# # 第三行登陆按扭，command绑定事件
# b_login = Button(root, text='登陆', command=reg)
# b_login.grid(row=2, column=1, sticky=E)
# # 登陆是否成功提示
# l_msg = Label(root, text='')
# l_msg.grid(row=3)
# root.mainloop()


# import tkinter as tk
# '''紧耦合'''
# # 弹窗
# class PopupDialog(tk.Toplevel):
#   def __init__(self, parent):
#     super().__init__()
#     self.title('设置用户信息')
#     self.parent = parent # 显式地保留父窗口
#     # 第一行（两列）
#     row1 = tk.Frame(self)
#     row1.pack(fill="x")
#     tk.Label(row1, text='姓名：', width=8).pack(side=tk.LEFT)
#     self.name = tk.StringVar()
#     tk.Entry(row1, textvariable=self.name, width=20).pack(side=tk.LEFT)
#     # 第二行
#     row2 = tk.Frame(self)
#     row2.pack(fill="x", ipadx=1, ipady=1)
#     tk.Label(row2, text='年龄：', width=8).pack(side=tk.LEFT)
#     self.age = tk.IntVar()
#     tk.Entry(row2, textvariable=self.age, width=20).pack(side=tk.LEFT)
#     # 第三行
#     row3 = tk.Frame(self)
#     row3.pack(fill="x")
#     tk.Button(row3, text="取消", command=self.cancel).pack(side=tk.RIGHT)
#     tk.Button(row3, text="确定", command=self.ok).pack(side=tk.RIGHT)
#   def ok(self):
#     # 显式地更改父窗口参数
#     self.parent.name = self.name.get()
#     self.parent.age = self.age.get()
#     # 显式地更新父窗口界面
#     self.parent.l1.config(text=self.parent.name)
#     self.parent.l2.config(text=self.parent.age)
#     self.destroy() # 销毁窗口
#   def cancel(self):
#     self.destroy()
# # 主窗
# class MyApp(tk.Tk):
#   def __init__(self):
#     super().__init__()
#     # self.pack() # 若继承 tk.Frame，此句必须有！！！
#     self.title('用户信息')
#     # 程序参数
#     self.name = ''
#     self.age = ''
#     # 程序界面
#     self.setupUI()
#   def setupUI(self):
#     # 第一行（两列）
#     row1 = tk.Frame(self)
#     row1.pack(fill="x")
#     tk.Label(row1, text='姓名：', width=8).pack(side=tk.LEFT)
#     self.l1 = tk.Label(row1, text=self.name, width=20)
#     self.l1.pack(side=tk.LEFT)
#     # 第二行
#     row2 = tk.Frame(self)
#     row2.pack(fill="x")
#     tk.Label(row2, text='年龄：', width=8).pack(side=tk.LEFT)
#     self.l2 = tk.Label(row2, text=self.age, width=20)
#     self.l2.pack(side=tk.LEFT)
#     # 第三行
#     row3 = tk.Frame(self)
#     row3.pack(fill="x")
#     tk.Button(row3, text="设置", command=self.setup_config).pack(side=tk.RIGHT)
#   # 设置参数
#   def setup_config(self):
#     pw = PopupDialog(self)
#     self.wait_window(pw) # 这一句很重要！！！
#     return
# if __name__ == '__main__':
#   app = MyApp()
#   app.mainloop()


# # coding=gbk
# # 重点：  1. tkinter.Tk() 创建窗口
# #           tkinter.Toplevel(a) 创建窗口，在窗口a的顶端
# #        2. 以字典的形式保存账户和密码
# #               exist_usr_info[nn] = np
# #               usrs_info = {'admin': 'admin'}
# #        3. with语句可以自动关闭资源
# #               with open('usrs_info.pickle', 'wb') as usr_file:
# #                 pickle.dump(exist_usr_info, usr_file)
#
# # 图片下载：https://github.com/MorvanZhou/tutorials/tree/master/tkinterTUT/tk15_login_example
# import tkinter as tk
# from tkinter import messagebox  # import this to fix messagebox error
# import pickle
#
# window = tk.Tk()
# window.title('Welcome to Mofan Python')
# window.geometry('450x300')
#
# # welcome image
# canvas = tk.Canvas(window, height=200, width=500)
# # image_file = tk.PhotoImage(file='welcome.gif')
# # image = canvas.create_image(0,0, anchor='nw', image=image_file)
# image = canvas.create_image(0,0, anchor='nw')
# canvas.pack(side='top')
#
# # User name标签和输入框
# # Password标签和输入框
# tk.Label(window, text='User name: ').place(x=50, y= 150)
# tk.Label(window, text='Password: ').place(x=50, y= 190)
# var_usr_name = tk.StringVar()
# var_usr_name.set('example@python.com')
# entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
# entry_usr_name.place(x=160, y=150)
# var_usr_pwd = tk.StringVar()
# entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
# entry_usr_pwd.place(x=160, y=190)
#
# def usr_login():
#     usr_name = var_usr_name.get()
#     usr_pwd = var_usr_pwd.get()
#     try:
#         with open('usrs_info.pickle', 'rb') as usr_file:# with语句可以自动关闭资源
#             usrs_info = pickle.load(usr_file)
#     except FileNotFoundError:
#         with open('usrs_info.pickle', 'wb') as usr_file:
#             usrs_info = {'admin': 'admin'} # 以字典的形式保存账户和密码
#             pickle.dump(usrs_info, usr_file)
#     if usr_name in usrs_info:
#         if usr_pwd == usrs_info[usr_name]:
#             tk.messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
#         else:
#             tk.messagebox.showerror(message='Error, your password is wrong, try again.')
#     else:
#         is_sign_up = tk.messagebox.askyesno('Welcome',
#                                'You have not signed up yet. Sign up today?')
#         if is_sign_up:
#             usr_sign_up()
#
# # 第一个窗口的Sign up按钮绑定的命令
# def usr_sign_up():
#     # 第二个窗口的Sign up按钮绑定的命令
#     def sign_to_Mofan_Python():
#         np = new_pwd.get()
#         npf = new_pwd_confirm.get()
#         nn = new_name.get()
#         with open('usrs_info.pickle', 'rb') as usr_file:
#             exist_usr_info = pickle.load(usr_file)
#         if np != npf:
#             tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
#         elif nn in exist_usr_info:
#             tk.messagebox.showerror('Error', 'The user has already signed up!')
#         else:
#             # 以字典的形式保存账户和密码
#             exist_usr_info[nn] = np
#             # with语句可以自动关闭资源
#             with open('usrs_info.pickle', 'wb') as usr_file:
#                 pickle.dump(exist_usr_info, usr_file)
#             tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
#             window_sign_up.destroy()
#     # tkinter.Tk() 创建窗口
#     # tkinter.Toplevel(a) 创建窗口，在窗口a的顶端
#     window_sign_up = tk.Toplevel(window)
#     window_sign_up.geometry('350x200')
#     window_sign_up.title('Sign up window')
#
#     # User name标签输入框
#     new_name = tk.StringVar()
#     new_name.set('example@python.com')
#     tk.Label(window_sign_up, text='User name: ').place(x=10, y= 10)
#     entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
#     entry_new_name.place(x=150, y=10)
#
#     # Password标签输入框
#     new_pwd = tk.StringVar()
#     tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
#     entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
#     entry_usr_pwd.place(x=150, y=50)
#
#     # Confirm password标签输入框
#     new_pwd_confirm = tk.StringVar()
#     tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y= 90)
#     entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
#     entry_usr_pwd_confirm.place(x=150, y=90)
#
#     # Sign up按钮
#     btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Mofan_Python)
#     btn_comfirm_sign_up.place(x=150, y=130)
#
# # login and sign up button
# btn_login = tk.Button(window, text='Login', command=usr_login)
# btn_login.place(x=170, y=230)
# btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
# btn_sign_up.place(x=270, y=230)
#
# window.mainloop()
