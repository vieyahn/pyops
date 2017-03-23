#coding=utf-8
from bs4 import BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)\
                              AppleWebKit 537.36 (KHTML, like Gecko) Chrome",\
                "Accept":"text/html,application/xhtml+xml,application/xml;\
                          q=0.9,image/webp,*/*;q=0.8"}


url = "https://en.wikipedia.org/wiki/Kevin_Bacon"
url_lagou = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="



req = session.get(url_lagou,headers=headers)


#html = urlopen(url_lagou)

#html1 = requests.Request("http://www.btcc.com")

print(req.text)

bsobj = BeautifulSoup(req.text,'html.parser')


#print(bsobj)

layout1 = bsobj.findAll('div',{"id":"s_position_list "})



print(layout1)