from fastapi import FastAPI #FastAPI와 MongoDB를 사용하여 API를 구현
from pymongo import mongo_client
import pydantic
from bson.objectid import ObjectId
import os.path
import json

pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str # ENCODERS_BY_TYPE: pydantic의 JSON 인코더가 MongoDB [ObjectId]를 문자열(str)로 인코딩할 수 있도록 설정

app = FastAPI() #FastAPI 애플리케이션을 생성

#비밀정보를 로드하고 가져오기 위한 함수 정의
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./"))) #재 스크립트의 상위 디렉토리 경로를 BASE_DIR 변수에 할당
secret_file = os.path.join(BASE_DIR, '../../secret.json') #BASE_DIR과 상대 경로를 조합하여 비밀 정보가 저장된 파일의 경로를 secret_file 변수에 할당

with open(secret_file) as f: #secret_file을 열고 파일 객체 f를 생성
    secrets = json.loads(f.read()) #파일의 내용을 읽어와 JSON 형식으로 디코딩하여 secrets 변수에 할당

def get_secret(setting, secrets=secrets): #비밀 정보를 가져오기 위한 함수
    try:
        return secrets[setting] #setting 매개변수로 설정 이름을 받음 -> secrets 딕셔너리에서 해당 설정 이름에 해당하는 값을 찾아 반환
    except KeyError: #secrets에 존재하지 않는 경우
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg #환경 변수를 설정하라는 오류 메시지를 반환

#정의한 get_secret()함수 사용 => Mongodb 호스트이름, 사용자이름, 비밀번호를 가져와 MongoDB에 연결
HOSTNAME = get_secret("ATLAS_Hostname")
USERNAME = get_secret("ATLAS_Username")
PASSWORD = get_secret("ATLAS_Password")

#호스트 이름, 사용자 이름, 비밀번호를 사용하여 mongo_client.MongoClient를 초기화 -> 해당 클라이언트를 사용하여 MongoDB에 연결
client = mongo_client.MongoClient(f'mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}')
print('Connected to Mongodb....') #연결에 성공하면 "Connected to Mongodb...." 메시지를 출력

# 이전에 초기화한 client 객체를 사용=>MongoDB의 'test' 데이터베이스에 접속하고, 'testdb' 컬렉션을 선택
mydb = client['test'] # 'test' 데이터베이스에 접속
mycol = mydb['testdb'] # 'testdb' 컬렉션을 선택
#=> mycol 객체를 통해 'test' 데이터베이스의 'testdb' 컬렉션에 접근가능

#/: 'OK'라는 문자열을 반환하는 기본 엔드포인트
@app.get('/')
async def healthCheck(): #서버의 연결상태 확인
    return "OK"

#/getmongo: MongoDB의 mycol 컬렉션에서 최대 10개의 문서를 가져오는 엔드포인트
@app.get('/getmongo')
async def getMongo():
    return list(mycol.find().limit(10))

#/getuser: 지정된 id에 해당하는 사용자를 MongoDB의 mycol 컬렉션에서 검색하는 엔드포인트
@app.get('/getuser')
async def getuser(id=None):
    if id is None:
        return "id를 입력하세요."
    result = mycol.find_one({"id":id})
    if result:
        return result #요청으로 받은 id에 해당하는 사용자를 mycol 컬렉션에서 검색하여 결과를 반환
    else:
        return "검색 결과가 없습니다."

#/useradd: 지정된 id와 name으로 사용자를 추가하는 엔드포인트
@app.get('/useradd')
async def useradd(id=None, name=None):
    if (id and name) is None:
        return "id, name을 입력하세요."
    else:
        user = dict(id=id, name=name)
        mycol.insert_one(user)
        result = mycol.find_one({"id":id})
        return result

#/userupdate: 지정된 id의 사용자의 이름을 업데이트하는 엔드포인트
@app.get('/userupdate')
async def userupdate(id=None, name=None):
    if (id or name) is None:
        return "id, name을 입력하세요"
    else:
        user = mycol.find_one({"id":id}) #지정된 id에 해당하는 사용자를 검색
        if user: #user가 존재하는지 여부
            filter = {'id':id} #업데이트 대상이 되는 사용자를 필터링
            data = {"$set":{'name':name}} # 업데이트할 필드와 값을 지정
                #"$set"은 MongoDB의 업데이트 연산자 
            mycol.update_one(filter, data) #filter에 해당하는 사용자의 필드를 data에 지정된 값으로 업데이트
            result = mycol.find_one({"id":id}) #업데이트된 사용자 정보를 다시 검색
            return result #업데이트된 사용자 정보를 반환
        else:
            return f"id = {id} 데이터가 존재하지 않습니다."

#/userdel: 지정된 id의 사용자를 삭제하는 엔드포인트
@app.get('/userdel')
async def userdel(id=None):
    if id is None:
        return "id를 입력하세요"
    else:
        user = mycol.find_one({"id":id})
        if user:
            mycol.delete_one({"id":id})
            return list(mycol.find().limit(10))
        else:
            return f"id = {id} 데이터가 존재하지 않습니다."