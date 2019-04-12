8#abc={'name':['小李','老赵','小王'],'age':19'sex':'男'
#a=0
#for i in range(1,100,2):
#	a=a+i
#for i in range(2,100,2):
#	a=a-i
#print(a)
#a=['abc','Abc','sad','saf','wetr','abd','00c']
#for i in a:
#	if i.startswith('a') or i.startswith('A'):
#	 if i.endswith('c'):
#	      print(i)
#import random
#a=random.randint(1,10)
#for i in range(1,4):
# b=input('内容')
# b=int(b)   #从一到十随机选中一个数赋值给a
# if   b<a:
#  print('小了')
# elif b>a:
#  print('大了')
# elif b==a:
#  print('恭喜')
#  break
#else:
#     print('赔钱')
#!/bin/python
#abc=input('输入三个数，以逗号隔开')
#abc=abc.split(',')
#abc=[int(abc[0]),int(abc[1]),int(abc[2])]
#abc.sort()
#if abc[0]+abc[1]>abc[2]:
#    if abc[0]**2+abc[1]**2==abc[2]**2:
#        print('直角三角形')
#    elif abc[0]**2+abc[1]*2>abc[2]**2:
#        print('锐角三角形')
#    else:
#        print('钝角三角形')
#else:
#    print('不是三角形')
#!/bin/bash
#for i in range(100,1000):
#    i=int(i)
#    a=i//100
#    b=i//10%10
#    c=i%10
#    if a**3+b**3+c**3==i:
#        print(i)
#abc=0
#for i in range(1,100):
#    if i%2 ==0:
#        abc=abc-i
#    else:
#        abc=abc+i
#print(abc)
#!/bin/python
# def cba():
#  for i in range(1,10):
#    for j in range(1,i+1):
#        print('{}*{}={}'.format(i,j,i*j),end='\t')
#    print()
#for i in range(2,100):
#    for j in range(2,i+1):
#        if i%j==0:
#         break
#    if i==j:
#        s=s+i
#print(s)
#a = input('请输入一个字符串：')
#for i in range(len(a)):
#    if a[i] != a[-i-1]:
#         print('不是回文字符串')
#         break
#else:
#    print('是回文字符串)
#while True:
# b=input('输入成绩，以逗号隔开')
# if b[0]=='-':
#     break
# else:
#  a=b.split(',')
#  s=0
#  for i in a:
#   s+=float(i)
#  print('平均分为:',s / len(a))
#  for j in a:
#      if float(j) <= s / len(a):
#          print('低于平均分:',j)
#  else:
#      break
#a=input('输入一组数，以逗号隔开:')
#a=a.split(',')
#c=len(a)
#for i in range(c-1):
#    for j in range(c-1):
#        if int(a[j]) > int(a[j+1]):
#         t=a[j]
#         a[j]=a[j+1]
#         a[j+1]=t
#print(a)

#a=input('输入一串数字,以逗号隔开')
#b=input('输入一个数字')
#a=a.split(',')
#c=len(a)
#for i in range(c):
#    for j in range(i+1,c):
#        if int(a[i])+int(a[j])==int(b):
#            print(a[i],a[j])

#s=0
#a=input('输入一个数')
#a=int(a)
#for i in range(1,a+1):
#    b=b*i
#    s=s+b
#print(s)
#good=[
   # ('电脑',1999),
  #  ('鼠标',10),
 #   ('游艇',20),
#    ('美女',998)
#]
#gouwuche=[]
#a=input('输入总资产')
#a=int(a)
#while True:
#    print('商品如下')
#    for index,item, in enumerate (good):
#        print(index,item)
#    user=input('请输入商品号')

# a = [
#    ('兰博基尼',2800),
#    ('玛莎拉蒂',7700),
#    ('法拉利',8000),
#    ('布加迪威龙',10600),
#    ('奔驰',3152),
#     ('98k',12000),
# ]
# z = []#购物车
# b = input("请输入资产:")
# b = int(b)
# while True:
#         for i,j in enumerate(a):
#             print(i,j)#打印商品列表
#         x= input("选择商品>>>:")
#         if x.isdigit():#判断用户输入是否为数字
#             x = int(x)
#             if x < len(a) and x >=0:#判断用户输入的商品编号是否在下标范围之内，len()-取列表下标长度
#                 p = a[x]#通过下标获取商品价格
#                 if p[1] <= b:#买的起
#                     z.append(p)#将该商品加到购物车
#                     b-= p[1]#扣钱
#                     print("添加成功,按exit结算")
#                 else:#买不起
#                     print("余额不足,添加失败，按exit结算")
#             else:#输入编号不存在
#                 print("商品不存在")
#         elif x == 'exit':
#             print("z")#打印商品清单
#             for p in z:
#                 print(p)
#             print("你的资产余额。。。",b)
#             exit()
#         else:
#             print("错误输入")
#
# # a=['电脑','手机','计算机','mp4']
# # for i,j in enumerate(a):
#     print(i+1,j)
# while True:
#     b= int(input('请输入商品号'))
#     if b=='exit':
#         break
#     else:
#       print(a[b-1])
# z=[]
# s=input('请输入总资产')
# a=[['电脑',1999],['手机',2000],['计算机',3000],['电视机',2500],['玩具枪',68],['洗衣机',2500]]
# for i,j in enumerate(a):
#     print(i,j)
# while True:
#     b=int(input('请输入购买商品号'))
#     z.append(a[b])
#     print('添加成功')
#     c=input('输入8结束购物，输入回车继续购物')
#     sum=0
#     for i in z:
#
#     if c=='8':
#      break
# print(z)



# a=input('输入一串字符')
# a=a.split(',')
# b=[]
# for i in range(len(a)):
#     if a[i] not in b:
#         b.append(a[i])
# print(b)


# a=[3,5,7,6,6,9,9]
# b=a.copy()
# b.sort()
# b=list(set(b))
# c = a.count(b[-1])
# s = a.count(b[-2])
# print('{},'.format(b[-1])*c)
# print('{},'.format(b[-2])*s)

#
# for i in range(2,1000):
#     s=0
#     for j in range(1,i):
#         if i % j == 0:
#             s=s+j
#     if i==s:
#         print(s)

# try:
#     a=(123)
#     print(list(a+1))
# except TypeError:
#    print('类型错误')
# except NameError:
#     print('命名错误')
# except SyntaxError:
#      print('代码逻辑错误')
# try:
#     a='123'
#     print(a+'1')
# except TypeError:
#     print('类型错误')
# else:
#     print('sys')
# finally:
#     print('你好')
#
#
# b =input('输入字符串，以逗号隔开')
# b=b.split(',')
# a = 0
# for i,m in enumerate(b[::-1]):
#     for j in range(10):
#         if m == str(j):
#          a =a+j*(10**i)
# print(a)

# a=input('输入任意四个数，以逗号隔开')
# a=a.split(',')
# b=len(a)
# z=[]
# x=[]
# for i in range(b):
#     for j in  range(b):
#         for k in range(b):
#            c=a[i]+a[j]+a[k]
#            z.append(c)
# for ii in z:
#     if ii not in x:
#         x.append(ii)
# print(x)

# a=input('输入字符串，以逗号隔开')
# a=a.split(',')
# b=a[0]
# a.pop(0)
# a.append(b)
# print(a)


# a=100
# for i in range(100):
#     for j in range(100):
#         for k in range(100):
#             if a==i+j+k:
#              if a==2*i+1*j+0.5*k:
#                 abc='公鸡{},母鸡{},小鸡{}'
#                 f=abc.format(i,j,k)
#                 print(f)
#
# b=input('输入一个数')
# b=int(b)
# a=[1,2,3,4,6,7,8,9]
# a.append(b)
# a.sort()
# print(a)
#
# a=input('输入一个数')
# a=a[::-1]
# sum=0
# for i in range(len(a)):
#     for j in range(10):
#         if str(j)==a[i]:
#             sum=sum+j*10**i
# print(sum)



# b=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# a=input('输入一个十进制的数')
# a=int(a)
# c=[]
# while True:
#     x=a%16
#     a=a//16
#     c.append(b[x])
#     if a==0:
#         break
# c.reverse()
# print(c)
# m=c[0]
# for i in range(1,len(c)):
#     m=m+c[i]
# print(m)

# f=open(r'C:\Users\Wmf\Desktop\gouwuche.png','rb')
# a=f.read()
# f.close()
# print(a)
# c=open(r'C:\Users\Wmf\Desktop\aaa.png','wb')
# c.write(a)
# c.close()

# f=open('a.txt','w',encoding='utf-8')


# def xy():
#  f=open('ab.txt','r',encoding='utf-8')
#  a=f.readlines()
#  f.close()
#  print(len(a))
# xy()

# f=open('a.txt','w',encoding='utf-8')
# for i in range(1,10):
#     for j in range(1,i+1):
#         f.write('{}*{}={}\t'.format(i,j,i*j))
#     f.write('\n')

#
# a=input('输入成绩，以逗号隔开')
# a=a.split(',')
# b=len(a)
# s=0
# for i in range(b):
#     s=s+int(a[i])
#     x=x/int(b)
#     print(int(x))

# f=open('a.txt','r',encoding='utf-8')
# a=f.readlines()
# for i in a[10::]:
#     print(i)
#     if i==a[15]:
#         break
#
# f=open('a.txt','r',encoding='utf-8')
# a=f.readlines()
# f.close
# b=len(a)
# for i in range(b):
#     if 'abc'in a[i]:
#         a[i]=str(a[i])
#         a[i]=a[i].replace('\n','')
#         print(a[i])

# def abc(x=2,y=100):
#     s=0
#     for i in range(x,y+1):
#         for j in range(2,i+1):
#             if i % j ==0:
#                 break
#         if i==j:
#             s=s+i
#     print(s)
#
# abc(x=2,y=1000)



# def c(a,b=10,*abc):
#     print(a)
#     print(b)
#     print(abc)
# c(1314,150,110,120,135)


# def abc(x,y,z):
#     if y=='+':
#         s=x+z
#         print(s)
#     elif y=='-':
#         c=x-z
#         print(c)
#     elif y=='*':
#         d=x*z
#         print(d)
#     elif y=='/':
#         q=x/z
#         print(q)
# abc(1,'+',1)




# sum=lambda  x,y:print(x+y)
# sum(10,100)



# a=[i for i in range(1,10)]
# print(a)

# f=open('a.txt','r',encoding='utf-8')
# a=f.readlines()
# f.close()
# b=len(a)
# for i in a:
#     if i=='\n':
#         b=b-1
# print(b)


# f=open('a.txt','r',encoding='utf-8')
# a=f.readlines()
# f.close()
# b=len(a)
# for i in a:
#     if i=='\n'or'#'in i:
#           b=b-1
# print(b)

# a=[1,2,3,4,5,6,6]
# b=a.copy()
# b=list(set(b))
# b.sort()
# for i in a:
#     if i==b[-1] or i==b[-2]:
#         print(i)

#
# def abc():
#  a=[1,2,4,6,7,6,9]
#  b=len(a)
#  c=[]
#  for i in a:
#   if a[i] not  in c:
#     c.append(a[i])
#  for j in range(len(c)):
#     for k in range(len(c)):
#         if c[j]<c[k]:
#             c[k],c[j]=c[j],c[k]
#  print(c)
# abc()

# import xlwt
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('学生表')
# c=open('a.txt','r',encoding='utf-8')
# x=c.readlines()
# for i,j in enumerate(x):
#     j=j.replace('\n','').split(',')
#     for k in range(len(j)):
#      sheet.write(i,k,j[k])
# f.save('软件测试4.xls')


# import xlrd
# f=xlrd.open_workbook('软件测试4.xls')
# print(f.nsheets)
# sheet=f.sheets()[0]
# new_sheet=f.sheet_by_name('学生表')
# print(sheet.col_values(0))
# print(sheet.cell(1,0).value)

# import  xlrd
# from xlutils.copy import copy
# f=xlrd.open_workbook('软件测试2.xls')
# abc=copy(f)
# sheet=abc.get_sheet(0)
# sheet.write(6,6,'爱他鲁嘎')
# abc.save('软件测试4.xls')

# import xlwt
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('学生表')
# c=open('a.txt','r',encoding='utf-8')
# d=opeadlines()
# ii=h+x
# mm=ii+u
# print(ii)
# for i,j in enumerate(mm):
#     j=j.replace('\n','').split(',')
#     for k in range(len(j)):
#      sheet.write(i,k,j[k])
# f.save('软件测试4.xls')en('ab.txt','r',encoding='utf-8')
# m=open('c.txt','r',encoding='utf-8')
# h=d.readlines()
# x=c.readlines()
# u=m.r

# import xlrd
# f=xlrd.open_workbook('软件测试4.xls')
# sheet=f.sheets()[0] #根据标签页的名称获取想要操作的标签页
# with open('a.txt','w',encoding='utf-8') as f:
#  for i in range(sheet.nrows):
#     j=','.join(sheet.row_values(i))
#     if j[-1]==',':
#         j=j.split(',')
#         j.pop(-1)
#         j=','.join(j)
#         f.write(j+'\n')
#     elif i ==(sheet.nrows-1):
#         f.write(j)
#     else:
#         f.write(j+'\n')


# import os
# a=os.listdir(r'd:')
# print(a)


# os.rename('软件测试.xls','软件测试1.xls')
# for i in os.listdir():
#     if os.path.splitext(i)[1]=='.xls':
#         print(i)


# a=[i for i in os.listdir()if os.path.splitext(i)[1]=='.xls']
# print(a)
# for i in range(1,10):
#  os.rmdir('user{}'.format(i))




# import re
# a='abscfdrfg'
# b=re.compile('a(.*?)f',re.S)
# c=b.findall(a)
# print(c)

# import xlrd
# f=xlrd.open_workbook('软件测试1.xls')
# sheet=f.sheets()[0]
# shuju=[]
# for i in range(sheet.nrows):
#     i = sheet.row_values(i)
#     shuju.append(i)
# # print(shuju)
# q=open('bb.txt','w',encoding='utf-8')
# for i in shuju:
#   for j in i:
#       if j==i[-1]:
#           q.write(j+'\n')
#       else:
#           q.write(j)






 
# with open('c.txt','w',encoding='utf-8') as f:
#     for i in shuju:
#         for j in i:
#             if j ==i[-1]:
#                 f.write(j+'\n')
#             else:
#                 f.write(j+',')



# import xlwt
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('学生表')
# c=open('a.txt','r',encoding='utf-8')
# d=open('ab.txt','r',encoding='utf-8')
# m=open('c.txt','r',encoding='utf-8')
# h=d.readlines()
# x=c.readlines()
# u=m.readlines()
# ii=h+x
# mm=ii+u
# print(ii)
# for i,j in enumerate(mm):
#     j=j.replace('\n','').split(',')
#     for k in range(len(j)):
#      sheet.write(i,k,j[k])
# f.save('软件测试5.xls')

# import re
# f=open('ab.txt','r',encoding='utf-8')
# a=f.read()
# patt= re.compile('1.[0-9]{9}')
# c=patt.findall(a)
# print(c)

# import requests
# import re
#
# class zuowen_Spider(object):
#
# 	def qingqiu(self,page):
# 		ur = 'http://www.shicimingju.com/book/xiyouji/{}.html'.format(page)
# 		# 伪装成浏览器
# 		# head = {
# 		# 	'User-Agent':'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.109Safari / 537.36'
# 		# }
#
# 		# 发送请求
# 		res = requests.get(url=ur)
# 		#  读取响应 1.text     以字符串的方式读取
# 		#          2.content  以字节的方式读取
# 		html = res.content.decode('utf-8')
# 		# 返回结果并赋值
# 		return html
#
# 	def guolv(self,abc):
# 		# 将正则表达式编译
# 		shuju = []
# 		patt = re.compile(r'<div class="chapter_content">(.*?) <div class="layui-col-md4 layui-col-sm5">',re.S)
# 		# 将编译后的条件到字符串中取查找
# 		items = patt.findall(abc)
# 		for i in items:
# 			i = i.replace('&nbsp;','').replace('<br>','').replace('<p>','').strip()
# 			shuju.append(i)
# 		return shuju
#
# 	def save(self,qwe):
# 		with open('c.txt','w',encoding='utf-8') as f:
# 			for i in qwe:
# 				f.write(i+'\n')
#
# qiu = zuowen_Spider()
# html = qiu.qingqiu(page=1)
# shuju = qiu.guolv(abc=html)
# qiu.save(shuju)

# import requests
# import re
# import xlwt
# #
# class douban_Spider(object):
#
#  def qingqiu(self,page):
# 		ur = 'https://movie.douban.com/top250?start={}&filter='.format(page)
# 		# 伪装成浏览器
# 		# head = {
# 		# 	'User-Agent':'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.109Safari / 537.36'
# 		# }
#
# 		# 发送请求
# 		res = requests.get(url=ur)
# 		#  读取响应 1.text     以字符串的方式读取
# 		#          2.content  以字节的方式读取
# 		html = res.content.decode('utf-8')
# 		# 返回结果并赋值
# 		return html
#
#  def guolv(self,abc):
#         shuju1 = []
#         patt = re.compile(r'<span class="title">(.*?)</span>', re.S)
#         items = patt.findall(abc)
#         for i in items:
#           i = i.replace('&nbsp;', '').replace('<br>', '').replace('<p>', '').strip()
#           shuju1.append(i)
#           return shuju1
#
#  def guolv2(self,abc):
#         shuju=[]
#         patt=re.compile(r'<span class="inq">(.*?)</span>',re.S)
#         items=patt.findall(abc)
#         for i in items:
#             i=i.replace('&nbsp;','').replace('<br>','').replace('<p>','').strip()
#             shuju.append(i)
#             return shuju
#
#  def save(self,qwe):
# 		with open('y.txt','a',encoding='utf-8') as f:
# 			for i in qwe:
# 				f.write(i+'\n')
# def t():
#  f=xlwt.Workbook()
#  sheet=f.add_sheet('电影')
#  k=open('y.txt','r',encoding='utf-8')
#  s=k.readlines()
#  print(s)
#  for i,j in enumerate(s):
#     j = j.replace('\n', '').split(',')
#     for k in range(len(j)):
#         sheet.write(i,k,j[k])
#  f.save('电影.xls')
#
#
# qiu = douban_Spider()
# for i in range(26):
#  html = qiu.qingqiu(page=i)
#  shuju1 = qiu.guolv(abc=html)
#  shuju = qiu.guolv2(abc=html)
#  qiu.save(shuju1)
#  qiu.save(shuju)
# t()
import requests
import re
import os

#
# a=['张凯','凤姐']
# b=[250,520]
# z=set(zip(a,b))
# print(z)


# def dy():
#      f=open('y.txt','r',encoding='utf-8')
#      a=f.readlines() class tupian():
#     a=0
#     def qingqiu(self,page):
#      ur = 'https://www.qiushibaike.com/imgrank/page/{}/'.format(page)
#      res = requests.get(url=ur)
#      #发送请求
#      html = res.content.decode('utf-8')
#      return html
#     def guolv(self,abc):
#         #过滤图片网址
#         shuju=[]
#         ab=re.compile('<div class="thumb">(.*?)</a>',re.S)
#         items=ab.findall(abc)
#         for j in items:
#             patt = re.compile(r'src="(.*?)"',re.S)
#             hhh=patt.findall(j)
#             shuju.append(hhh[0])
#         return shuju
#     def save(self,qwe):
#         #任何图片都是二进制
#         #请求图片的网址，得到图片的源码
#         for i in qwe:
#             res=requests.get('https:'+i)
#             ht=res.content #二进制
#             with open('{}.jpg'.format(self.a),'wb')as f:
#                 f.write(ht)
#             self.a+=1
#
# aa=tupian()
# for i in range(1,3):
#  aa.save(aa.guolv(aa.qingqiu(i)))
#      print(a)
#
# import pymysql
# conn=pymysql.connect(host='192.168.0.115',
#                      port=56151,
#                      user='root',
#                      password='123456',
#                      charset='utf8')

#创建游标（控制器）
# abc=conn.cursor()
# while True:
#     a=input('输入命令')
#     if a!='exit':
#         abc.execute(a)
#         print(abc.fetchall())
#     else:
#         break
# conn.close()
#执行sql语句

 # abc.execute('show databases')
 # abc.execute('use python_test;')
# abc.execute('create table biao1(name char(20),age int,sex char(10));')
# abc.execute('insert into biao1 values("xiaowang",20,"nan"),("li",21,"nv");')
# for i in range(5):
#     abc.execute('insert into biao1 values("{}",{},"{}");'.format(12,13,14))
#  abc.execute何结果都需要容器接收
# # # print(abc.fetchmany(5)) #只接收上一个sql语句的结果('select * from biao1;')
#任

# def dy():
#     f = open('y.txt', 'r', encoding='utf-8')
#     a = f.readlines()
#     return(a)
#
#
# import pymysql
#
# conn = pymysql.connect(host='192.168.0.115',
#                        port=56151,
#                        user='root',
#                        password='123456',
#                        charset='utf8')
# abc=conn.cursor()
# abc.execute('show databases')
# abc.execute('use python_test;')
# # abc.execute('create table biao2(name char(20));')
#
# for i in dy():
#  abc.execute('insert into biao2 values();')

# import json
# a={'name':123}
# #将json数据变成字典
# json_data=json.dumps(a)
# b=json_data
# c=json.loads(json_data)
# print(b)
# print(c)

# import xlrd
import pymysql
# conn=pymysql.connect(host='192.168.0.115',
#                      port=56151,
#                      user='root',
#                      passwd='123456',
#                      charset='utf8')
# abc=conn.cursor()
# # abc.execute('create database daoru;')
# abc.execute('use daoru;')
# f=xlrd.open_workbook('电影.xls')
# sheet=f.sheets()[0]
# for i in range(sheet.nrows):
#     a=sheet.row_values(i)
#     if i==0:
#         abc.execute('create table dy(电影 char(255));')
#     else:
#         abc.execute('insert into dy values("{}");'.format(a[0]))
#         conn.commit()
# abc.execute('select * from dy;')
# print(abc.fetchall())
# conn.close()

import xlwt
# import xlrd
# f=xlrd.open_workbook('电影.xls')
# k=open('aa.txt','w',encoding='utf-8')
# sheet=f.sheets()[0]
# for i in range(sheet.nrows):
#     a=(sheet.row_values(i))
#     a=''.join(a)
#     k.write('{}\n'.format(a))



import  xlrd
import  xlwt

conn=pymysql.connect(host='192.168.0.115',
                     port=56151,
                     user='root',
                     passwd='123456',
                     charset='utf8')
abc=conn.cursor()
# abc.execute('create database daoru;')
abc.execute('use daoru;')
f=xlrd.open_workbook('电影.xls')
sheet=f.sheets()[0]
for i in range(sheet.nrows):
    a=sheet.row_values(i)
    if i==0:
        abc.execute('create table dy(电影 char(255));')
    else:
        abc.execute('insert into dy values("{}");'.format(a[0]))
        conn.commit()
abc.execute('select * from dy;')
print(abc.fetchall())
conn.close()

# import xlwt
# import xlrd
# f=xlrd.open_workbook('电影.xls')
# k=open('aa.txt','w',encoding='utf-8')
# sheet=f.sheets()[0]
# for i in range(sheet.nrows):
#     a=(sheet.row_values(i))
#     a=''.join(a)
#     k.write('{}\n'.format(a))


# from time import sleep
# import threading
# def  asd():
#     for i in range(3):
#         print('打篮球')
#         sleep(2)
# def sdf():
#     for i in range(3):
#         print('制作饮料')
#         sleep(1)
# threading.Thread(target=asd).start()
# threading.Thread(target=sdf).start()

# import time
# a=time.localtime()
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# bb=time.time()
# print(bb)
# print(time.strptime('1970-01-2','%Y-%m-%d'))
# time.sleep()
# 休息
# abc=time.strptime('2019-01-2','%Y-%m-%d')
# print(time.mktime(abc))
# time.sleep(5)
# print(time.time())

# a=input('输入一个日期')
# b=[]
# for i in range(4):
#     b.append(a[i])
# b=b[::-1]
# sum=0
# for z in range(len(b)):
#     for j in range(10):
#         if str(j)==b[z]:
#             sum=sum+j*10**z
# if sum%4==0:
#     print('是闰年')
# else:
#     print('不是闰年')
# t=time.strptime(a,'%Y-%m-%d')
# print('星期{},一年中的第{}天'.format(t[6]+1,t[7]))

# import smtplib #连接邮件服务器
# import email.mime.multipart #处理邮件组成
# import email.mime.text  #处理邮件正文
# server ='smtp.163.com' #邮件服务器
# abc= '18438513345@163.com' #发件人
# res='qq1714475433@163.com'#收件人
# passwd='W794497259'#授权码  允许登陆客户端的密码
# #创建一个空的邮件
# message=email.mime.multipart.MIMEMultipart()
# message['From']=abc  #邮件的发件人
# message['To']=res #邮件的接收者
# message['Subject']='110'
# text="多管闲事多吃屁，少管闲事少拉稀"
# #对正文进行编码
# tet=email.mime.text.MIMEText(text,'plain','utf-8')
# #将正文添加到邮件中
# message.attach(tet)
# #对附件进行读取和编码
# att2=email.mime.text.MIMEText(open('a.txt','rb').read(),'base64','utf-8')
# att2["Content-Type"]='application/octet-strem'
# att2['Content-Disposition']='attachment;filename="a.txt"'
# message.attach(att2)
# #登录服务器
# smtp123=smtplib.SMTP_SSL(server,465)
# #登录服务器
# smtp123.login(abc,passwd) #发送邮件
# smtp123.sendmail(abc,res,message.as_string())
# smtp123.close()
# a=input('输入一个时间')
#
# a=int(a)
# abc=time.strptime('{}','%Y-%m-%d'.format(a))
# c=abc-86400
# print(time.mktime(c))

# a=input('输入一个日期')
# b=[]
# for i in range(len(a)):
#     b.append(a[i])
# b=b[::-1]
# sum=0
# for z in range(len(b)):
#     for j in range(10):
#         if str(j)==b[z]:
#             sum=sum+j*10**z
# print(sum)
# abc=time.strptime('2010-01-01','%Y-%m-%d')
# print(abc)
# c=int(abc)-86400
# print(time.mktime(c))
# a=input('输入一个时间')




# abc=time.strptime('20151011','%Y-%m-%d')
# print(time.mktime(abc))

# a=input()
# b=time.strptime(a,'%Y-%m-%d')
# b=time.mktime(b)5
# c=b-86400
# d=time.localtime(c)
# d=time.strftime('%Y-%m-%d',d)
# print(d)



import pymysql
import  xlrd
import  xlwt
# conn=pymysql.connect(host='192.168.0.115',
#                      port=56151,
#                      user='root',
#                      passwd='123456',
#                      charset='utf8')
# abc=conn.cursor()
# abc.execute('use test1;')
# abc.execute('show tables;')
# abc.execute('select * from chengji;')
# a=abc.fetchall()
# conn.close()
# f=xlwt.Workbook()
# sheet=f.add_sheet('excel')
# for i,j in enumerate(a):
#     for k in range(len(j)):
#      sheet.write(i,k,j[k])
# f.save('软件测试5.xls')



# import pymysql
# import  xlwt
# conn=pymysql.connect(host='192.168.0.115',
#                      port=56151,
#                      user='root',
#                      passwd='123456',
#                      charset='utf8')
# abc=conn.cursor()
# abc.execute('use test1;')
# abc.execute('show tables;')
# abc.execute('select * from chengji;')
# a=abc.fetchall()
# conn.close()
# f=open('x.txt','a',encoding='utf-8')
# for i in a:
#     f.write('{}\n'.format(i))

#连接linux socket
#采用ssh协议。连接linux，并管理
import  paramiko
# ssh123=paramiko.SSHClient()
# #第一次连接主机,known_hosts 存放的主机地址,跳过查找
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# #连接主机
# ssh123.connect(hostname='192.168.0.115',
#                port=22,
#                username='root',
#                password='123456')
#exec_command 执行命令 直接具有结果的命令
# while True:
#     a=input('输入命令')
#     if a!='exit':
#         a,b,c=ssh123.exec_command(a)
#         print(b.read().decode())
#     else:
#         break
# ssh123.close()


# a,b,c=ssh123.exec_command('halt')
#第一个变量：表示输入的命令
#第二个变量：命令执行的结果
#第三个变量：命令的报错
# print(b.read().decode())
# ssh123.close()




#建立一个传输通道
# ssh123=paramiko.Transport('192.168.0.115',22)
# #连接linux
# ssh123.connect(username='root',password='123456')
# #创建一个传输文件的对象
# sftp = paramiko.SFTPClient.from_transport(ssh123)
# #从linux到windows传文件
# #第一个参数表示的要上传的文件
# #第二个参数表示本机存放位置
# sftp.get(r'/home/test1',r'.\sh.py')
# # sftp.put('a.txt',r'/home/a.txt.py')
# ssh123.close()

#socket 自带的模块
#socket:套接字，是实现最底层的一种通信方式   接受  发送
#采用C/S架构
#通过tcp协议进行通信  socket
#server端

# import socket
#创建一个套接字，规定使用tcp协议，使用IP版本
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #绑定ip,端口号  接收的是个元组
# s.bind(('192.168.0.57',8888))
# #监听服务是否开启，数字指的是最大等待数
# s.listen(3)
# while True:
#     #接受请求 第一个变量名：连接信息  第二个变量：客户端的IP和端口号
#     conn,addr=s.accept()
#     #接收数据 1024表示一次性最大能接收1024字节数据
#     reg=conn.recv(1024)
#     msg=input('>>>')
#     conn.send(msg.encode('utf-8'))
#     print(conn)
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定主机
# s.bind(('127.0.0.100',8888))
# while True:
#     #第一个变量：客户端发送的数据
#     #第二个变量：客户端的ip和端口号
#     conn,addr=s.recvfrom(1024)
#     print(conn.decode('utf-8'))
#     #发送响应
#     s.sendto('服务器响应'.encode('utf-8'),addr)

#!/user/bin/python
#*-*encoding:utf-8-*-










