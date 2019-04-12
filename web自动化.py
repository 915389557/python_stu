#!/usr/bin/python 
#-*- coding:utf-8-*- 
#user:吴鸣非

from selenium import webdriver
from time import sleep

import selenium.webdriver.support.ui as ui
#定义使用什么浏览器
dr=webdriver.Chrome()
#打开网址
dr.get('http://www.jingdong.com')
# dr.switch_to.frame('login_frame')
sleep(2)
# dr.get('http://www.jd.com')
# sleep(2)
# dr.back()
#dr.forward()前进
# dr.s
# sleep(2)
#获取网址的标题
# print(dr.title)
#

# dr.quit()
# dr.set_window_size(400,400)#设置浏览器的大小
# dr.set_window_position(400,600) #设置浏览器的位置
# dr.maximize_window() #设置浏览器全屏
# dr.minimize_window() #设置浏览器最小化
# dr.close()关闭浏览器不断开连接
# # dr.quit()关闭浏览器断开连接
#定位  核心
#1.  id  来定位   id
# dr.find_element_by_id('kw').send_keys('老光棍')
# sleep(2)
# dr.find_element_by_id('su').click()#点击

#2.  通过class_name  定位   标签的class属性
# dr.find_element_by_class_name('s_ipt').send_keys('python')
# dr.find_element_by_class_name('bg s_btn').click()

#3. 通过name  定位    标签上的name属性

# dr.find_element_by_name('wd').send_keys('老光棍')

#4. 通过text定位  标签的文本定位
# dr.find_element_by_link_text('hao123').click()

#5.  partial_link_text定位   标签的模糊文本定位
# dr.find_element_by_partial_link_text('hao').click()

#6.  tag_name定位   标签名称定位   最不唯一的定位，通常定位一组数据
# dr.find_element_by_tag_name('input')

#7. css_selector定位  通过css定位
# dr.find_elements_by_css_selector('#kw')

#8.  xpath定位    路径定位
#  xpath   路径标记语言
#  xml    可扩展性标记语言
# dr.find_element_by_xpath('//*[@id="kw"]').send_keys('习近平')

#  id > css > xpath > name > class_name....



# dr.find_element_by_id('kw').send_keys('qq空间')
# sleep(2)
# dr.find_element_by_id('su').click()
# sleep(2)
# sleep(10)
# dr.find_element_by_xpath('').click()


# dr.find_element_by_xpath('#u').send_keys('794497259')
# dr.find_element_by_xpath('#p').send_keys('w943595525')
# dr.find_element_by_xpath('#login_button').click()

# 定位一组数据  对多个数据进行操作
# wd=dr.find_elements_by_class_name('mnav')
# for i in wd:
#  dr.get(i.get_attribute('href'))
#  sleep(2)
#  dr.back()


#层级定位  遇到复杂的元素时

# wd=dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_xpath('option')
# for i in wd:
#     i.click()
#     sleep(2)


#send_keys() 输入    click()  点击    text()  获取定位到的元素的文本    #clear() 清空定位到元素上面的数据

#处理浏览器窗口
# print(dr.current_window_handle) #获取当前窗口的字符串(句柄）
# print(dr.title)
# dr.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[1]/a').click()
# print(dr.window_handles)  #获取所有窗口句柄
# qq=dr.window_handles  #获取所有窗口句柄
# dr.switch_to.window(qq[1]) #切换句柄  参数只能是句柄
# print(dr.title)


#处理弹出框

# ww=dr.switch_to_alert
# print(ww.text)  #获取弹出框上面的内容
#
# ww.accert  #点击确定
#
# # ww.dismiss()  #点击取消
# #
# # ww.send_keys('内容')  #输入
# for i in range(1,10000,200):
#  js="var q=document.documentElement.scrollTop=10000"
#  dr.execute_script(js)
#  sleep(2)
#智能等待
# unit=ui.WebDriverWait(dr,10)
# unit.until(lambda dr:dr.find_element_by_xpath('//*[@id="key"]').is_displayed())  #直到元素出现，就不等待了
# print('hhh')

#dr.refresh()  #刷新当前网页


w=dr.find_element_by_xpath('//*[@id="key"]')
sleep(2)
a=w.get_attribute('id')
print(a)


