import csv
from pymongo import MongoClient
from pymongo import InsertOne

# MongoDB 접속 정보 설정
client = MongoClient('mongodb://192.168.1.189:27017')
db = client['test']  # 데이터베이스 이름 지정
collection = db['FabCapacityDatas']  # 컬렉션 이름 지정

# CSV 파일 경로
csv_file = 'FabCapacityData.csv'

# CSV 파일 읽기 및 MongoDB에 import
with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    documents = [row for row in reader]
    collection.insert_many(documents)

print('CSV 파일 import 완료')