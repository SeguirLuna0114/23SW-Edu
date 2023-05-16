import folium, requests #주소 정보를 검색
import os.path
import json #JSON 데이터를 다룰 수 있도록 준비
import pandas as pd

#카카오맵 API를 사용하여 주소를 검색하기 위한 URL의 헤더 부분을 저장
url_header = 'https://dapi.kakao.com/v2/local/search/address.json?query=' #url의 주어진 주소 기반으로 해당 지리정보 검색에 사용

#현재 스크립트 파일의 기준 디렉토리를 가져옴
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, '../secret.json')

with open(secret_file) as f: #secret.json 파일을 열어서 해당 정보 사용하는 부분
    secrets = json.loads(f.read()) #JSON 형식으로 파싱하여 secrets 변수에 저장 => 저장된 비밀 정보를 사용할 수 있음

def get_secret(setting, secrets=secrets): #get_secret함수: setting 매개변수에 해당하는 비밀 정보를 반환
    #secrets=secrets: secret 매개변수에 기본값으로 secret변수 설정 => 전역변수로 사용되지 않더라도 함수 내 접근 가능하도록 함
    try:
        return secrets[setting] #secret 딕셔너리에서 setting에 해당하는 값을 반환. 즉 setting은 비밀정보의 key를 의미
    except KeyError:
        errorMsg = "Set the {} environment variable".format(setting)
        raise errorMsg

#HTTP 요청 헤더에  Authorization 필드 설정
header = {'Authorization': 'KakaoAK ' + get_secret("kakao_apiKey")} #kakao Maps API의 인증키를 사용하여 헤더값 설정 & kakao_apiKey라는 비밀 정보를 가져옴

def getGeocoder(address): #getGeocoder: 주소(address)를 받아와서 해당 주소의 지리정보(Geocoder)를 반환
    result = "" #result 변수를 빈 문자열로 초기화
    url = url_header + address #url 변수를 생성하여 url_header와 주소(address)를 조합한 값을 할당
    r = requests.get(url, headers=header) #request.get(): http get 요청을 보냄

    if r.status_code == 200: #요청이 성공적으로 처리될 경우
        try: #예외 발생 시
            result_address = r.json()["documents"][0]["address"] #응답 데이터를 JSON 형식으로 파싱하여 주소 정보를 추출. 주소정보는 documents 배열의 첫번째 요소에 있는 address객체
            result = result_address["y"], result_address["x"] #주소 정보에서 위도와 경도 값을 추출하여 result변수에 할당. 위도(y), 경도(x)
        except Exception as err: #Exception 블록:예외가 발생하는 경우(JSON파싱이 실패하거나 주소정보가 없는 경우)
            return None #None을 반환하여 함수의 실행이 중단됨
    else: #요청이 실패한 경우(응답코드가 200이 아닌 경우)->에러메시지 출력
        result = "ERROR[" + str(r.status_code) + "]"

    return result #result값 반환하여 지리정보 얻음

def makeMap(brand, store, getInfo): #지도에 마커 생성 함수
    shopinfo = store + '(' + brand_dict[brand] + ')' #상점과 브랜드 정보를 조합하여 문자열로 저장
    mycolor = brand_color[brand] #brand_color 딕셔너리를 사용하여 브랜드에 대응하는 색상을 찾음
    latitude, longitude = float(getInfo[0]), float(getInfo[1]) #getInfo를 위도와 경도 정보를 갖는 리스트라고 가정 -> 값을 각각 변수에 할당(데이터타입 float)

    #folium.Marker()생성
    marker = folium.Marker([latitude, longitude], popup=shopinfo, icon=folium.Icon(color=mycolor, icon='info-sign')).add_to((mapObject)) #shopinfo를 팝업메시지로 표시
    #folium.Icon()함수를 사용하여 색상과 아이콘을 지정
    #.add_to((mapObject)): 생성된 마커를 mapObject에 추가

mylatitude = 37.4946203470469
mylongitude = 127.027606136235
#folium.Map()함수 =>지도객체 생성
mapObject = folium.Map(location=[mylatitude, mylongitude], zoom_start=13) #중심위치는 지정한 위도와 경도로 설정.  초기 지도의 확대/축소 수준 13정도로 설정

brand_dict = {'cheogajip' : '처갓집', 'pelicana' : '페리카나'} # 브랜드 코드와 이름을 매핑하는 딕셔너리
brand_color = {'cheogajip' : 'red', 'pelicana' : 'blue'} #브랜드 코드와 마커색상을 매핑하는 딕셔너리

csvfile ='ChickenResult.csv'
#pd.read_csv()함수를 활용하여 csv파일을 읽고 데이터프레임 형태로 저장
myframe = pd.read_csv(csvfile, index_col=0, encoding='utf-8') #index_col=0: 첫번째 열을 index로 설정

where = '강남구' #검색할 지역 설정
brandName = 'cheogajip' #검색할 브랜드 설정
condition1 = myframe['gungu'] == where #시군구 열이 where와 일치하는 조건을 만족하는지 확인(조건식)
condition2 = myframe['brand'] == brandName #브랜드 열이 brandname과 일치하는지 확인하는 조건식
mapData01 = myframe.loc[condition1 & condition2] #데이터프레임에서 조건1과 2를 모두(&) 만족하는 행을 선택하여 저장한 변수

brandName = 'pelicana' #검색할 브랜드 설정
condition1 = myframe['gungu'] == where #시군구 열이 where와 일치하는 조건을 만족하는지 확인(조건식)
condition2 = myframe['brand'] == brandName #브랜드 열이 brandname과 일치하는지 확인하는 조건식
mapData02 = myframe.loc[condition1 & condition2] #데이터프레임에서 조건1과 2를 모두(&) 만족하는 행을 선택하여 저장한 변수

mylist =[]
mylist.append(mapData01)
mylist.append(mapData02)

mapData = pd.concat(mylist, axis=0) #mylist에 추가된 데이터프레임들을 수직으로 결합(axis=0)하여 mapData라는 데이터프레임 생성

#ok, notok 변수 초기화
ok = 0
notok = 0
for idx in range(len(mapData.index)): #각 행을 반복하면서 브랜드, 가게이름, 주소 추출
    brand = mapData.iloc[idx]['brand']
    store = mapData.iloc[idx]['store']
    address = mapData.iloc[idx]['address']
    getInfo = getGeocoder(address) #주소를 getGeocoder 함수에 전달하여 해당 주소의 지리정보를 가져옴

    if getInfo == None: #가져온 지리정보가 없는 경우
        print("Not OK : " + address)
        notok +=1
    else: #가져온 지리정보가 None이 아닌 경우
        print("OK : " + address)
        ok += 1
        makeMap(brand, store, getInfo) #makeMap 함수를 호출하여 브랜드, 가게 이름, 지리정보를 기반으로 지도에 마커를 추가
    print('%' * 40)

total = ok + notok #total 변수에 ok와 notok를 더한 값을 저장
print('ok : ', ok)
print('Not ok : ', notok)
print('total : ', total)

filename = 'xx_chickenMap.html'
mapObject.save(filename)
print('file saved...')
