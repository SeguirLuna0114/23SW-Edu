import json, datetime, math
import requests
import os.path
import pandas as pd
import requests, bs4
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
from collections import defaultdict
from time import sleep 

key = "pz8AHfdVgweD18FrLox%2Bf84re1suiNrLxNSkqRY8qEqQgWkiIae1tYmHahgYbnW9mPZkDLQhzA70tsy4mCqXPg%3D%3D"

def dataUrl(numOfRows, pageNo):
    end_point = f'https://apis.data.go.kr/B551011/GoCamping/basedList?serviceKey={key}&'
    parameters = 'numOfRows=' + f"{numOfRows}"
    parameters += '&pageNo=' + f"{pageNo}"
    parameters += "&MobileOS=ETC&MobileApp=AppTest" 
    url = end_point + parameters
    res = requests.get(url).text.encode('utf-8')
    xmlobj = bs4.BeautifulSoup(res, 'lxml-xml')
    rows = xmlobj.findAll('item')
    
    return rows

rows = dataUrl(100, 1)
dic = defaultdict(list)
col = ["사이트간 거리", "사이트간 크기1", "사이트간 크기2", "사이트간 크기3", "사이트간 세로1", "사이트간 세로2", "사이트간 세로3", "사이트간 수량1", "사이트간 수량2", "사이트간 수량3"]
for _ in range(0,100):
    columns = rows[_].find_all()
    # col.append(columns[1].text)
    cnt = 0 
    for n in range(35, 45):
        a = {col[cnt] : columns[n].text}
        dic[f"{columns[1].text}"].append(a)
        cnt += 1

with open('SampleData.json', 'w') as f:       
    json.dump(dic, f, ensure_ascii=False)

        
# print(dic)