from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import io
import random
import pandas as pd
import openpyxl
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


from YungData import *
from IO.YungChorme import *
from IO.excel import *
from Context.YungTiny import *


#from IO import YungChorme
#from IO.excel import *
#from Context.YungTiny import *
#from Filter import *








def LoadExcelDataToHouses(sourceUrls):
    titleRow = getRowDataFromExcel(ouputFile, sheet, 0)
    for i in range(len(sourceUrls)):
        rowData = getRowDataFromExcel(ouputFile, sheet, i+1)        
        for i, data in enumerate(rowData):
            AppenedDataToHouse(houses, titleRow[i], rowData[i])

driver = YungDriver()
houses = GetHouse()

ouputFile = 'D:/PythonApplication1/PythonApplication1/PythonApplication1_v1/細抓1.xlsx'
sheet = '永慶'
index = 15
title = '網址'
sourceUrls = getUrlFromExcel(ouputFile,sheet,index,title)#

LoadExcelDataToHouses(sourceUrls)
houses = YungTiny(driver,sourceUrls,houses)#
StuffATableToExcel(houses,sheet,ouputFile)

#主邏輯:
#將要抓取的網址給Load
    #次邏輯:
    #excel來源抽換機率較低，主要可能的變化點是網址存放的位置可能是不同的欄，又或是列的筆數會有不同的狀況，不是順序性
#主邏輯:
#將每頁的網址所需要的資料轉換成一列
    #次邏輯：
    #瀏覽器抽換機率較低、目前chorme
    #模擬資料表做的結構。變動機率也不高。
    #所要抓的網址是否要用js，做過濾的動作
    #爬蟲目標的網址標籤，一定會變
#主邏輯：將結果呈現給使用者
    #次邏輯：
    #目前是輸出在excel，未來有可能在Db，網頁