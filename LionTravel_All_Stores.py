
# use requests module/ proxies / import data to Mysql
import requests
import re
import csv
import warnings
import pymysql
import time


class LionTravel(object):
	def __init__(self):
		self.base_url = 'https://info.liontravel.com/category/zh-tw/store/index'
		self.page = 1
		self.headers = {'User-Agent':'Mozilla/5.0'}
		self.proxies = {'http':'http:// ip : port'}
		self.db = pymysql.connect(str(host), str(user), str(password), charset='utf8')
		self.cur = self.db.cursor()
    
	def LoadPage(self,url):
		req = requests.get(url,headers=self.headers,timeout=5)
		req.encoding = 'utf-8'
		html = req.text
		print('Loaded the page. It is parsing...')
		self.ParseContext(html)

  def ParseContext(self,html):
		pattern = re.compile(r'''{"id":\d+,"name":"(.*?)","address":"(.*?)"''',re.S)
		c_list = pattern.findall(html)
		print('Parsed the page. It is writing and saving to mysql database...')
		self.WrtToMysql(c_list)
    
  def WrtToMysql(self,c_list):
		#filter warning
		warnings.filterwarnings('ignore')
		try:
			self.cur.execute('create database if not exists LionTravel character set UTF8;')
			self.cur.execute('use LionTravel;')
			self.cur.execute('create table if not exists LionTravelStores( \
							Id int primary key auto_increment,\
							StoreName char(10), \
							Address varchar(50)) character set UTF8;')
		except Warning:
			pass

		insert_sql = 'insert into LionTravelStores(StoreName,Address) values(%s,%s);'
		for c_tuple in c_list:
			StoreName = c_tuple[0].strip()
			Address = c_tuple[1].strip()
			l = [StoreName,Address]
			self.cur.execute(insert_sql,l)
			self.db.commit()
		print('It is written and saved to mysql database.')
    
    
  def Work(self):
	    self.LoadPage(self.base_url)
	    print('Done.')
	    self.cur.close()
	    self.db.close()
    
    
if __name__ == '__main__':
  spyderman = LionTravelStores()
  spyderman.Work()				
