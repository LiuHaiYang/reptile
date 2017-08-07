from bs4 import BeautifulSoup
import requests
url = 'http://bj.58.com/pbdnipad/0/pn2/?PGTID=0d3065d1-0000-1bea-d43e-0f783fe0856d&ClickID=1'
urls  = ['http://bj.58.com/pbdnipad/0/pn{}/?PGTID=0d3065d1-0000-1bea-d43e-0f783fe0856d&ClickID=1'.format(str(i)) for i in range(2,4,1)]
def get_ali(url,data=None):

    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    imgs = soup.select('td.img > a > img')
    titles = soup.select(' td.t > a')
    prices = soup.select('td.t > span.pricebiao > span')
    links = soup.select('td.t > span.desc')
    if data == None:
        for   img ,title , price , link   in zip (  imgs , titles , prices, links):
            data = {
                'img':img.get('src'),
                'title':title.get_text(),
               'link':link.get_text(),
                'price':price.get_text()
            }
            print(data)
#get_ali(url)
for single_url in urls:
    get_ali(single_url)