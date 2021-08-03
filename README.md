LionTravel Website scraping, store names extraction.

 
## Requirements
● Python 3    
● request   
● csv   
● re


## Class
LionTravelStores


## Functions
● LoadPage    
● ParseContext   
● WrtDc   
● Work


## Run Codes
### Simply Crawling and Scraping Web Pages with below descriptions to start:

#### 1. Call the main finction to work, Work.
    if __name__ == '__main__':
      spyderman = LionTravelStores()
      spyderman.Work()
				
#### 2. Go to the first function, LoadPage:
    # requests the url 'https://info.liontravel.com/category/zh-tw/store/index'	    
    res = requests.get(url,headers=self.headers)
    res.encoding = 'utf-8'
    html = res.text
    # put html into ParseContext function
    self.ParseContext(html)
				
#### 3. Go to the ParsePage function:
    # use regex patterns to parse html 
    pattern = re.compile(r'{"id":\d+.*?name":"(.*?)",',re.S)
    C_list = pattern.findall(html)
    self.WrtDc(C_list)	
    
#### 4. Go to the WrtDc function:
    # set s=0 as the default of location quantity 
    s = 0
    with open ('LionTravelStores.csv','a',newline='') as f :
      writer = csv.writer(f)
      # write the title first
      writer.writerow( ['雄獅旅遊/公司服務據點'] )
      for c_item in c_list:
        s +=1
        # write store names into csv
        writer.writerow( [c_item] )
      writer.writerow( ['\n'])
      # finally, show the total number of locations
      writer.writerow( ['共',s,'個據點'] )
        
#### 5. Finish:
	# shows 'Done' to notify all the runnings are done.
    print('Done.')
