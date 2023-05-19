#한국환경공단_에어코리아_대기오염
import json, urllib.request, datetime, math
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
def getMinuDustFrcstDspth(numOfRows, pageNo, searchDate):
    # pageNo와 numOfRows, sidoName을 매개변수로 받음
    end_point = 'https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMinuDustFrcstDspth'

    # API 호출에 필요한 파라미터들을 저장하기 위함
    parameters = ''
    parameters += '?serviceKey=' + get_secret("data_apiKey")  # serviceKey는 비밀키를 설정
    parameters += '&returnType=json'  # JSON 형식으로 요청
    parameters += '&numOfRows=' + str(numOfRows) # 한 페이지 당 결과 개수
    parameters += '&pageNo=' + str(pageNo) # 페이지 번호
    parameters += '&searchDate=' + str(searchDate) #통보시간 검색(조회 날짜 입력이 없을 경우 한달동안 예보통보 발령 날짜의 리스트 정보를 확인)
    #parameters += '&InformCode' + str(InformCode) #통보코드검색(PM10, PM25, O3)

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
pageNo = 1
numOfRows = 100

#searchDate 입력변수 정의
inputDate = input('조회 날짜를 입력하세요 (ex. YYYY-MM-DD) : ')
if inputDate is None:
    # 조회 날짜 입력이 없을 경우 한달동안 예보통보 발령 날짜의 리스트 정보를 확인
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=30)
    EndDate = end_date.strftime("%Y%m%d")

    searchDate = start_date + "-" + end_date.strftime("%Y%m%d")

    print(searchDate)
else:
    searchDate = inputDate



#jsonData = getMinuDustFrcstDspth(numOfRows, pageNo, searchDate)
#print(jsonData)