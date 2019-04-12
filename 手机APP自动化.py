#!/usr/bin/python 
#-*- coding:utf-8-*- 
#user:吴鸣非

from appium  import webdriver
import time

desired_caps={'platformName':'Android',
             # 'platformVersion':'6.0',
             'deviceName':'127.0.0.1:62001',
             'appPackage':'com.netease.cloudmusic',
             'appActivity':'.activity.LoadingActivity'}
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# driver.quit()

time.sleep(10)

driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()
time.sleep(10)
driver.find_element_by_id('com.netease.cloudmusic:id/ik').send_keys('17737545867')
time.sleep(10)
driver.find_element_by_id('com.netease.cloudmusic:id/ii').send_keys('w943595525')
time.sleep(10)
driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()
# driver.quit()
driver.find_element_by_id('com.netease.cloudmusic:id/qn').click()
time.sleep(10)
aa=driver.find_element_by_id('com.netease.cloudmusic:id/af4').text
if aa=='用户1801651294':
    print('pass')


