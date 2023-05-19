#한국환경공단_에어코리아_대기오염
import requests
import json, urllib.request, math
import pandas as pd
from datetime import datetime, timedelta
import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
#os.path.relpath("./")는 현재 스크립트 파일의 상대 경로를 반환
#os.path.dirname()을 두 번 호출하여 상위 디렉토리 경로를 얻음

#os.path.join() 함수: 경로를 결합
secret_file = os.path.join(BASE_DIR, '../secret.json') #BASE_DIR과 '../secret.json'을 결합하여 비밀 파일의 경로를 생성

#with 문을 사용 => 파일을 열고 사용한 후에 자동으로 닫히도록 보장
with open(secret_file) as f:
    secrets = json.loads(f.read()) #json.loads() 함수를 사용하여 JSON 문자열을 파싱하고 파이썬객체로 변환

def get_secret(setting, secrets=secrets):#설정 값을 가져오기 위해 secrets 딕셔너리를 참조하는 함수 정의
    # setting 매개변수로 설정 값을 지정하고, 기본값으로 secrets 변수를 사용
    try: #secrets 딕셔너리에서 setting에 해당하는 값을 가져오려 시도
        return secrets[setting] #secrets 딕셔너리에서 setting에 해당하는 값을 반환
    except KeyError: #KeyError 예외가 발생
        # setting에 해당하는 환경 변수를 설정하라는 오류 메시지를 반환
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

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

#공공데이터포털에서 '한국환경공단_에어코리아_대기오염'데이터를 가져와 JSON 형식으로 저장
#시도명(전국):https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=3jrfQwF8GqsGiZXpzCOgPdESM%2FQAoErRSKH6LXfZK6%2BuKdPV%2F8bTS0ytNHnrs0vp4ve0DLHeRuMelVEUlPHDYQ%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%A0%84%EA%B5%AD&ver=1.0
def getArpltInfoData(pageNo, numOfRows, sidoName):
    # pageNo와 numOfRows, sidoName을 매개변수로 받음
    end_point = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'

    # API 호출에 필요한 파라미터들을 저장하기 위함
    parameters = ''
    parameters += '?serviceKey=' + get_secret("data_apiKey")  # serviceKey는 비밀키를 설정
    parameters += 'returnType=json'  # JSON 형식으로 요청
    parameters += '&numOfRows=' + str(numOfRows)  # 한 페이지 당 결과 개수
    parameters += '&pageNo=' + str(pageNo)  # 페이지 번호
    parameters += '&sidoName=' + sidoName #시도 이름(전국, 서울, 부산, 대구, 인천, 광주, 대전, 울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주, 세종)
    parameters += '&ver=1.0' #버전별 상세 결과 참고

    # URL 생성: url 변수에 엔드포인트 URL과 파라미터를 조합하여 완전한 URL을 생성
    url = end_point + parameters

    print('URL')
    print(url)

    # getRequestUrl(url) 함수를 사용하여 생성한 URL로 API 요청을 보내고, 응답을 받음
    result = getRequestUrl(url)
    if (result == None):  # 응답이 None인 경우, None을 반환
        return None
    else:  # 응답이 None이 아닌 경우
        return json.loads(result)  # 응답을 JSON 형식으로 변환하여 반환

#빈 리스트 jsonResult를 생성합니다. 이 리스트는 모든 결과를 저장
jsonResult = []

#파라미터의 값 설정
pageNo = 1
numOfRows = 100
sidoName = '%EC%A0%84%EA%B5%AD' #전국
#시도 이름(전국, 서울, 부산, 대구, 인천, 광주, 대전, 울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주, 세종)

nPage = 0
while (True):  # 무한루프
    print('pageNo : %d, nPage : %d, sidoName : %s' % (pageNo, nPage, sidoName))  # 현재 페이지 번호와 총 페이지 개수를 출력
    jsonData = getArpltInfoData(pageNo, numOfRows, sidoName)  # getArpltInfoData(pageNo, numOfRows, sidoName) 함수를 호출하여 데이터를 가져옴
    print(jsonData)

    if (jsonData['response']['header']['resultCode'] == '00'):  # jsonData의 결과 코드를 확인하여 성공적으로 데이터를 가져왔는지 확인
        totalCount = jsonData['response']['body']['totalCount']
        print('데이터 총 개수 : ', totalCount)

        for item in jsonData['response']['body']['items']:
            jsonResult.append(item)  # 가져온 데이터를 jsonResult 리스트에 추가

        if totalCount == 0:  # 데이터의 총 개수가 0인 경우(데이터가 더이상 없는 경우), 루프를 종료
            break

        # 총 페이지 개수 계산
        nPage = math.ceil(totalCount / numOfRows)  # 한 페이지당 결과 개수인 numOfRows로 나눈 뒤, 올림

        if (pageNo == nPage):  # 만약 현재 페이지 번호가 총 페이지 개수와 같다면, 루프를 종료
            break

        pageNo += 1  # 현재 페이지 번호인 pageNo를 1 증가

    else:  # 위의 조건들을 만족하지 않을 경우, 루프를 종료
        break

    savedFilename = 'xx_ArpltnInforInqire.json'  # 저장할 파일 명 설정

    # jsonResult에 저장된 데이터를 JSON 형식으로 변환하여 파일에 저장
    # with 문을 사용 => 파일을 열고 사용한 후에 자동으로 닫히도록 보장
    with open(savedFilename, 'w', encoding='utf-8') as outfile:  # 파일을 쓰기 모드로 열기
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)  # jsonResult 리스트를 JSON 형식으로 변환
        # json.dumps() 함수를 사용하여 jsonResult를 JSON 문자열로 변환
        # indent 매개변수: 들여쓰기 칸 수 설정
        # sort_keys=True: 키를 기준으로 정렬
        # ensure_ascii=False: 유니코드 문자를 그대로 유지

        outfile.write(retJson)  # JSON 데이터를 파일에 쓰기

    print(savedFilename + ' file saved..')