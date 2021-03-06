#!/usr/bin/python 
#-*- coding:utf-8-*- 
#user:吴鸣非
import time
import requests
import json
import unittest
import HTMLTestRunnertest
class Suopei(unittest.TestCase):
    def test_1(self):
        url='https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
        head={
         'Content-Type':'application/json',
         'x-dealer-code':'2100150',
         'x-position-code':'D_PO_1028',
         'x-resource-code':'BASIC_DATA',
         'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
         'x-user-code':'djy0mx',
         'x-access-token':'da05ee37e5676e7b27972b2892e0fdeb'
          }
        body='{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode('utf-8')
        res=requests.post(url,headers=head,data=body)
        mes=res.json()
        self.assertEqual(mes['data']['applicationType'][0]['name'],'多装')

    def test_2(self):
        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
        head = {
            'Content-Type': 'application/json',
            'x-dealer-code': '2100150',
            'x-position-code': 'D_PO_1028',
            'x-resource-code': 'BASIC_DATA',
            'x-track-code': '4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
            'x-user-code': 'djy0mx',
            'x-access-token': 'da05ee37e5676e7b27972b2892e0fdeb'
        }
        body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode('utf-8')
        res = requests.post(url, headers=head, data=body)
        mes = res.json()
        self.assertEqual(mes['data']['returnStatus'][0]['value'],'1')


    def test_3(self):
        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
        head = {
            'Content-Type': 'application/json',
            'x-dealer-code': '2100150',
            'x-position-code': 'D_PO_1028',
            'x-resource-code': 'BASIC_DATA',
            'x-track-code': '4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
            'x-user-code': 'djy0mx',
            'x-access-token': 'da05ee37e5676e7b27972b2892e0fdeb'
        }
        body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode('utf-8')
        res = requests.post(url, headers=head, data=body)
        mes = res.json()
        self.assertEqual(mes['data']['applicationMode'][1]['value'],'2')

    def test_4(self):
        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
        head = {
            'Content-Type': 'application/json',
            'x-dealer-code': '2100150',
            'x-position-code': 'D_PO_1028',
            'x-resource-code': 'BASIC_DATA',
            'x-track-code': '4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
            'x-user-code': 'djy0mx',
            'x-access-token': 'da05ee37e5676e7b27972b2892e0fdeb'
        }
        body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode(
            'utf-8')
        res = requests.post(url, headers=head, data=body)
        mes = res.json()
        self.assertEqual(mes['data']['applicationStatus'][0]['name'],'待上报' )
if __name__=='__main__':
        unittest.main()

# import time
import HTMLTestRunnertest
#
# class Suopei(unittest.TestCase):
#         def test_1(self):
#             self.assertNotEqual(123, 456)
#
#         def test_2(self):
#             self.assertEqual(123, 123)
#
#         def test_3(self):
#             self.assertEqual(456, 456)
#
#         def test_4(self):
#             self.assertNotEqual(400, 401)
#创建一个测试流程
suit=unittest.TestSuite()
#添加测试用例
for i in range(1,4):
 suit.addTest(Suopei('test_{}'.format(i)))
now=time.strftime('%Y-%m-%d%H:%M:%S',time.localtime(time.time()))
f=open('abc.html','wb')
runner=HTMLTestRunnertest.HTMLTestRunner(stream=f,title='索赔测试报告',tester='吴鸣非',description='结果如下')
runner.run(suit)
f.close()
