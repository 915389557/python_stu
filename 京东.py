#!/usr/bin/python 
#-*- coding:utf-8-*- 
#user:吴鸣非
from selenium import webdriver
from time import sleep

dr=webdriver.Chrome()

#打开网址
# dr.get('https://www.jingdong.com')
dr.get('https://passport.jd.com/uc/login?ltype=logout')
sleep(2)
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
# dr.switch_to.frame('login_frame')
# sleep(5)
# dr.find_element_by_xpath('//*[@id="key"]').click()
# sleep(5)
# dr.find_element_by_xpath('//*[@id="key"]').send_keys('python')
# sleep(5)
# dr.find_element_by_xpath('//*[@id="search"]/div/div[2]/button/i').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[7]/a[3]').click()
# sleep(2)


# w=dr.find_element_by_xpath('//*[@id="loginname"]').find_elements_by_tag_name('li')
# for i in w:
#     ActionChains(dr).move_to_element(i).perform()  #控制鼠标来移动到元素位置  执行
#     sleep(2)
dr.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="loginname"]').send_keys('123df456')
sleep(2)
dr.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys('123fsa4567')
sleep(2)
dr.find_element_by_id('loginsubmit').click()
sleep(5)
start=dr.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]')
sleep(2)
# drag_and_drop。拖拽 (起始位置，结束位置）
# drag_and_drop_by_offset  （起始位置，X轴坐标，Y轴坐标）

ActionChains(dr).drag_and_drop_by_offset(start,68,0).perform()
sleep(2)

