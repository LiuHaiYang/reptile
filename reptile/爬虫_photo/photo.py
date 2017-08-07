from bs4 import BeautifulSoup
import requests
# url='http://www.zbjuran.com/dongtai/'
url = 'http://mp.weixin.qq.com/s?__biz=MzA4MTc3NTQ3NA==&mid=2650094317&idx=1&sn=0994fce9d8b8f5f8e08f32e69c3abeda'
def get_photo(url,data=None):
    wb_data = requests.get(url)
    print(wb_data)
    soup = BeautifulSoup(wb_data.text,'lxml')
    # img-content > ul > li:nth-child(3) > label > div > span > img
    imgs = soup.select('label > div > span > img')
    #img-content > ul > li:nth-child(3) > label > span
    titles = soup.select('label > span')
    # imgs = soup.select('div.text > p > img')
    # titles = soup.select('h3 > a > b')
    if data == None:
        for img,title in zip(imgs,titles):
            data = {
                'img':img.get('src'),

                'title':title.get_text()
            }
            print(data)
get_photo(url)
