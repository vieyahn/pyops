import requests
from lxml import etree
from time import time
from threading import Thread


url  = "https://book.douban.com/top250"

def fetch_page(url):
    response = requests.get(url)
    return response

def parse(url):
    response = fetch_page(url)
    page = response.content
    html = etree.HTML(page)

    xpath_book = '//*[@id="content"]/div/div[1]/div/table'
    xpath_signature = './/span[@class="inq"]'
    xpath_title = './/div[@class="pl2"]/a'


    #xpath_title = './/span[@class="title"]'

    xpath_pages = '//*[@id="content"]/div/div[1]/div/div/a'

    pages = html.xpath(xpath_pages)
    fetch_list = []
    result = []

    for element_book in html.xpath(xpath_book):
        #print(element_book.attrib)
        result.append(element_book)


    for p in pages:
        fetch_list.append(p.get('href'))

    #test print("hello %s"%fetch_list)

    def fetch_content(url):
        response = fetch_page(url)
        page = response.content
        html = etree.HTML(page)
        for element_book in html.xpath(xpath_book):
            result.append(element_book)

    threads = []

    for url in fetch_list:
        t = Thread(target=fetch_content,args=[url,])
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    for i,book in enumerate(result,1):
        title = book.find(xpath_title).text
        str(title)
        print(i,title.strip())


def main():
    parse(url)

if __name__ == "__main__":
    main()
