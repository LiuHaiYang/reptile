from bs4 import BeautifulSoup
import requests
urls=['http://xa.xiaozhu.com/search-duanzufang-p{}-0/?startDate=2016-10-07&endDate=2016-10-08'.format(str(i)) for i in range(2,4,1)]
url = 'http://xa.xiaozhu.com/search-duanzufang-p2-0/'
#url = 'http://xa.xiaozhu.com/fangzi/1391456235.html'
def get_favs(url,data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles =soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > div > a > span')
    imgs = soup.select('#page_list > ul > li > a > img')
    prices = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > span.result_price > i')
    hostimgs = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > span.result_img > a > img')
    texts = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > div > em')
    for  img, title, price , hostimg ,text in zip( imgs, titles,prices,hostimgs,texts):
        data = {
            'title':title.get_text(),
            'img': img.get('src'),
            'price':price.get_text(),
            'hostimg':hostimg.get('src'),
            'text':text.get_text()
            }
        print(data)
for url in urls:
    get_favs(url)