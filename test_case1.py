#导包
from controller import login


#assert:断言
assert '登录成功' == login('admin','123456')

assert '密码不能为空' == login('admin','')


assert '用户名不能为空' == login('','123456')