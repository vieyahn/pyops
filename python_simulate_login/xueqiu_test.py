import requests



url = "https://www.btcchina.com/"

url_auth = "https://api.btcchina.com/api.php/account/authenticate"

s = requests.Session()

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",\
           "Accept-Encoding":"gzip, deflate, br",\
           #"authorization":"Basic OTk1NTY0Mjg2QHFxLmNvbTpBcmllbFZhbmNlMDMwMg==",\
           "Connection":"keep-alive",\
           "content-type":"application/x-www-form-urlencoded",\
    }
payload = {}

r = s.post(url_auth,headers=headers)
r1 = s.post(url_auth)
print(r1.status_code)

print(r.status_code)
ses_get = s.get(url)
#print(ses_get.content)
str_btc = ses_get.content

rs = s.get("https://www.btcchina.com/exc/account/fund.cny")
print(rs.cookies)


x = requests.get("https://www.btcchina.com/exc/account/fund.cny")
print(x.cookies)
