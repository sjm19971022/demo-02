import unittest
from controller import login


class Testlogin(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print('开始执行测试用例')
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print('测试用例执行完毕')
    #
    #
    #
    #
    # #@初始化
    # def setUp(self) -> None:
    #     print('执行初始化工作')
    #
    # def tearDown(self) -> None:
    #         print('执行清空工作')


    #case1 验证正确的用户名和密码登录
    def test_login1(self):
        print('执行测试用例1')
        self.assertEqual('登录成功',login('admin','123456'))

    #case2  验证正确的用户名和空的名字
    def test_login2(self):
        print('执行测试用例2')
        self.assertEqual('用户名不能为空',login('','123456'))


    def test_login3(self):
        print('执行测试用例3')
        self.assertEqual('密码不能为空',login('admin',''))





# suite = unittest.TestSuite()
# #suite.addTest(Testlogin('test_login2'))
# #suite.addTest(Testlogin('test_login3'))
#
# case_lst = [Testlogin('test_login2'), Testlogin('test_login3')]
# suite.addTests(case_lst)
#
# runnner = unittest.TextTestRunner(verbosity=2)
# runnner.run(suite)


# suite_smoke = unittest.TestSuite()
# suite_smoke.addTests(Testlogin('test_login1'))

