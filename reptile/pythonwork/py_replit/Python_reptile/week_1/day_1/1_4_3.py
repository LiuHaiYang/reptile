from bs4 import BeautifulSoup
import requests
import time
url = ''

def get_favs(url,data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles =soup.select(' ')
    imgs = soup.select(' ')
    prices = soup.select(' ')
    hostimgs = soup.select(' ')
    texts = soup.select('')
    for  img, title, price , hostimg ,text in zip( imgs, titles,prices,hostimgs,texts):
        data = {
            'title':title.get_text(),
            'img': img.get('src'),
            'price':price.get_text(),
            'hostimg':hostimg.get('src'),
            'text':text.get_text()
            }
        print(data)
def get_more_pages(start,end):
    for one in range(start,end):
        get_favs(url+str(one))
        time.sleep(2)

get_more_pages(1,2)