from urllib.request import urlopen




htm = urlopen("http://www.baidu.com")


print(htm.read())