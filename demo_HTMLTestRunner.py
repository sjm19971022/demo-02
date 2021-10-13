#1、放在当前的项目下，方便导包



#2、导入  htmltestrunner  类
from HTMLTestRunner import HTMLTestRunner


#使用run 方法，写到html

flame = 'test_report.html'
f = open(flame,'wb')
runner = HTMLTestRunner(f,title='测试报告',description='v1.0')
runner.run(suite)

f.close()


with open(flame,'wb') as f:
    runner = HTMLTestrunner(f, title='测试报告', descriptinon'v1.0')
    runner.run(suite)