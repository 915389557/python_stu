#!/usr/bin/python
#-*- coding:utf-8 -*-
import xlrd
class suopei_shuju(object):
    def duqu_jichu(self):
        shuju = []
        f = xlrd.open_workbook(r'C:\Use'
                               r'rs\Wmf\Desktop\python_学习\接口_框架\data\suopei.xls')
        sheet = f.sheets()[0]
        num = sheet.nrows
        for i in range(num):
            if i==0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju

if __name__ == '__main__':
    print(suopei_shuju().duqu_jichu())