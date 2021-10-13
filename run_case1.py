#所有的测试用例由该入口运行，这里面组装套件，运行套件
import unittest
from HTMLTestRunner import HTMLTestRunner

#1、创建套件
suite = unittest.TestLoader().discover(r'E:\python\demo02',pattern='test*.py')

#2、创建运行器

report_path = 'test_report.html'
with open(report_path,'wb') as f:
    runner = HTMLTestRunner(f, title='测试报告', description='v1.0')
    runner.run(suite)