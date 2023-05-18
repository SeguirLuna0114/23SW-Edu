from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
import os.path
import json

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
HOSTNAME = get_secret("Mysql_Hostname")
PORT = get_secret("Mysql_Port")
USERNAME = get_secret("Mysql_Username")
PASSWORD = get_secret("Mysql_Password")
DBNAME = get_secret("Mysql_DBname")

DB_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DBNAME}' # 데이터베이스 연결 정보를 담고 있는 URL 정의

#db_conn 클래스: 데이터베이스 연결 및 세션 관리를 용이하게 해주는 기능을 제공
class db_conn:
    def __init__(self): #클래스의 인스턴스가 생성될 때 호출되는 생성자 메서드
        #create_engine 함수를 사용하여 데이터베이스 연결 엔진을 생성
        self.engine = create_engine(DB_URL, pool_recycle=500)
        #pool_recycle=500: 데이터베이스 연결 풀 내의 연결을 재사용하기 전에 최대한으로 유지하는 시간(초)을 설정
    
    def sessionmaker(self): #sessionmaker 함수를 사용하여 세션을 생성하고 반환
        Session = sessionmaker(bind=self.engine) #bind=self.engine을 통해 session과 데이터베이스 연결 엔진을 바인딩
        session = Session() #session: 데이터베이스와의 상호작용을 담당하는 객체
        return session
    
    def connection(self): #직접 데이터베이스 연결 객체를 얻을 수 있음
        conn = self.engine.connection() #self.engine.connection()을 호출하여 데이터베이스 연결 객체를 생성
        return conn
