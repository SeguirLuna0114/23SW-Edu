import csv
from pymongo import MongoClient

#MongoDB에 연결
client = MongoClient('mongodb://192.168.1.189:27017')
db = client['test']  # 데이터베이스 이름 지정
collection = db['collection2']  # 컬렉션 이름 지정

# CSV 파일 경로
csv_file = 'CN_FabCapacityData.csv'

# MongoDB 컬렉션에서 데이터 가져오기
data = collection.find()

# CSV 파일로 내보내기
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # 헤더 작성
    field_names = list(data[0].keys())
    writer.writerow(field_names)

    # 데이터 작성
    for document in data:
        writer.writerow(list(document.values()))

print("CSV 파일로 내보내기가 완료되었습니다.")