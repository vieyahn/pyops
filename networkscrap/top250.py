from urllib.request import urlopen
import ssl
from lxml import etree


url = "https://movie.douban.com/top250"
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_1)

def fetch_page(url):
    response = urlopen(url,context=context)
    return response

def parse(url):
    response = fetch_page(url)
    page = response.read()
    html = etree.HTML(page)

    xpath_movie = '//*[@id="content"]/div/div[1]/div/table'
    xpath_title = './/div[@class="pl2"]/a'
    xpath_pages = '//*[@id="content"]/div/div[1]/div/div/a'

    pages = html.xpath(xpath_pages)
    fetch_list = []
    result = []

    for element_movie in html.xpath(xpath_movie):
        result.append(element_movie)

    for p in pages:
        fetch_list.append(url+p.get('href'))

    for url in fetch_list:
        response = fetch_page(url)
        page = response.read()
        html = etree.HTML(page)

        for element_movie in html.xpath(xpath_movie):
            result.append(element_movie)

    for i,movie in enumerate(result,1):
        title = movie.find(xpath_title).text
        print(type(title))
        print(i,title)

def main():

    parse(url)

if __name__ == "__main__":
    main()

