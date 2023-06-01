from fastapi import FastAPI #FastAPI와 MongoDB를 사용하여 API를 구현
from pymongo import mongo_client
import pydantic
from bson.objectid import ObjectId
import os.path
import json

pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str # ENCODERS_BY_TYPE: pydantic의 JSON 인코더가 MongoDB [ObjectId]를 문자열(str)로 인코딩할 수 있도록 설정

app = FastAPI() #FastAPI 애플리케이션을 생성

#MongoDB Atlas 접속시
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
#HOSTNAME = get_secret("ATLAS_Hostname")
#USERNAME = get_secret("ATLAS_Username")
#PASSWORD = get_secret("ATLAS_Password")

#호스트 이름, 사용자 이름, 비밀번호를 사용하여 mongo_client.MongoClient를 초기화 -> 해당 클라이언트를 사용하여 MongoDB에 연결
#client = mongo_client.MongoClient(f'mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}')
#print('Connected to Mongodb ATLAS....') #연결에 성공하면 "Connected to Mongodb...." 메시지를 출력

#MongoDB Ubuntu 접속

HOSTNAME = '192.168.1.189:27017'

#호스트 이름, 사용자 이름, 비밀번호를 사용하여 mongo_client.MongoClient를 초기화 -> 해당 클라이언트를 사용하여 MongoDB에 연결
client = mongo_client.MongoClient(f'mongodb://{HOSTNAME}')
print('Connected to Mongodb Ubuntu....') #연결에 성공하면 "Connected to Mongodb...." 메시지를 출력

# 이전에 초기화한 client 객체를 사용=>MongoDB의 'test' 데이터베이스에 접속하고, 'testdb' 컬렉션을 선택
mydb = client['test'] # 'test' 데이터베이스에 접속
#mycol = mydb['AllUlfptcaAlarms'] # 'testdb' 컬렉션을 선택
#=> mycol 객체를 통해 'test' 데이터베이스의 'testdb' 컬렉션에 접근가능

# 애플리케이션 상태 확인
@app.get('/')
async def healthCheck():
    return "OK"

#url을 활용하여 데이터 불러오기 -> 응답을 문자열로 디코딩
def getRequestUrl(url):  # 주어진 URL에 HTTP 요청을 보내고, 성공적인 응답을 받아서 문자열로 반환
    # url을 매개변수로 받음
    req = urllib.request.Request(url)  # URL 요청을 나타내는 요청 객체 생성
    try:
        # urllib.request.urlopen() 함수: 요청 객체 req를 서버로 보내고, 서버로부터의 응답을 받음
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:  # 성공적인 HTTP 요청인 경우
            return response.read().decode('utf-8')  # response.read()는 응답의 내용을 바이트로 읽어옴, 바이트를 UTF-8 문자열로 디코딩하여 반환
    except Exception as e:  # 예외가 발생
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))  # 오류 메시지를 출력
        return None  # None을 반환

@app.get('/getData_Mongo')
async def getData_Mongo(collection):
    #collection을 매개변수로 받음
    mycol = mydb[collection] #mydb 데이터베이스 내에서 해당 컬렉션 선택
    return list(mycol.find().limint(20)) #.find(): 컬렉션 내의 모든 문서 반환. #.limit(20): 반환할 문서의 수를 '20'으로 제한. #list()함수: 결과를 리스트형태로 반환

@app.get('/getData_URL')
async def getUlfptcaAlarmInfo(year: str = None):
    # 파라미터의 값 설정
    #data_list = []  # 모든 데이터를 저장할 리스트

    if year == 'all':
        for year_data in range(2018, 2024):
            end_point = 'https://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo'
            
            parameters = '?serviceKey=' + get_secret("data_apiKey")
            parameters += '&returnType=json'
            parameters += '&numOfRows=500'
            parameters += '&pageNo=1'
            parameters += '&year=' + str(year_data)
            url = end_point + parameters
            print(url)
            print('-' * 50)
            
            response = requests.get(url) #서버에 get요청을 해서 응답받은 상태를 담아둠
            print(response)
            print('-' * 50)
            
            contents = response.text #UTF-8로 인코딩된 문자열 얻을 수 있음
            print(contents)
            print('-' * 50)
            
            dict = json.loads(contents) #인코딩된 문자열을 JSON으로 디코딩
            print(dict)
            print('-' * 50)
            
            items = dict['items'][0] #dict 데이터 체크
            print(type(items))
            print(items)
            print('-' * 50)
            
            #데이터를 선택적으로 불러오기
            item = ['sn', 'districtName', 'dataDate', 'issueVal', 'moveName', 'issueGbn', 'itemCode']
            validItem = {}
            for _ in item:
                validItem[_] = items[_]
            print(validItem)
            print('-' * 50)

            return validItem
      
            #result_toJSON = response.json()
            #data_list.extend(result_toJSON['response']['body']['items'])
        #return data_list

    else:  # 단일연도
        year = int(year)
        end_point = 'https://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo'
        parameters = ''
        parameters += '?serviceKey=' + get_secret("data_apiKey")
        parameters += '&returnType=json'
        parameters += '&numOfRows=500'
        parameters += '&pageNo=1'
        parameters += '&year=' + str(year)
        url = end_point + parameters
        print(url)

        response = requests.get(url)
        print('-' * 50)
        
        #result_toJSON = response.json()
        #return result_toJSON['response']['body']['items']
        
        contents = response.text
        print(contents)
        print('-' * 50)
        
        dict = json.loads(contents)
        print(dict)
        print('-' * 50)
        
        items = dict['items'][0] #dict 데이터 체크
        print(type(items))
        print(items)
        print('-' * 50)
            
        #데이터를 선택적으로 불러오기
        item = ['sn', 'districtName', 'dataDate', 'issueVal', 'moveName', 'issueGbn', 'itemCode']
        validItem = {}
        for _ in item:
            validItem[_] = items[_]
        print(validItem)
        print('-' * 50)

        return validItem

def getUlfptcaAlarmInfo_year(year: int = None, itemCode: str = None):
    if year is None: # year 변수가 None인 경우 현재 년도를 할당하도록 함
        now = datetime.now()
        current_year = now.year
        year = current_year
        return year
    elif year is None or year < 2018 or year > 2023:
        return '입력한 연도 관련 데이터가 존재하지 않습니다.'
    else:
        return year
    
    if itemCode is None: #itemCode 변수가 None인 경우 PM10과 PM25 모두 조회하도록
        return ['PM10', 'PM25']
    else:
        return itemCode
    
    end_point = 'https://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo'
    # API 호출에 필요한 파라미터들을 저장하기 위함
    parameters = ''
    parameters += '?serviceKey=' + get_secret("data_apiKey")
    parameters += '&returnType=json'
    parameters += '&numOfRows=500'
    parameters += '&pageNo=1'
    parameters += '&year=' + str(year) #측정연도
    parameters += '&itemCode=' + str(itemCode) #미세먼지 항목 구분(PM10, PM25), PM10/PM25 모두 조회할 경우 파라미터 생략
    
    url = end_point + parameters
    print(url)
