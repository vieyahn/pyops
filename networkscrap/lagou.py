import requests
from lxml import etree


url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="

def fetch_page(url):
    response = requests.get(url)
    return response

def parse(url):
    response = fetch_page(url)
    page = response.content
    html = etree.HTML(page)

    work_path = '//*[@class="content_left"]/div[3]/ul/li'
    #print(work_path)
    two_path = './/div[@class="company_name"/a]'

    works = html.xpath(work_path)

    print(works)

    for item in works:
        print(item.text)

parse(url)