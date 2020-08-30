#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pymysql
import sys
sys.path.append('..')
from config.config import *

class DB:
	def __init__(self):
		self.conn = pymysql.connect(host=db_host,
			port=db_port,
			user=db_user,
			passwd=db_passwd,
			db=db_name)
		self.cur=self.conn.cursor()


	def __del__(self):
		self.cur.close()
		self.conn.close()

	def query(self,sql):
		self.cur.execute(sql)
		return self.cur.fetchall()

	def exec(self,sql):
		try:
			self.cur.execute(sql)
			self.conn.commit()
		except Exception as e:
			self.conn.rollback()
			print(str(e))

	def check_user(self,phone):
		result=self.query("select * from user where phone ='{}'".format(phone))
		return True if result else False

	def del_user(self, phone):
		self.exec("delete from user where phone= %s" %(phone))


	def add_user(self, phone):
		self.exec("insert into user (phone) value(%s)"%phone)


