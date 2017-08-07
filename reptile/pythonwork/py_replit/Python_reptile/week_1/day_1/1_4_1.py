from bs4 import BeautifulSoup
import requests
url = 'http://xa.xiaozhu.com/fangzi/1391456235.html'
def get_favs(url,data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
    adress =soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span')
    imgs = soup.select(' div > img')
    prices = soup.select('#pricePart > div.day_l > span')
    hostimgs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    hostnames = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    for title, img, adress, price , hostimg ,hostname in zip(titles, imgs, adress,prices,hostimgs,hostnames):
        data = {
            'title': title.get_text(),
            'adress':adress.get_text(),
            'img': img.get('src'),
            'price':price.get_text(),
            'hostimg':hostimg.get('src'),
            'hostname':hostname.get_text()
            }
        print(data)
get_favs(url)
