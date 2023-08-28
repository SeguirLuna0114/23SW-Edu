import pandas as pd
from pandas import DataFrame as df
from pymongo import MongoClient
import os
import json

# csv_data = pd.read_csv("aa_FoodData2.csv", sep = ",", low_memory=False, encoding='utf-8')
# csv_data.to_json("aa_FoodData2.json", orient = "records", force_ascii=False)

file_path = "aa_Food.json"

with open(file_path, 'r') as file:
    data = json.load(file)
    df = pd.DataFrame(data["Food"])
    new_Data = df[["type1", "name", "year", "servingsize", "unit", "kcal"]]
    new_Data = new_Data.sort_values("year")
    set_food = new_Data.drop_duplicates(["name"], keep = 'last')
    set_food = set_food[set_food["type1"] != "가공식품"].reset_index(drop=True)
set_food = set_food[set_food["kcal"] != "-"].reset_index(drop=True)

for _ in set_food.columns:
    if (_ == 'kcal') or (_ == 'servingsize'):
        set_food = set_food.astype({ _ : 'float'}) 
        print(f'{_} 포맷')
    else:
        print(f"{_} 패스")
        
cnt = 0
for i in set_food["unit"]:
    if i == "g" or i == "mL":
        score = set_food.loc[cnt, "servingsize"]
        score_change = 100 / score
        kal = set_food.loc[cnt,"kcal"]
        ser = set_food.loc[cnt,"servingsize"]
        
        set_food.loc[cnt,"kcal"] = kal * score_change
        set_food.loc[cnt,"servingsize"] = ser * score_change
    else:
        pass
    cnt += 1
set_food = set_food.round()
set_food = set_food.astype({ "servingsize" : 'int'})
for _ in range(len(set_food.index)):
    set_food["1회제공량"] = str(set_food["servingsize"][_]) + str(set_food["unit"][_])
    
set_food["1회제공량"]
set_food.drop(["servingsize","unit"], axis= 1, inplace=True)

set_food = set_food.rename(columns={"type1": "종류", "name": "식품이름", "year": "연도", "kcal": "열량"})
# print(set_food)
set_food.drop(["종류", "연도"], axis= 1, inplace=True)
print(set_food)

# set_food.to_json("modified_aa_FoodData.json", orient="records", force_ascii=False)

# json-server --watch ./modified_aa_FoodData.json --host 0.0.0.0 --port 5000
# http://192.168.1.78:5000/Food
# json-server 에 너무 큰 용량의 파일 띄우지 않기로함. 따라서 modified_aa_FoodData.json을 mosngodb에 넣기로함.

food = set_food.to_dict("records")
client = MongoClient('mongodb://192.168.1.78:27017/')

db = client['test']
collection_name = 'Food2Data'
collection = db[collection_name]

collection.insert_many(food)

client.close()