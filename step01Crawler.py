#coding=utf-8
# 迴圈爬頁數
import requests
from bs4 import BeautifulSoup
import re


file_w=open('./AllData150.csv','a')
#title="Year"+","+"HostName"+","+"Organziation"+","+"PlanName"+","+"ResultReport"+","+"Start"+","+"End"+","+"Budget"
#file_w.write(title.encode('utf8')+'\n')
for i in range(0,199,1):
    payload ={
        "__EVENTTARGET":"",
        "__EVENTARGUMENT":"",
        "__LASTFOCUS":"",
        "__VIEWSTATE":"/wEPDwUJNjcyNDczNjc3DxYCHgpRVUVSWV9DT0RFBQRRUzAxFgICAw9kFhwCAQ9kFggCAQ8PFgIeCEltYWdlVXJsBR5+L2ltYWdlcy9Bd2FyZC9OZXcvbG9nb18wMS5qcGdkZAIDDxYCHgVzdHlsZQVAd2lkdGg6OTklO2JhY2tncm91bmQtaW1hZ2U6dXJsKC4uL2ltYWdlcy9Bd2FyZC9OZXcvbG9nb19iZy5naWYpOxYCAgEPDxYCHwEFHn4vaW1hZ2VzL0F3YXJkL05ldy9sb2dvXzAyLmpwZ2RkAgUPD2QWBB4Lb25tb3VzZW92ZXIFLHRoaXMuc3JjPScuLi9pbWFnZXMvQXdhcmQvTmV3L2xvZ29fMDNfMi5naWYnHgpvbm1vdXNlb3V0BSx0aGlzLnNyYz0nLi4vaW1hZ2VzL0F3YXJkL05ldy9sb2dvXzAzXzEuZ2lmJ2QCBw8PFgIfAQUefi9pbWFnZXMvQXdhcmQvTmV3L2xvZ29fMDQuanBnZGQCAw8PFgIfAQUefi9pbWFnZXMvQXdhcmQvTmV3L21lbnUxXzIuZ2lmFgQfAwUqdGhpcy5zcmM9Jy4uL2ltYWdlcy9Bd2FyZC9OZXcvbWVudTFfMS5naWYnHwQFKnRoaXMuc3JjPScuLi9pbWFnZXMvQXdhcmQvTmV3L21lbnUxXzIuZ2lmJ2QCBQ8PFgIfAQUefi9pbWFnZXMvQXdhcmQvTmV3L21lbnUyXzEuZ2lmZGQCBw8PFgIfAQUefi9pbWFnZXMvQXdhcmQvTmV3L21lbnUzXzIuZ2lmFgQfAwUqdGhpcy5zcmM9Jy4uL2ltYWdlcy9Bd2FyZC9OZXcvbWVudTNfMS5naWYnHwQFKnRoaXMuc3JjPScuLi9pbWFnZXMvQXdhcmQvTmV3L21lbnUzXzIuZ2lmJ2QCCQ8PFgIeBFRleHQFBzAzMTMwOThkZAILDw8WAh8BBSd+L2ltYWdlcy9Bd2FyZC9OZXcvdGFibGVfbGVmdF90b3BfZy5naWZkZAINDxYCHwIFRmJhY2tncm91bmQtaW1hZ2U6dXJsKCcuLi9pbWFnZXMvQXdhcmQvTmV3L3RhYmxlX3RvcF9nLmdpZicpO3dpZHRoOjk5JTtkAg8PDxYCHwEFKH4vaW1hZ2VzL0F3YXJkL05ldy90YWJsZV9yaWdodF90b3Bf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KTtkAhcPDxYCHwEFKH4vaW1hZ2VzL0F3YXJkL05ldy90YWJsZV9sZWZ0X2Rvd25fZy5naWZkZAIZDxYCHwIFR2JhY2tncm91bmQtaW1hZ2U6dXJsKCcuLi9pbWFnZXMvQXdhcmQvTmV3L3RhYmxlX2Rvd25fZy5naWYnKTt3aWR0aDo5OSU7ZAIbDw8WAh8BBSl+L2ltYWdlcy9Bd2FyZC9OZXcvdGFibGVfcmlnaHRfZG93bl9nLmdpZmRkGAMFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYHBRxXVWN0bEF3YXJkSGVhZGVyMSRidG5OU0NIb21lBQ1idG5NdWx0aVF1ZXJ5BQpidG5TdWJTaWR5BQhidG5Bd2FyZAUcd1VjdGxBd2FyZFF1ZXJ5UGFnZSRidG5RdWVyeQUrd1VjdGxBd2FyZFF1ZXJ5UGFnZSRncmRSZXN1bHQkY3RsMTMkYnRuTmV4dAUrd1VjdGxBd2FyZFF1ZXJ5UGFnZSRncmRSZXN1bHQkY3RsMTMkYnRuTGFzdAUHbXZ3TWFpbg8PZAIBZAUdd1VjdGxBd2FyZFF1ZXJ5UGFnZSRncmRSZXN1bHQPFCsACmRkZGRkZBUCBVNSTk8yD0FXQVJEX1BMQU5fQ09ERRQrAAoUKwACAgEFEzEwNC0yNDIwLUgtMTU1LTAwMS0UKwACAgIFFjEwNC0yNDIwLUgtMDAyLTAxMC1NWTIUKwACAgEFEzEwNC0zMTEzLUUtMDA4LTAwNC0UKwACAgEFFTEwNC0yNjIzLUUtMTU1LTAwMy1FVBQrAAICAQUUMTA0LTMxMTMtRS0wNDJBLTAwMS0UKwACAgEFEzEwNC0yMzIxLUItNDAwLTAxNi0UKwACAgEFFTEwNC0yNjIzLUUtMTY4LTAwMi1FVBQrAAICAQUUMTA0LTI2MjMtRS02MDYtMDAzLUQUKwACAgEFFDEwNC0yNjIzLUUtNjA2LTAxMC1EFCsAAgIBBRMxMDQtMjMyMS1CLTAwMi0wNDctAiUUKwACAgEFEzEwNC0yNDIwLUgtMTU1LTAwMS1k55gfBVKtrcKfkVnn3zPK1zYwQA8=",
        "__VIEWSTATEGENERATOR":"629AD1C9",
        "__EVENTVALIDATION":"/wEWkAEC8ODoIQKpm+7LAgKOhJj7DwLUqauGBgLtjpCcCwKXkP7jBwL4qpyVCgLdw7OIDALG1NGjBgKr7ffWCAKVrPyCDwKVrPCCDwKVrLSBDwKVrKiBDwKVrKyBDwKVrKCBDwKVrKSBDwKVrJiBDwKVrJyBDwKVrJCBDwKarPyCDwKarPCCDwKarLSBDwKarKiBDwKarKyBDwKarKCBDwKarKSBDwKarJiBDwKarJyBDwKarJCBDwKLrPyCDwKLrPCCDwKyxoXgAgLd/OeWDwL4lciLCQLjgqqgAwKOu4zVDQKw+oeBCgKw+ouBCgKw+s+CCgKw+tOCCgKw+teCCgKw+tuCCgKw+t+CCgKw+uOCCgKw+ueCCgKw+uuCCgK/+oeBCgK/+ouBCgK/+s+CCgK/+tOCCgK/+teCCgK/+tuCCgK/+t+CCgK/+uOCCgK/+ueCCgK/+uuCCgKu+oeBCgKu+ouBCgKMt7/kBgKNt7/kBgKOt7/kBgKPt7/kBgKD2JWKCgKI5urOCAKI5urOCALXicCgBALWicCgBALVicCgBALUicCgBALTicCgBALSicCgBALRicCgBALgicCgBALvicCgBALuicCgBALticCgBALsicCgBAKI5qbgAgLnhZrlBgLnhZbmBgKcwef8DwKcwef8DwLCrs2SAwLHrs2SAwL0rs2SAwL/rs2SAwLxrs2SAwLjwOGlBALvs9i1CgKNk94kAoPYgY8KAqqs1/4EApyKoawGApfli8IKApPly8EKApLly8EKApfly8EKArWkrJYNArSkrJYNAsCpyecDAqvFg8sEAre+vPkGAqClhLYCApylkLYBAsWjrXwC1cyHkgwCysyHkgwCy8yHkgwCyMyHkgwCycyHkgwCzsyHkgwCz8yHkgwCzMyHkgwC3cyHkgwC0syHkgwCyszHkQwCyszLkQwCyszPkQwCyszzkQwCysz3kQwCysz7kQwCysz/kQwCyszjkQwCysynkgwCysyrkgwCy8zHkQwCy8zLkQwCy8zPkQwCy8zzkQwCy8z3kQwCy8z7kQwCy8z/kQwCy8zjkQwCy8ynkgwCy8yrkgwCyMzHkQwCyMzLkQwCyMzPkQwCyMzzkQwCyMz3kQwCyMz7kQwCyMz/kQwCt7nr3Q2l6q6eKqyP/uAP5yaYLlMB7AzgNg==",
        "wUctlAwardQueryPage$repQuery$ctl01$ddlYRst":"78",
        "wUctlAwardQueryPage$repQuery$ctl01$ddlYRend":"104",
        "wUctlAwardQueryPage$repQuery$ctl02$rblR":"1",
        "wUctlAwardQueryPage$repQuery$ctl03$ddlO1":"",
        "wUctlAwardQueryPage$repQuery$ctl04$txtT":"",
        "wUctlAwardQueryPage$repQuery$ctl05$txtT":"",
        "wUctlAwardQueryPage$repQuery$ctl06$ddlS1":"",
        "wUctlAwardQueryPage$repQuery$ctl07$rblR":"AWARD_YEAR",
        "wUctlAwardQueryPage$btnQuery.x":"23",
        "wUctlAwardQueryPage$btnQuery.y":"9",
        "wUctlAwardQueryPage$ddlPageSize":"200",
        "wUctlAwardQueryPage$grdResult$ctl13$ddlPage":"1",
        "wUctlAwardQueryPage$hidPage":"%d"%i
        }    
    res=requests.post("http://statistics.most.gov.tw/was2/award/AsAwardMultiQuery.aspx",data=payload)
    res.encoding='utf-8'
    soup =BeautifulSoup(res.text)
    for event in soup.find('table',{'class':'Grid_Font','id':'wUctlAwardQueryPage_grdResult'}).findAll('tr',{'class':'Grid_Row'}):
        try:
            planYear=event.findAll('td')[0].text.encode('utf8')
            hostName=event.findAll('td')[1].text.encode('utf8')
            organization=event.findAll('td')[2].text.encode('utf8')
            '''
            content[0]+content[1]為計畫名稱:名稱
            content[2]+content[3]為成果報告:報告內容
            content[4]+content[5]為執行起訖:執行時間
            content[6]+content[7]為總核定金額:金額
            '''
            content=event.findAll('td')[3].findAll('span')
            planName=content[1].text.encode('utf8')
            resultReport=content[3].text.encode('utf8')
            executePeriod=content[5].text.encode('utf8')
            start=re.match('(\d+\/\d+\/\d+)~(\d+\/\d+\/\d+)',executePeriod).group(1)
            end=re.match('(\d+\/\d+\/\d+)~(\d+\/\d+\/\d+)',executePeriod).group(2)
            budget=content[7].text.replace(',','').encode('utf8').replace('元','')
            temp='"'+planYear+'","'+hostName+'","'+organization+'","'+planName+'","'+resultReport+'","'+start+'","'+end+'","'+budget+'"'
            file_w.write(temp+'\n')
        except:
            print i 
            print "失敗過，可考慮重爬此頁" 

            
    for event in soup.find('table',{'class':'Grid_Font','id':'wUctlAwardQueryPage_grdResult'}).findAll('tr',{'class':'Grid_AlternatingRow'}):
        try:
            planYear=event.findAll('td')[0].text.encode('utf8')
            hostName=event.findAll('td')[1].text.encode('utf8')
            organization=event.findAll('td')[2].text.encode('utf8')
            '''
            content[0]+content[1]為計畫名稱:名稱
            content[2]+content[3]為成果報告:報告內容
            content[4]+content[5]為執行起訖:執行時間
            content[6]+content[7]為總核定金額:金額
            '''
            content=event.findAll('td')[3].findAll('span')
            planName=content[1].text.encode('utf8')
            resultReport=content[3].text.encode('utf8')
            executePeriod=content[5].text.encode('utf8')
            start=re.match('(\d+\/\d+\/\d+)~(\d+\/\d+\/\d+)',executePeriod).group(1)
            end=re.match('(\d+\/\d+\/\d+)~(\d+\/\d+\/\d+)',executePeriod).group(2)
            budget=content[7].text.replace(',','').encode('utf8').replace('元','')
            temp='"'+planYear+'","'+hostName+'","'+organization+'","'+planName+'","'+resultReport+'","'+start+'","'+end+'","'+budget+'"'
            file_w.write(temp+'\n')
        except:
            print i
            print "失敗過，可考慮重爬此頁"        
    print i
file_w.close()
print 'success'