from bs4 import BeautifulSoup
import requests
headers = {
    'Uesr-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
    'Cookie':'ServerPool=C; TAUnique=%1%enc%3AbFQRvXohvK%2BK%2BKBXQqjxKGE6%2FiwJkiRwJhzDICANiwA2jHwltRJPGQ%3D%3D; TASSK=enc%3AAMxAaCTDk2vVJrNAoruUNlODLEtk176YtOiQGcCVwiaLSySESGRRfOA6n6m9aeyQ7BAr297VfQjt01B18AFZ32iAZquX9chM41vks8ZLX2Rt%2Blpf2RkHnyszJIMgZSFEhQ%3D%3D; _jzqy=1.1475845060.1475845060.1.jzqsr=baidu|jzqct=tripadvisor%E5%AE%98%E7%BD%91.-; _jzqckmp=1; __gads=ID=1b2c6166ef8378c7:T=1475845052:S=ALNI_MZ8TJnvhI15J62af7hRSMcOVRSTOQ; CommercePopunder=SuppressAll*1475845433566; TAAuth2=%1%3%3Af181f27d164dc3a2d620a5966d6bf57f%3AACgftkZ0dvvmjf0quPi3zZf%2F7HXR2%2BzWdArDnWXXsa9nMguHBMzHfUPbuKkJTeuXfgGm2uegNRVGgkLu%2BfzOpQctJy34hydO1sssXqpc3jvtEsuZfpQNeXWYI%2FhVKzyv4BkvM6Gg9fnSGqU3CZGj2Gimc%2BRE0sRsf0qDwlknnFKvsy0OVvbl3Yn6UWXFmmnWMSlxEsOltL56vEQy4a7%2FajwBXNO2WuYeR3GGNLoBmyyd; bdshare_firstime=1475846234749; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.60763_281l105127_281l105125_281l1687489_281l267031_281*RS.1; CM=%1%t4b-pc%2C%2C-1%7CRCPers%2C%2C-1%7CHomeAPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CRCSess%2C%2C-1%7CHomeASess%2C2%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CPremiumMCSess%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7C2016sticksess%2C%2C-1%7Csesscoestorem%2C%2C-1%7CCCPers%2C%2C-1%7CCCSess%2C%2C-1%7CViatorMCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7Csesssticker%2C%2C-1%7C2016stickpers%2C%2C-1%7Ct4b-sc%2C%2C-1%7CViatorMCSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C2%2C-1%7Csessamex%2C%2C-1%7Cperscoestorem%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7Cpers_rev%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CRBAPers%2C%2C-1%7C; TAReturnTo=%1%%2FAttraction_Review-g60763-d267031-Reviews-Manhattan_Skyline-New_York_City_New_York.html; roybatty=TNI1625!AOUoy1SvYRuiBx84BMz8AqiPH%2FZ0EDjG%2B0u1ZP0L9gptFGvf7oYU8RuOvgwKtYvkxcyIxqgvMAfRP0Rwt%2FAKjI5leP33mypkHJuXf47bOcP3GdYBQLzbEL32kgbFIBKkGOSPIiEugj0BEpEwLbaDZg096aROhVMWTjQso5w0IAp8%2C1; NPID=; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1475845365; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1475846371; _qzja=1.1014560602.1475845060550.1475845060550.1475845060552.1475846349122.1475846371455..0.0.9.1; _qzjb=1.1475845060551.9.0.0.0; _qzjc=1; _qzjto=9.1.0; _jzqa=1.1196646216743080200.1475845060.1475845060.1475845060.1; _jzqc=1; _jzqb=1.9.10.1475845060.1; TASession=%1%V2ID.36954710D9B71DECCFE93F8164A0789B*SQ.59*MC.16631*PR.427%7C*LS.RecommendedAjax*GR.79*TCPAR.30*TBR.87*EXEX.89*ABTR.91*PPRP.66*PHTB.77*FS.43*CPU.28*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.49EA94D7826FEDF1B0F7D44E3FDA9071*LF.zhCN*FA.1*DF.0*LR.http%3A%2F%2Fbzclk%5C.baidu%5C.com%2Fadrc%5C.php%3Ftpl%3Dtpl_10144_14402_1%3Fl%3D1045915587%3Fie%3Dutf-8%3Ff%3D8%3Ftn%3D90648806_hao_pg%3Fwd%3Dtripadvisor%25E5%25AE%2598%25E7%25BD%2591%3Frqlang%3Dcn%3FinputT%3D5927%3Fsug%3Dtripadvisor%25E5%25AE%2598%25E7%25BD%2591*LP.%2F-a_tttype%5C.text-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.logo-m16631*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.267031; TAUD=LA-1475845036132-1*LG-1324345-2.1.F.*LD-1324346-.....'
}

url_save ='http://www.tripadvisor.cn/Saves#510353'
wb_data = requests.get(url_save,headers=headers)
soup = BeautifulSoup(wb_data.text,'lxml')
titles = soup.select('a.location-name')
imgs = soup.select('img.photo_image')
metas = soup.select('span.format_address')

for title,img,meta in zip(titles,imgs,metas):
    data={
        'title':title.get_text(),
        'img':img.get('src'),
        'meta':list(meta.stripped_strings)
    }
    print(data)
