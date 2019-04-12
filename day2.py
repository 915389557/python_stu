#!/usr/bin/python 
#-*- coding:utf-8-*- 
#user:吴鸣非

# def abc(x,y,z):
#     s = x + z
#     return (s)
#
# elif y == '-':
# c = x - z
# return (c)
# elif y == '*':
# d = x * z
# return (d)
# elif y == '/':
# q = x / z
# return (q)
# if __name__ == '__main__':
#     print('hello')
# print(abc(10, '*', 10))
# if y=='+':


# import  paramiko
# ssh123=paramiko.SSHClient()
# #第一次连接主机,known_hosts 存放的主机地址,跳过查找
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# #连接主机
# ssh123.connect(hostname='192.168.0.115',
#                port=22,
#                username='root',
#                password='123456')
# #exec_command 执行命令 直接具有结果的命令
# while True:
#     a=input('输入命令')
#     if a!='exit':
#         a,b,c=ssh123.exec_command(a)
#         print(b.read().decode())
#     else:
#         break
# ssh123.close()

#client 客户端
import socket
# sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #连接服务器
# sock.connect(('192.168.0.57',8888))
# reg=input('>>>')
# sock.send(reg.encode('utf-8'))
# #接收数据
# # pass
# #断开连接
# msg=sock.recv(1024)
# print(msg.decode('utf-8'))
# sock.close()
# sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #直接发送请求
# host=('127.0.0.100',8888)
# while True:
#     a=input('输入内容')
#     if a!=exit:
#      sock.sendto(a.encode('utf-8'),host)
# #接收数据
#      a=sock.recv(1024)
#      print(a.decode('utf-8'))
#     else:
#         break
# sock.close



from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk

def love():
    #创建一个顶级窗口，依赖原始窗口存在
    love=Tk()
    love.title('大幂幂')
    love.mainloop()
def nolove():
    nolove=Tk()
    nolove.title('小颖颖')
    nolove.mainloop()

def closewindow():
    #设置提示信息
     messagebox.showinfo(title='别走啊',message='再玩一会啊')
    #关闭窗口
     window.destroy()
     return
window=Tk()
#命名窗口的标题
window.title('0701')
#设置窗口的大小
window.geometry('800x600')
#设置窗口位置
#window.geometry('+10+10')
#当用户关闭窗口时触发
window.protocol('WM_DELETE_WINDOW',closewindow)
#添加文本标签
label=Label(window,text='sys',font=("微软雅黑",20))
#显示标签
label.grid()
#添加图片控件
# imag=PhotoImage(file='11(1).png')
# image=Label(window,image=imag)
# image.grid(row=1,columnspan=1)
photo=Image.open('2345_image_file_copy_1.jpg')
phot=ImageTk.PhotoImage(photo)
pho=Label(window,image=phot)
#添加一个按钮
botten=Button(window,text='杨幂',width=10,height=3,command=love)
botten.grid(row=2,column=0,sticky=W)
pho.grid(row=2,columnspan=2)
botten1=Button(window,text='赵丽颖',width=10,height=3,command=nolove)
botten1.grid(row=2,column=1,sticky=W)
pho.grid(row=2,columnspan=2)
#显示窗口
window.mainloop()






