import json
from pymongo import MongoClient
from pymongo import InsertOne

# MongoDB 접속 정보 설정
client = MongoClient('mongodb://192.168.1.189:27017')
db = client['testdb']  # 데이터베이스 이름 지정

for year in range(2018, 2024):
    collection = db['{}ParticleDataTests'.format(year)]  # 컬렉션 이름 지정

    # JSON 파일 경로
    json_file = 'XXX{}_UlfptcaAlarmInfo.json'.format(year)

    # JSON 파일 로드
    with open(json_file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    # Bulk Write 작업용 리스트 생성
    bulk_operations = []

    # 대용량 데이터를 작은 배치로 분할하여 Bulk Write 작업 생성
    for data in json_data:
        bulk_operations.append(InsertOne(data))
        if len(bulk_operations) >= 1000:  # 작은 배치 크기 설정
            collection.bulk_write(bulk_operations, ordered=False)
            bulk_operations = []

    # 남은 데이터에 대해 Bulk Write 작업 실행
    if bulk_operations:
        collection.bulk_write(bulk_operations, ordered=False)

    print(json_file, 'MongoDB imported!!')

# 연결 종료
client.close()
print('\n JSON file Finished!!')