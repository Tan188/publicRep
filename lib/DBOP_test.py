from lib.DBOP import DB

#数据准备
p1 = '15805511088'

db = DB()

if not db.check_user(p1):
	db.add_user(p1)

r = db.check_user(p1)

if r:
	print("存在")

db.del_user(p1)
r = db.check_user(p1)
if not r:
	print("已删除")


