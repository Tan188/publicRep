import unittest
import sys
sys.path.append("../..")  # 提升2级到项目根目录下
from config.config import *
from test.user.test_REG import TestUserReg
from lib.HTMLTestReportCN import *


# suite = unittest.defaultTestLoader.discover("./")

suite=unittest.TestSuite()
suite.addTest(TestUserReg('test_user_reg_normal'))



f = open(report_file, 'wb') # 二进制写格式打开要生成的报告文件
HTMLTestRunner(stream=f,title="Api Test",description="测试描述").run(suite)
f.close()

#unittest.TextTestRunner(verbosity=2).run(suite)
