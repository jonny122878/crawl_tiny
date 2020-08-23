from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from YungData import *
import time
import io
import random
import pandas as pd
import openpyxl

def FillDefaultData(idx, houses):
    for i, key in enumerate(houses):
    # 社區
        if i>=15:
            SetDataToHouseByIdx(houses, idx, key, "")

def YungTiny(driver,urls,houses):
    for idx, url in enumerate(urls):
        FillDefaultData(idx, houses)

        driver.get(url)
        time.sleep(3)
        soup=BeautifulSoup(driver.page_source,'html.parser')

        if soup == None:
            continue

        notFoundDiv = soup.findAll("div", {"class": "m-house-error_msg middleSet"})
        if len(notFoundDiv) >=1:
            continue
            
    #time.sleep(random.uniform(30,60))
    ##處理外觀
        #img=soup.find('img',class_='carousel-main-photo')
        #prjimg.append(img.get('src'))

    #處理電話
        tel=soup.find('div',class_='m-info-tel')
        for index in tel.children:
            if index.string!=None and index.string!='\n':
                SetDataToHouseByIdx(houses, idx, '電話', index.string)
    #處理社區
        comu=soup.find('a',attrs={'style':'text-decoration: underline;'})
        if comu==None:
            SetDataToHouseByIdx(houses, idx, '社區', "")
        else:
            SetDataToHouseByIdx(houses, idx, '社區', comu.string)
    #處理土地坪數
        Nol=soup.find_all('li',class_='left') 
        SetDataToHouseByIdx(houses, idx, '土地坪數', Nol[1].string.replace('土地坪數：','').replace('坪',""))

    #處理朝向
        Dir=soup.find_all('ul',class_='detail-list-lv1')
        findit=False
        for index in Dir[len(Dir)-1].children:
            if index!=None:
                if str(index.string).find('朝向')!=-1 and findit==False:
                    findit=True
                    SetDataToHouseByIdx(houses, idx, '朝向', index.string)
        
    #處理主建物、附屬建物、共有部分
        BS=soup.find('ul','detail-list-lv2')

        MBFind=False
        AbFind=False
        CpFind=False
        if BS!=None:
            for index in BS.children:
                if index!=None:
                    if str(index.string).find('主建物小計')!=-1 and MBFind==False:#主建物
                        MBFind=True
                        SetDataToHouseByIdx(houses, idx, '主建物', index.string.replace('主建物小計：',"").replace('坪',''))
                    elif str(index.string).find('附屬建物小計')!=-1 and AbFind==False:#附屬建物
                        AbFind=True
                        sp=(index.string.replace('附屬建物小計：',"").replace('坪','')).split(" ",1)
                        SetDataToHouseByIdx(houses, idx, '附屬建物', sp[0])
                    elif str(index.string).find('共同使用小計')!=-1 and CpFind==False:#共有部分
                        CpFind=True  
                        SetDataToHouseByIdx(houses, idx, '共有部分', index.string.replace('共同使用小計：',"").replace('坪',''))                
        if MBFind==False:
            SetDataToHouseByIdx(houses, idx, '主建物', "")
        if AbFind==False:
            SetDataToHouseByIdx(houses, idx, '附屬建物', "")
        if CpFind==False:
            SetDataToHouseByIdx(houses, idx, '共有部分', "")
        
    driver.close()
    return houses
       
#houses['加蓋'].append(temp3[index])
#           houses['次序'].append("")
#           houses['外觀'].append("")
#           houses['社區'].append("")
#           houses['土地坪數'].append("")
#           houses['朝向'].append("")
#           houses['電話'].append("")
#           houses['主建物'].append("")
#           houses['附屬建物'].append("")
#           houses['共有部分'].append("")
#           houses['段建號'].append('')

#        houses = trans_df={
#    '房屋品牌':prjbrand,
#    '次序':prjID,
#    '案名':prjName,
#    '地址':prjaddr,
#    '價錢':prjprice,

#    '格局':prjPattern,
#    '加蓋':prjStamped,
#    '坪數':prjNop,
#    '樓層':prjStair,
#    '屋齡':prjAge,

#    '索引':prjIndex,
#    '種類':prjType,
#    '外觀':prjImg,
#    '車位':prjParking,
#    '網址':prjhref,

#    '社區':prjComu,
#    '段建號':prjSN,
#    '土地坪數':prjNol,
#    '朝向':prjDir,
#    '電話':prjtel,

#    '主建物':prjMainBui,
#    '附屬建物':prjAb,
#    '共有部分':prjCp      
#}    