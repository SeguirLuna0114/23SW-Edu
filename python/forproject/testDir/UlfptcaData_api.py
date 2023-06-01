import requests
import json, urllib.request, math
import pandas as pd
from datetime import datetime, timedelta
from fastapi import FastAPI, Query
import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, '../secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
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

app = FastAPI()

@app.get('/getUlfptcaAlarmInfo')
async def getUlfptcaAlarmInfo(year: str = Query(..., description="측정연도를 입력하세요(ex.YYYY or all)")):
    # 파라미터의 값 설정
    data_list = []  # 모든 데이터를 저장할 리스트

    if year == 'all':
        for year_data in range(2018, 2024):
            end_point = 'https://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo'
            parameters = ''
            parameters += '?serviceKey=' + get_secret("data_apiKey")
            parameters += '&returnType=json'
            parameters += '&numOfRows=100'
            parameters += '&pageNo=1'
            parameters += '&year=' + str(year_data)
            url = end_point + parameters

            response = requests.get(url)
            print(response)
            print('-' * 50)
            result_toJSON = response.json()
            data_list.extend(result_toJSON['response']['body']['items'])
        return data_list

    else:  # 단일연도
        year = int(year)
        end_point = 'https://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo'
        parameters = ''
        parameters += '?serviceKey=' + get_secret("data_apiKey")
        parameters += '&returnType=json'
        parameters += '&numOfRows=' + str(numOfRows)
        parameters += '&pageNo=' + str(pageNo)
        parameters += '&year=' + str(year)
        url = end_point + parameters

        response = requests.get(url)
        result_toJSON = response.json()
        return result_toJSON['response']['body']['items']