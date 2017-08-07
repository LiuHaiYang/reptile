from bs4 import BeautifulSoup
import requests

url= 'http://sh.58.com/pingbandiannao/27593663167417x.shtml?'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')

def get_links_from(who_sells):
    urls = []
    list_view = 'http://bj.58.com/pingbandiannao/{}/pn2'.format(str(who_sells))
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text,'lxml')
    for link in soup.select('td.t a.t'):
        urls.append(link.get('href').split('?')[0])
    return urls
  #  print(urls)

def get_views_from(url):
    id = url.split('/')[-1].strip('x.shtml')
    api = 'http://jst1.58.com/counter?infoid={}'.format(id)
    js = requests.get(api)
    views = js.text.split('=')[-1]
    return views

def get_item_info(who_sells=1):
    urls = get_links_from(who_sells)
    for url in urls:
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        data = {
            'title':soup.title.text,
             'price':soup.select('.price')[0].text,
            'area':list(soup.select('.c_25d')[0].stripped_strings) if soup.find_all('span','c_25d') else None,
            'cate':'商家' if who_sells == 1  else  '个人',
            'views':get_views_from(url)
            }
        print(data)

get_item_info()
#get_links_from()
#get_views_from(url)