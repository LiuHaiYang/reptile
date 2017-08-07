# -*- coding:utf-8 -*-
from  urllib.request  import urlopen,Request  
import re
from bs4 import BeautifulSoup 
#百度贴吧爬虫类
class BDTB:
 
    #初始化，传入基地址，是否只看楼主的参数
    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)

    #传入页码，获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
            request = Request(url)
            response = urlopen(request)
            # print(response.read().decode('utf-8'))#decode('utf-8')
            return response
        except URLError as e:
            if hasattr(e,"reason"):
                print ("连接百度贴吧失败,错误原因",e.reason)
                return None

    #获取帖子标题
    def getTitle(self):
        page = self.getPage(1)
        content = BeautifulSoup(page)
        title = content.title.get_text()
        defaultTitle = u"百度贴吧"
        #如果标题不是为None，即成功获取到标题
        if title is not None:
            self.file = open(title + ".txt","w",encoding='utf-8')
        else:
            self.file = open(self.defaultTitle + ".txt","w",encoding='utf-8')
        print(title)
        self.file.write(title)
        return title

    
    #获取总得页数
    def get_page_a(self):
        page = self.getPage(1)
        content = BeautifulSoup(page)
        page_count = content.find('span',{'class':'red'}).next_siblings
        ii = []
        for i in page_count:
            ii.append(i)
        page_ll = str(ii[1])[18:]
        page_l = page_ll[:1]
        # print(page_l)
        return page_l


    #获取每一层楼的内容,传入页面内容
    def getContent(self,page_p):
        page = self.getPage(page_p)
        content = BeautifulSoup(page)
        info = content.findAll('div',{'class':"d_post_content j_d_post_content "})
        for item in info:
            # print('===========================================')
            # print (item.get_text())
            self.file.write('\n' + '===========================================================================================' + '\n')
            self.file.write(item.get_text())


        

    def getinfo_all(self):
        page_all = self.get_page_a()
        # print(page_all)
        self.getTitle()
        for pp in range(1,int(page_all)):
            self.getContent(pp)

 
baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL,1)
# bdtb.getPage(1)
# bdtb.getTitle()
# bdtb.getContent()
bdtb.getinfo_all()
# bdtb.get_page_a()
