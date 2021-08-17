LionTravel Website scraping, store names extraction.

 
## Requirements
● Python 3    
● request   
● csv   
● re
● warnings  
● pymysql  
● time  


## Class
LionTravelStores


## Functions
● LoadPage    
● ParseContext   
● WrtToMysql   
● Work


## Create __init__
#### set website, page, headers, proxy, database, cursor
    def __init__(self):
	self.base_url = 'https://info.liontravel.com/category/zh-tw/store/index'
	self.page = 1
	self.headers = {'User-Agent':'Mozilla/5.0'}
	self.proxies = {'http':'http:// ip : port'}
	self.db = pymysql.connect(str(host), str(user), str(password), charset='utf8')
	self.cur = self.db.cursor()
        

#### 1. Call the main finction to work, Work.
    if __name__ == '__main__':
      spyderman = LionTravelStores()
      spyderman.Work()
			
			
#### 2. Go to the first function, LoadPage:  
    def LoadPage(self,url):
	req = requests.get(url,headers=self.headers,timeout=5)
	req.encoding = 'utf-8'
	html = req.text
	print('Loaded the page. It is parsing...')
	# put html into ParseContext function
	self.ParseContext(html)
    	   	
#### 3. Go to the ParsePage function, use regex patterns to parse html : 
    def ParseContext(self,html):
	pattern = re.compile(r'''{"id":\d+,"name":"(.*?)","address":"(.*?)"''',re.S)
	c_list = pattern.findall(html)
	print('Parsed the page. It is writing and saving to mysql database...')
	self.WrtToMysql(c_list)


#### 4. Go to the WrtToMysql function, to write info into Mysql:
    def WrtToMysql(self,c_list):
	# filter warning
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
        
#### 5. Finish:
    # shows 'Done' to notify all the runnings are done.
    print('Done.')
    
#### 6. Close cursor, database:
    self.cur.close()
    self.db.close()
