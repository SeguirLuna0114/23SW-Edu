import urllib.request, datetime, math, json
import pandas as pd
import xml.etree.ElementTree as ET
import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
#os.path.relpath("./")는 현재 스크립트 파일의 상대 경로를 반환
#os.path.dirname()을 두 번 호출하여 상위 디렉토리 경로를 얻음

#os.path.join() 함수: 경로를 결합
secret_file = os.path.join(BASE_DIR, '../secret.json') #BASE_DIR과 '../secret.json'을 결합하여 비밀 파일의 경로를 생성

#with 문을 사용 => 파일을 열고 사용한 후에 자동으로 닫히도록 보장
with open(secret_file) as f:
    secrets = json.loads(f.read()) #json.loads() 함수를 사용하여 JSON 문자열을 파싱하고 파이썬객체로 변환

def get_secret(setting, secrets=secrets): #설정 값을 가져오기 위해 secrets 딕셔너리를 참조하는 함수 정의
    # setting 매개변수로 설정 값을 지정하고, 기본값으로 secrets 변수를 사용
    try: #secrets 딕셔너리에서 setting에 해당하는 값을 가져오려 시도
        return secrets[setting] #secrets 딕셔너리에서 setting에 해당하는 값을 반환
    except KeyError: #KeyError 예외가 발생
        #setting에 해당하는 환경 변수를 설정하라는 오류 메시지를 반환
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

def getRequestUrl(url): #주어진 URL에 HTTP 요청을 보내고, 성공적인 응답을 받아서 문자열로 반환
    #url을 매개변수로 받음
    req = urllib.request.Request(url)
    
     try:
        #urllib.request.urlopen() 함수: 요청 객체 req를 서버로 보내고, 서버로부터의 응답을 받음
        response = urllib.request.urlopen(req)
        
        if response.getcode() == 200: #성공적인 HTTP 요청인 경우
            return response.read().decode('utf-8') #response.read()는 응답의 내용을 바이트로 읽어옴, 바이트를 UTF-8 문자열로 디코딩하여 반환
    
    except Exception as e: #예외가 발생
        # print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url)) #오류 메시지를 출력
        return None #None을 반환

#공공데이터포털에서 'ulsanBicycle'데이터를 가져와 CSV 로 저장
def getBicycleData(pageNo, numOfRows):
    end_point = 'http://apis.data.go.kr/6310000/ulsanbicyclepath/getUlsanbicyclepathList' #데이터를 가져올 API의 엔드포인트 URL

    #API 호출에 필요한 파라미터들을 저장하기 위함
    parameters = '?'
    parameters += "ServiceKey=" + get_secret("data_apiKey") #serviceKey는 비밀키를 설정
    parameters += "&pageNo=" + str(pageNo) #페이지 번호
    parameters += "&numOfRows=" + str(numOfRows) #한 페이지 당 결과 개수
    #URL 생성: url 변수에 엔드포인트 URL과 파라미터를 조합하여 완전한 URL을 생성
    url = end_point + parameters

    print('URL')
    print(url)

    #getRequestUrl(url) 함수를 사용하여 생성한 URL로 API 요청을 보내고, 응답을 받음
    result = getRequestUrl(url)
    if (result == None): # 응답이 None인 경우, None을 반환
        return None
    else: # 응답이 None이 아닌 경우
        return result #응답을 반환

#빈 리스트 dataList를 생성합니다. 이 리스트는 모든 결과를 저장
dataList = []

#파라미터의 값 설정
pageNo = 1 
numOfRows = 2 
nPage = 0

while(True): #무한루프(XML 데이터를 가져와서 처리)
    print('pageNo : %d, nPage : %d' % (pageNo, nPage)) #현재 페이지 번호와 총 페이지 개수 출력
    xmlData = getBicycleData(pageNo, numOfRows) #getBicycleData(pageNo, numOfRows) 함수를 호출하여 XML 데이터를 가져옴
    print(xmlData)
    
    #ET.fromstring(xmlData)를 사용하여 XML 데이터를 파싱하여 XML 트리를 생성
    xmlTree = ET.fromstring(xmlData)

    #결과 메시지 확인
    if (xmlTree.find('header').find('resultMsg').text == 'success'): #header 요소의 resultMsg 값을 확인하여 데이터를 성공적으로 가져왔는지 확인
        #데이터 개수 확인
        totalCount = int(xmlTree.find('body').find('totalCount').text) #XML트리에서 body 요소의 totalCount 값을 저장
        print('데이터 총 개수 : ', totalCount) #데이터 총 개수 출력

        #리스트 요소 처리
        listTree = xmlTree.find('body').find('data').findall('list') #XML 트리에서 body 요소의 data 요소의 모든 list 요소를 찾아 저장
        print(listTree)

        for node in listTree: #리스트 요소를 순회(listTree를 순회하면서 각 요소를 node에 할당)
            #node.find(): 각 node에서 필요한 데이터를 추출
            bikeFirstLanes = node.find("bikeFirstLanes").text #node에서 "bikeFirstLanes" 요소의 텍스트 값 가져옴
            bikeFirstLanesRatio = node.find("bikeFirstLanesRatio").text
            bikeLanesRatio = node.find("bikeLanesRatio").text
            
            bikeOnlyLanes = node.find("bikeOnlyLanes") #node에서 "bikeOnlyLanes" 요소를 찾음
            if bikeOnlyLanes == None : #값이 없을 경우
                bikeOnlyLanes = "" #빈 문자열로 설정
            else : #값이 있을 경우
                bikeOnlyLanes = bikeOnlyLanes.text #텍스트값을 가져옴
                
            bikeOnlyLanesRatio = node.find("bikeOnlyLanesRatio").text #node에서 "bikeOnlyLanesRatio" 요소의 텍스트 값을 가져옴
            cycleRoute = node.find("cycleRoute").text
            entId = node.find("entId").text
            gugun = node.find("gugun").text
            pedestrianBikeLanes = node.find("pedestrianBikeLanes").text
            pedestrianBikeLanesRatio = node.find("pedestrianBikeLanesRatio").text

            #추출한 데이터를 사용하여 onedict라는 딕셔너리를 생성
            onedict = {'자전거우선도로':bikeFirstLanes, \
                       '자전거우선도로비율':bikeFirstLanesRatio, '자전거전용도로비율':bikeLanesRatio, \
                       '자전거전용차로':bikeOnlyLanes, '자전거전용차로비율':bikeOnlyLanesRatio, \
                       '자전거전용도로':cycleRoute, '고유번호':entId, '군구':gugun, \
                       '자전거보행자겸용도로':pedestrianBikeLanes, '자전거보행자겸용도로비율':pedestrianBikeLanesRatio}
            
            dataList.append(onedict) #onedict를 dataList에 추가

        if totalCount == 0:#데이터의 총 개수가 0인 경우(데이터가 더이상 없는 경우), 루프를 종료
            break
        
        #총 페이지 개수 계산
        nPage = math.ceil(totalCount / numOfRows) #한 페이지당 결과 개수인 numOfRows로 나눈 뒤, 올림
        
        if (pageNo == nPage):#만약 현재 페이지 번호가 총 페이지 개수와 같다면, 루프를 종료
            break 

        pageNo += 1#현재 페이지 번호인 pageNo를 1 증가
        
    else : #위의 조건들을 만족하지 않을 경우, 루프를 종료
        break

savedFilename = 'xx_ulsanByke.csv' #저장할 파일 명 설정

#pd.DataFrame(): 데이터 프레임 생성
#.to_csv(savedFilename) 메서드 => 데이터프레임을 CSV파일로 저장
myframe = pd.DataFrame(dataList) #dataList를 사용하여 myframe 데이터프레임을 생성
myframe.to_csv(savedFilename) # 데이터프레임을 CSV 파일로 저장

print(savedFilename + ' file saved..')
