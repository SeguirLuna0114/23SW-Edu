#외교부_국가 지역별 경제현황
import json, urllib.request, datetime, math
import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./`")))
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

#공공데이터포털에서 '외교부_국가·지역별 경제현황'데이터를 가져와 JSON 형식으로 저장
#https://apis.data.go.kr/1262000/OverviewEconomicService/OverviewEconomicList?serviceKey=3jrfQwF8GqsGiZXpzCOgPdESM%2FQAoErRSKH6LXfZK6%2BuKdPV%2F8bTS0ytNHnrs0vp4ve0DLHeRuMelVEUlPHDYQ%3D%3D&numOfRows=100&pageNo=1
def getEconomicServData(numOfRows, pageNo):
    # pageNo와 numOfRows을 매개변수로 받음
    end_point = 'https://apis.data.go.kr/1262000/OverviewEconomicService/OverviewEconomicList'

    # API 호출에 필요한 파라미터들을 저장하기 위함
    parameters = ''
    parameters += '?serviceKey=' + get_secret("data_apiKey")  # serviceKey는 비밀키를 설정
    parameters += '&numOfRows=' + str(numOfRows)  # 한 페이지 당 결과 개수
    parameters += '&pageNo=' + str(pageNo)  # 페이지 번호
    #parameters += '&cond[country_nm::EQ]=' + urllib.parser.quote(country_nm)  # 한글국가명
    #parameters += '&cond[country_iso_alp2::EQ]=' + str(country_iso_alp2)  # ISO 2자리코드

    #중국 : &cond[country_nm::EQ]=%EC%A4%91%EA%B5%AD&cond[country_iso_alp2::EQ]=CN

    # URL 생성: url 변수에 엔드포인트 URL과 파라미터를 조합하여 완전한 URL을 생성
    url = end_point + parameters
    print('\n URL')
    print(url)

    # getRequestUrl(url) 함수를 사용 => 생성한 URL로 API 요청을 보내고, 응답을 받음
    result = getRequestUrl(url)
    if (result == None):  # 응답이 None인 경우, None을 반환
        return None
    else:  # 응답이 None이 아닌 경우
        return json.loads(result)  # 응답을 JSON 형식으로 변환하여 반환

#파라미터의 값 설정
numOfRows = 100
pageNo = 1

#jsonData = getEconomicServData(numOfRows, pageNo)
#print(jsonData)

#빈 리스트 jsonResult를 생성합니다. 이 리스트는 모든 결과를 저장
jsonResult = []
nPage = 0
while(True):
    print('pageNo : %d, nPage : %d' % (pageNo, nPage))  # 현재 페이지 번호와 총 페이지 개수를 출력
    jsonData = getEconomicServData(numOfRows, pageNo)
    print(jsonData)

    if (jsonData['resultCode'] == 0):
        totalCount = jsonData['totalCount']
        print('데이터 총 개수 : ', totalCount)

        for item in jsonData['data']:
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

    # jsonResult에 저장된 데이터를 JSON 형식으로 변환하여 파일에 저장
    # with 문을 사용 => 파일을 열고 사용한 후에 자동으로 닫히도록 보장
    savedFilename = 'xx_OverviewEconomicService.json'  # 저장할 파일 명 설정
    with open(savedFilename, 'w', encoding='utf-8') as outfile:  # 파일을 쓰기 모드로 열기
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)  # jsonResult 리스트를 JSON 형식으로 변환
        # json.dumps() 함수를 사용하여 jsonResult를 JSON 문자열로 변환
        # indent 매개변수: 들여쓰기 칸 수 설정
        # sort_keys=True: 키를 기준으로 정렬
        # ensure_ascii=False: 유니코드 문자를 그대로 유지

        outfile.write(retJson)  # JSON 데이터를 파일에 쓰기

print(savedFilename + ' file saved..')