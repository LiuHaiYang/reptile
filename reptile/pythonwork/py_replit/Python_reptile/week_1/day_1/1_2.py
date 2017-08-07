from bs4 import BeautifulSoup
import requests

Url  = 'http://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
wb_data = requests.get(Url)
soup = BeautifulSoup(wb_data.text,'lxml')
titles = soup.select('div.property_title > a[target="_blank"]')
imgs = soup.select('img[width="160"]')
cates = soup.select('div.p13n_reasoning_v2')
#print(titles,imgs,cates)

for title,img,cate in zip(titles,imgs,cates):
    data = {
        'title':title.get_text(),
        'img':img.get('src'),
        'cate':list(cate.stripped_strings)
    }
    print(data)
    #打印出的图片的地址一样，这是反爬的机制