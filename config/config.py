import logging
import os

#项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级的上一级目录（增加一级）
data_path = os.path.join(prj_path, 'data')  # 数据目录
log_file = os.path.join(prj_path, 'log', 'log.txt')  # 更改路径到log目录下
report_file = os.path.join(prj_path, 'report', 'report.html')  # 更改路径到log目录下

#日志设置
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=log_file,
                    filemode='a'
                    )

# 数据库配置
db_host='127.0.0.1'
db_port=3306
db_user='root'
db_passwd='a123456'
db_name='a_test'


if __name__=='__main__':
	logging.info("hello")