from bs4 import BeautifulSoup
import requests
url = 'http://bj.58.com/pingbandiannao/26001984319422x.shtml?adtype=1&entinfo=26001984319422_0&psid=143965789193452534368710195&iuType=q_2&ClickID=2&PGTID=0d3065d1-0000-1d79-2fed-3ab4c05c339c'
def get_ali(url,data=None):

    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    imgs = soup.select('#content img#img1')
    titles = soup.select('div > h1 ')
    prices = soup.select('div.su_con > span')
    links = soup.select('header > div.breadCrumb.f12')
    phones =soup.select('li.wupin_b > div > span')
    times = soup.select('li.time')
    adresses = soup.select('span.c_25d')
    if data == None:
        for   img ,title , price , phone ,link ,time ,adress  in zip (  imgs , titles , prices,phones , links , times, adresses):
            data = {
                'img':img.get('src'),
                'title':title.get_text(),
               'link':link.get_text(),
                'price':price.get_text(),
                'phone':phone.get_text(),
                'time':time.get_text(),
                'adress':adress.get_text()
            }
            print(data)
get_ali(url)
