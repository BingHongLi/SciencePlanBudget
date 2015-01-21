#### 專案內容:擷取科技部專案計畫補助款資料，資料視覺化後，尋找潛在客戶
### 1.擷取網站內容→2.轉存成csv(透過excel轉存，使R可直接讀取)→3.針對機構與單位名稱斷詞→4.資料視覺化(Spotfire)

## 1. 擷取網站內容(step01Crawler.py)
<br>資料來源</br>
<br>http://statistics.most.gov.tw/was2/award/AsAwardMultiQuery.aspx<br>
<br>抓取年度:100年-104年</br>
<br>抓取時針對計畫開始跟結束時間做切割</br>
<br>迴圈內要設定post的頁數，使用類似sprintf的方法</br>
<br>抓下來的檔案會存放在該專案資料夾下的data目錄</br>

## 2.轉存csv
<br>由於編碼問題，直接將python爬下的csv用excel重新存成csv檔，可使R順利讀取此中文編碼檔案(建議檔名存為completeData.csv，便不需要更改R的讀取檔案名)</br>

## 3. 針對機構與單位名稱斷詞(step03TextMining.R)
<br>字典製作，打開網頁監視器，可直接抓取input標籤內的option選項內的值，再透過replaceAll可更換所有不必要的符號，再將字典檔存入專案資料夾下的dic目錄中</br>
<br>執行step03TextMining.R檔後，會產生以當下日期命名的csv</br>

## 4.使用spotfire，讀取甫生成的csv，進行視覺化的調整，並存成dxp檔