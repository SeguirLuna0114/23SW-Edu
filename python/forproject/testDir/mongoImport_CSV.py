import csv
from pymongo import MongoClient
from pymongo import InsertOne

# MongoDB 접속 정보 설정
client = MongoClient('mongodb://192.168.1.189:27017')
db = client['test']  # 데이터베이스 이름 지정
collection = db['FabCapaDatas_All']  # 컬렉션 이름 지정

# CSV 파일 경로
csv_file = 'CNFabCapacityDatas_All.csv'

# CSV 파일 읽기
data = []
with open(csv_file, 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(dict(row))

# MongoDB에 데이터 삽입
requests = [InsertOne(item) for item in data]
result = collection.bulk_write(requests)

print(csv_file, ' 파일 import 완료')
