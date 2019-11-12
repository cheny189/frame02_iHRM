import unittest

import app
from case.Test_iHRM_Emp import Test_Emp
from case.Test_iHRM_Login import Test_Login
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(Test_Login("test_login_success"))
suite.addTest(Test_Emp("test_add"))
suite.addTest(Test_Emp("test_update"))
suite.addTest(Test_Emp("test_get"))
suite.addTest(Test_Emp("test_delete"))


# runner = unittest.TextTestRunner()
# runner.run(suite)

with open(app.PRO_PATH+ "/report/report.html","wb")as f:
    runner = HTMLTestRunner(f,title="人力资源管理系统测试报告",description="测试员工模块增删改查接口")
    runner.run(suite)
