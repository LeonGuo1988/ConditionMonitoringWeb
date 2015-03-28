#encoding=utf-8
import pymysql

class connection:

	def __init__(self):
		self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='admin_mfds', passwd='123456789', db='mfds', charset='utf8')
	def connect(self):
		return self.conn