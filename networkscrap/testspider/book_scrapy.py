import sys
import time
import urllib
import requests
import numpy as np
from bs4 import BeautifulSoup
from openpyxl import Workbook

sys.setdefaultencoding('utf-8')


#User-Agent
hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]

def book_spider(book_tag):
    page_num = 0
    book_list = []
    try_time = 0

    url = 'http://www.douban.com/tag/'+urllib.quote(book_tag)+'/book?start='+str(page_num*15)

