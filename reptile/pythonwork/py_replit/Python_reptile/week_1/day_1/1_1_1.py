from bs4 import BeautifulSoup

with open('D:/Python爬虫/Python实战爬虫系统/课程与参考答案/week1/1_2/1_2answer_of_homework/1_2_homework_required/index.html','r') as wb_data:
    Soup = BeautifulSoup(wb_data,'lxml')
    titles = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    images = Soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    prices = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    messages = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > p')
    rates = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
#print(titles,images,rates,cates,descs,sep='\n------------------------\n')


for title,image,price,message,rate in  zip(titles,images,prices,messages,rates):
    data = {
        'title':title.get_text(),
        'image':image.get('src'),
        'price':price.get_text(),
        'message':message.get_text(),
        'rate':rate.get_text()
    }
    print(data)
