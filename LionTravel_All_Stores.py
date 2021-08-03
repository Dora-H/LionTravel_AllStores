#雄獅旅遊/公司服務據點
import requests
import re
import csv


class LionTravelStores(object):
  def __init__(self):
    self.base_url = 'https://info.liontravel.com/category/zh-tw/store/index'
    self.headers = {'User_Agent':'Mozilla/5.0'}

    
  def LoadPage(self,url):
    res = requests.get(url,headers=self.headers)
    res.encoding = 'utf-8'
    html = res.text
    self.ParseContext(html)
    

  def ParseContext(self,html):
    pattern = re.compile(r'{"id":\d+.*?name":"(.*?)",',re.S)
    C_list = pattern.findall(html)
    self.WrtDc(C_list)

    
  def WrtDc(self,c_list):
    s = 0
    with open ('LionTravelStores.csv','a',newline='') as f :
      writer = csv.writer(f)
      writer.writerow( ['雄獅旅遊/公司服務據點'] )
      for c_item in c_list:
        s +=1
        writer.writerow( [c_item] )
      writer.writerow( ['\n'])
      writer.writerow( ['共',s,'個據點'] )
    
    
  def Work(self):
    self.LoadPage(self.base_url)
    print('Done.')
    
    
if __name__ == '__main__':
  spyderman = LionTravelStores()
  spyderman.Work()
