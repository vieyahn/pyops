import requests
from lxml import etree
from time import time
from concurrent.futures import ProcessPoolExecutor


url = "https://book.douban.com/top250"

def fetch_page(url):
    response = requests.get(url)
    return response

def fetch_content(url):
    response = fetch_page(url)
    page = response.content
    return page

def parse(url):
    page = fetch_page(url)
    html = etree.HTML(page)

    xpath_book = '//*[@id="content"]/div/div[1]/div/table'
    xpath_signature = './/span[@class="inq"]'
    xpath_title = './/div[@class="pl2"]/a'
    xpath_pages = '//*[@id="content"]/div/div[1]/div/div/a'

    pages = html.xpath(xpath_pages)
    fetch_list = []
    result  = []

    for elemnt_book in html.xpath(xpath_book):
        result.append(elemnt_book)

    for p in pages:
        fetch_list.append(p.get('href'))

    with ProcessPoolExecutor(max_workers=2)  as executor:
        for page in executor.map(fetch_content,fetch_list):
            html = etree.HTML(page)
            for elemnt_book in html.xpath(xpath_book):
                result.append(elemnt_book)


    for i,book in enumerate(result,1):
        title = book.find(xpath_title).text

def main():
    parse(url)

if __name__=="__main__":
    main()