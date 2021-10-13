#所有的测试用例由该入口运行，这里面组装套件，运行套件
import unittest

#1、创建套件
suite = unittest.TestLoader().discover('.',pattern='test*.py')

#2、创建运行器
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)