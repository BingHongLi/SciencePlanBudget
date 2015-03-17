#coding=utf-8

import requests
from bs4 import BeautifulSoup

'''
目標網頁: http://arsp.most.gov.tw/NSCWebFront/modules/talentSearch/talentSearch.do?

一千筆資料為一頁，爬取一頁便儲存一個檔案。


'''

for i in range(1,70,1):
    # 爬網頁的form data 設定
    payload={
        "currentPage":"%d"%i,
        "pageSize":"1000",
        "sortCondition":"",
        "specCode":"",
        "isSearch":"1",
        "LANG":"chi",
        "nameChi":"",
        "sex":"A",
        "organ_2_1":"",
        "organ_3_1":"",
        "organ_2_2":"",
        "organ_3_2":"",
        "organ_2_3":"",
        "organ_3_3":"",
        "organ_2_4":"",
        "organDesc":"",
        "kind_1":"",
        "spec_1":"",
        "academicExpertiseFullSearch":"",
        "code_1":"",
    }
    # 以上述form data 去擷取資料
    res=requests.post("http://arsp.most.gov.tw/NSCWebFront/modules/talentSearch/talentSearch.do?",data=payload)
    print "%d頁已爬取，準備進行parse"%i
    # parse 網頁結構
    soup=BeautifulSoup(res.text)
    print "%d頁已parse，準備進行儲存"%i
    # 開啟新檔案，準備將檔案寫入
    try:
        fileDest="./rawData/%d.txt"%i
        file_w = open(fileDest,'w')
        # 將資料寫入
        file_w.write(str(soup))
        print "%d頁成功爬取並儲存"%i
    except:
        print "%d頁儲存失敗"%i
    finally:
        file_w.close()
        print "%d.txt已關閉"%i