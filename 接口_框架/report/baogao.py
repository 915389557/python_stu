#!/usr/bin/python
#-*- coding:utf-8 -*-
from 接口_框架.report import HTMLTestRunner
import unittest

def baogao_(aa):
    suit = unittest.TestSuite()
    # 两个参数，1，路径  2.匹配条件
    # 到这个路径下，匹配所有的以test开头的文件
    # test开头文件中找到函数以test开头
    for o in aa:
        dis = unittest.defaultTestLoader.discover(r'C:\Users\Wmf\Desktop\python_学习\接口_框架\suo_test',pattern='test_{}.py'.format(o.strip()))
        for i in dis:
            suit.addTest(i)
    f = open(r'C:\Users\Wmf\Desktop\python_学习\接口_框架\report\a.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(title='索赔测试包告',stream=f,description='结果如下',tester='baizq')
    runner.run(suit)
    f.close()

if __name__ == '__main__':
    baogao_()