import os
import unittest
import time

from HTMLTestRunner_PY3 import HTMLTestRunner

from script.test_emp05_param import TestEmployee
from script.test_login_param import TestLogin

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmployee))
report_path = os.path.dirname(os.path.abspath(__file__))+"/report/IHRM{}.html".format(time.strftime("%Y%m%d%H%M%S"))
#如果在jenkins当中引入这个报告,那么需要把时间删掉
# report_path = os.path.dirname(os.path.abspath(__file__))+"/report/IHRM{}.html"
with open(report_path,mode='wb')as f:
    runner = HTMLTestRunner(f,verbosity=2,title="IHRM接口测试(登录和员工管理模块)",description="HTMLTestRunner_py3生成报告")
    runner.run(suite)