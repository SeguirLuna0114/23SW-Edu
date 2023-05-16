import folium, requests #주소 정보를 검색
import os.path
import json #JSON 데이터를 다룰 수 있도록 준비

address = '서울 마포구 신수동 451번지 세양청마루아파트 상가 101호'
url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address #Kakao Maps API의 주소 검색 기능을 활용하기 위한 요청 URL을 생성. 기본 url에 검색할 주소를 쿼리 파라미터(/address.json?query=')로 추가

#현재 스크립트 파일의 기준 디렉토리를 가져옴
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
#secret.json 파일(API키와 같은 비밀 정보가 저장됨)의 경로 설정
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
    r = requests.get(url, headers=header) #request.get(): http get 요청을 보냄

    if r.status_code == 200: #요청이 성공적으로 처리될 경우
        try: #예외 발생 시
            result_address = r.json()["documents"][0]["address"] #응답 데이터를 JSON 형식으로 파싱하여 주소 정보를 추출. 주소정보는 documents 배열의 첫번째 요소에 있는 address객체
            result = result_address["y"], result_address["x"] #주소 정보에서 위도와 경도 값을 추출하여 result변수에 할당. 위도(y), 경도(x)
        except Exception as err: #예외가 발생하는 경우(Exception 블록)
            return None #None을 반환하여 함수의 실행이 중단됨
    else: #요청이 실패한 경우->에러메시지 출력
        result = "ERROR[" + str(r.status_code) + "]"

    return result

address_latlng = getGeocoder(address) #getGeocoder()함수를 호출하여 주소(address)의 위도와 경도값을 얻어옴
latitude = address_latlng[0] #위도값 할당
longitude = address_latlng[1] #경도값 할당

print('주소지 :', address)
print('위도 :', latitude)
print('경도 :', longitude)

shopinfo = '교촌 신수점'
#folium.Map() 클래스 => foli_map 생성
foli_map = folium.Map(location=[latitude, longitude], zoom_start=17)
#location옵션: 위도와 경도값을 전달하여, 지도의 중심 위치를 설정
#zoom_start: 초기 확대수준을 설정

#folium.Icon() 클래스 => myicon변수 생성
myicon = folium.Icon(color='red', icon='info-sign')
#icon옵션: icon모양을 설정(이 경우, info-sign(정보 표시)아이콘)

#folium.Marker() 클래스 => 지도에 마커(folium.Marker)를 추가
folium.Marker([latitude, longitude], popup=shopinfo, icon=myicon).add_to(foli_map)
#첫번째 변수=location옵션: 위도와 경도값을 전달하여 마커의 위치 설정
#popup 옵션: 마커를 클릭했을 때 나타날 팝업 텍스트를 설정
#icon 옵션: myicon변수를 전달하여 마커의 아이콘을 설정
#.add_to(foli_map): 생성한 마커를 foli_map에 추가

#folium.CircleMarker()클래스 => 지도에 원형마커 추가
folium.CircleMarker([latitude, longitude], radius=300, color='blue', fill_color='red', fill=False, popup=shopinfo).add_to(foli_map)
#location 옵션에는 위도와 경도 값을 전달하여 마커의 위치를 설정
#radius 옵션: 원의 반지름을 설정(여기서는 300)
#color 옵션: 원의 테두리 색상을 설정
#fill_color옵션: 원의 내부를 채우는 색상 설정
#fill 옵션: 원의 내부를 채울지 여부 결정
#popup 옵션: 마커를 클릭했을 때 나타날 팝업 텍스트를 설정
#.add_to(foli_map): 생성한 마커를 foli_map에 추가

foli_map.save('./xx_shopmap.html')
print('file saved...')