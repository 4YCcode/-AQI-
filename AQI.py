import requests
import csv
import os

os.chdir('D:\Python-training\project\空氣品質指標(AQI)') #更改路徑(原路徑在C:\Users\amand)
csvfile = open('AQI.csv', 'w')    # 建立空白並可寫入的 CSV 檔案
csv_write = csv.writer(csvfile)

url='https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON'
data=requests.get(url)
data_json = data.json() 
output = [['縣市','地區','AQI','空氣品質']]
for i in data_json['records']:
    output.append([i["county"],i['sitename'],i['aqi'],i['status']]) 
print(output)
csv_write.writerows(output)

