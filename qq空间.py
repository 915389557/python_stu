#!/usr/bin/python 
#-*- coding:utf-8-*- 
#user:吴鸣非
from selenium import webdriver
from time import sleep

dr=webdriver.Chrome()

#打开网址
dr.get('https://qzone.qq.com/')
dr.switch_to.frame('login_frame') #框架的id或name或者，先定位到框架
sleep(2)
#处理框架   iframe
dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="u"]').send_keys('794497259')
dr.find_element_by_xpath('//*[@id="p"]').send_keys('w943595525')
sleep(2)
dr.find_element_by_xpath('//*[@id="login_button"]').click()
print(dr.title)
# dr.switch_to.default_content()  #回到最开始的页面
# # dr.switch_to.parent_frame()  #回到父框架页面中




