import json
from urllib import urlopen
from time

Init = urlopen("https://data.btcchina.com/data/historydata ")
datas = Init.read()

history_100 = json.loads(datas)
#for i,j in history_100:
#   print i,j

for i in history_100:
    print "Date                             Price"
    print ctime(int(i['date'])),'----',i['price']


