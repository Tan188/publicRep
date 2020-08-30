import unittest
import requests
import os  # 增加了一个os，需要用来组装路径
import sys
sys.path.append("../..")  # 提升2级到项目根目录下
from config.config import *
from lib.read_excel import *  # 从项目路径下导入
from lib.case_log import *  # 从项目路径下导入
from lib.DBOP import *



class TestUserReg(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "TestUserReg")

	def test_user_reg_normal(self):
		case_date=get_test_data(self.data_list,'test_user_reg_normal')
		if not case_date:
			print('用例数据不存在')

		url=case_date['url']
		data=json.loads(case_date['data'])
		expect_res=case_date['expect_res']

		p=data['phone']
		# 判断数据再数据库中是否已经存在
		db=DB()
		if db.check_user(p):
			db.del_user(p)

		res=requests.post(url=url,data=json.dumps(data))
		log_case_info("test_user_reg_normal",url,data,expect_res,res.text)
		self.assertEqual(res.text,expect_res)
		# self.assertTrue(db.check_user(p))  # 数据库断言
		db.del_user(p)


	def test_user_reg_exist(self):
		db=DB()

		#检查用户是否存在
		if not db.check_user(p1):
			db.add_user(p1)

		data={'phone':p1}
		res=requests.post(url=self.url,data=json.dumps(data))

		res_dict=res.json()
		self.assertEqual(res_dict['code'],10000)
		assert  '已注册' in res_dict['msg']








