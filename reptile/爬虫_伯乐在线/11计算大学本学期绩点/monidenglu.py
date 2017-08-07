# -*- coding:utf-8 -*-
import re
from urllib.request import urlopen,HTTPCookieProcessor,Request,build_opener
import urllib
import http.cookiejar
from bs4 import BeautifulSoup
from urllib.error import URLError, HTTPError
import pymongo
import json
#河北工程大学绩点运算
class SDU:
 
    def __init__(self):
        self.loginUrl = 'http://219.148.85.172:9380/loginAction.do'
        self.cookies = http.cookiejar.CookieJar()
        self.postdata = urllib.parse.urlencode({
            'zjh':'140950227',
            'mm':'19950910'
         })
        self.base_url = 'http://219.148.85.172:9380'
        self.opener = build_opener(HTTPCookieProcessor(self.cookies))
 
    def getPage(self):
        request  = Request(
            url = self.loginUrl,
            data = str.encode(self.postdata))
        result = self.opener.open(request)
        #打印登录内容
        denglu_data = result.read()
        # print(denglu_data.decode('gbk'))
        return denglu_data
    def get_main_url(self):
        body = self.getPage()
        bsObj = BeautifulSoup(body)
        all_url_main = bsObj.findAll('frame') 
        main_url=all_url_main[1]
        url_l = str(main_url)[93:112]
        url = self.base_url+url_l
        # print(url)
        # http://219.148.85.172:9380/menu/mainFrame.jsp
        return url
    def get_all_url(self): 
        try:
            all_url_body =self.get_main_url()
            print(all_url_body)
            
            request  = Request(
                url = all_url_body,
                data = str.encode(self.postdata))
            result = self.opener.open(request)
            result_data=result.read()
            bsObj = BeautifulSoup(result_data)
            result_url = bsObj.findAll('frame')
            main_url=result_url[2]
            url_l = str(main_url)[91:107]
            # print(url_l)
            url_ll = self.base_url +url_l
            return url_ll
        except URLError as e:
            print(e.reason)
        except HTTPError as e:
            print (e.code)
        else:
            print('ok')
            # print(bsObj.title)
    def get_all_url_a(self): 
        try:
            all_url_body =self.get_all_url()
            print(all_url_body)
            request  = Request(
                url = all_url_body,
                data = str.encode(self.postdata))
            result = self.opener.open(request)
            result_data=result.read()
            bsObj = BeautifulSoup(result_data)
            # result_url = bsObj.find('table',{'class':'hometopBg1'})
            result_url = bsObj.findAll("a",attrs={'href':True})   
            ##divCoHome > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(1) > td > table > tbody > tr > td > table > tbody > tr > td > table.homebody5 > tbody > tr > td > table.hometopBg1 > tbody > tr > td
            # print(result_url)
            p = []
            for ii in result_url:
                # print(ii[])
                p.append(ii)
            # print(p)
            #方案成绩

           

        except URLError as e:
            print(e.reason)
        except HTTPError as e:
            print (e.code)
        else:
            print('ok')
            return p
            # print(bsObj.title)

    # 获取成绩的url
    def get_all_kinds(self):
        try:
            p = self.get_all_url_a()
            chengji = p[0]
            # print(chengji)
            chengji_url_1=str(chengji)[44:73]
            chengji_url_2=str(chengji)[77:84]
            # print(chengji_url_1 + chengji_url_2)
            chengji_url =self.base_url + chengji_url_1 + chengji_url_2
            # print(chengji_url)

        except URLError as e:
            print(e.reason)
        except HTTPError as e:
            print (e.code)
        else:
            print('ok')
            return chengji_url
    def get_chengji_all(self):
        try:
            chengji = self.get_all_kinds()
            print(chengji)
            chengji_result = self.opener.open(chengji)
            chengji_result_data=chengji_result.read()
            bsObj_chengji = BeautifulSoup(chengji_result_data)
            chengji_url_main = bsObj_chengji.findAll("a",attrs={'href':True})
            # print(chengji_url_main)
            p =[]
            for i in chengji_url_main:
                p.append(i)
            # print(p[3])
            pp = p[3]

            chengji_url_1 = str(pp)[9:37]
            # print(chengji_url_1)
            chengji_url_2 = str(pp)[41:53]
            # print(chengji_url_2)
            chengji_url_3 = str(pp)[57:67]
            # print(chengji_url_3)
            chengji_url = self.base_url + '/' + chengji_url_1 + chengji_url_2 +chengji_url_3
            # print(chengji_url)
        except URLError as e:
            print(e.reason)
        except HTTPError as e:
            print(e.code)
        else:
            return chengji_url
    def get_chengji_all_aaa(self):
        chengji = self.get_chengji_all()
        print(chengji)
        chengji_result = self.opener.open(chengji)
        chengji_result_data_aaa=chengji_result.read()
        data = chengji_result_data_aaa.decode('gbk')
        # print(data)
        bsObj_chengji_aa = BeautifulSoup(data)
        # table = bsObj_chengji_aa.find(body.table)
        chengji_url_main_aa = bsObj_chengji_aa.findAll('',{'class':'odd'})
        jj = []
        for chengji in chengji_url_main_aa:
            txt = chengji.get_text()
            for ii in txt.split(' '):
                if ii == '' or ii=='\n\r\n' or ii =='\t' or ii =='\xa0\r\n' or ii =='\r\n':
                    pass
                else:
                    jj.append(ii)
        #个人情况
        # jj.insert(166,'重修\r\n')
        # print(jj[166])


        # for k in range(int((int(len(jj)-1))/14)):
        #     if k < 23 :
        #         # print((14 * int(k)) + 1)
        #         # print(jj[(14 * int(k)) + 1])
        #         del jj[(14 * int(k))]
        #     else:
        #         pass
        # # print(int(len(jj)))
        # for k in range(int((int(len(jj)-1))/13)):
        #     if k < 23 :
        #         # print((13 * int(k)) + 1)
        #         # print(jj[(13 * int(k)) + 1])
        #         del jj[(13 * int(k)) + 1]
        #     else:
        #         pass
        # # print(int(len(jj)))
        # for k in range(int((int(len(jj) - 1)) / 12)):
        #     if k < 23:
        #         # print((13 * int(k)) + 1)
        #         # print(jj[(13 * int(k)) + 1])
        #         del jj[(12 * int(k)) + 1]
        #     else:
        #         pass
        # print(int(len(jj)))
        # for k in range(int((int(len(jj) - 1)) / 11)):
        #     if k < 23:
        #         print((11 * int(k)) + 1)
        #         print(jj[(11 * int(k)) + 1])
        #         # del jj[(11 * int(k)) + 2]
        #     else:
        #         pass
        # print(int(len(jj)))
        # for k in range(int((int(len(jj) - 1)) / 10)):
        #     if k < 23:
        #         # print((13 * int(k)) + 1)
        #         # print(jj[(13 * int(k)) + 1])
        #         del jj[(10 * int(k)) + 3]
        #     else:
        #         pass
        # 课程号	课序号	课程名	英文课程名	学分	课程属性	成绩
        kcm = []
        for k in range(int(len(jj)/6)):
            kcm.append(jj[(6 * int(k)) + 2])
        # print(kcm)
        kch = []
        for k in range(int(len(jj) / 6)):
            kch.append(jj[(6 * int(k)) ])
        # print(kch)
        kxh = []
        for k in range(int(len(jj) / 6)):
            kxh.append(jj[(6 * int(k)) + 1])
        # print(kxh)
        xf = []
        for k in range(int(len(jj) / 6)):
            xf.append(jj[(6 * int(k)) + 3])
        # print(xf)
        xx = []
        for k in range(int(len(jj) / 6)):
            xx.append(jj[(6 * int(k)) + 4])
        # print(xx)
        ch = []
        for k in range(int(len(jj) / 6)):
            ch.append(jj[(6 * int(k)) + 5])
        # print(ch)
        bb= []
        for o in range(1,int(len(ch))):
            data_chengji = {
                '课程号':kch[o],
                '课序号': kxh[o],
                '学分': xf[o],
                '成绩': ch[o],
                '课程属性': xx[o],
                '课程名': kcm[o],
                }
            bb.append(data_chengji)
            # print(data_chengji)
        return bb

    def save(self):
        data = self.get_chengji_all_aaa()
        print(data)
        client_db = pymongo.MongoClient('127.0.0.1', 27017)
        db = client_db.pachong
        collection = db.chengji_dang
        for  a in data:
            collection.insert(a)

sdu = SDU()
# sdu.getPage()
# sdu.get_all_url()
# sdu.get_all_url()
# sdu.get_all_url_a()
# sdu.get_all_kinds()
# sdu.get_chengji_all_aaa()
sdu.save()



#http://219.148.85.172:9380/gradeLnAllAction.do?type=ln&oper=fainfo&fajhh=4701
#http://219.148.85.172:9380/gradeLnAllAction.do?type=ln&oper=fainfo&fajhh=4701