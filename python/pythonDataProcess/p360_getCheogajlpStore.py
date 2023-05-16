from itertools import count # count() 함수를 사용 => (0부터 시작하여 1씩 증가하는 값으로 이루어진)무한한 숫자 시퀀스 생성
from p340_ChickenUtil import ChickenStore #chickenStore 클래스를 import

brandName = 'cheogajip'
base_url = 'https://www.cheogajip.co.kr/bbs/board.php'

def getData(): #getData함수 정의: 크롤링 작업을 수행(상점 정보를 추출하여 리스트에 저장, 모든 상점정보 가져온 후 csv파일로 저장)
    savedData = [] #savedData라는 빈 리스트를 초기화(추출한 데이터를 저장할 공간)

    for page_idx in count(): # count() 함수를 사용 => 무한 루프를 통해 각 페이지의 url을 생성
        #count() 함수: 반복 가능한 객체에서 값을 하나씩 가져옴
        if page_idx >= 124:
            chknStore.save2Csv(savedData)
            break
        else:
            # 각 페이지의 URL 생성
            url = base_url
            url += '&page=%s' % str(page_idx+1) #base_url에 페이지 번호를 추가('?page=')하여 url생성.
            # print( url )

            # ChickenStore 객체를 생성 => 해당 페이지의 HTML 소스 가져옴
            chknStore = ChickenStore(brandName, url)
            soup = chknStore.getSoup()

            mytbody = soup.find('tbody') #그 안의 tbody를 가져옴
            # print(mytbody)

            shopExists = False #shopExists 변수를 False로 초기화
            for mytr in mytbody.findAll('tr'): #mytbody 변수에 저장된 테이블 요소에서 각각의 행 (<tr>)을 순회
                shopExists = True #상점 정보가 하나 이상 존재하므로, shopExists 변수를 True로 설정
                mylist = list(mytr.strings) #현재 행에서 모든 문자열을 추출하여 리스트로 변환
                print(mylist)

                store = mylist[1] #2번째 요소를 상점 이름
                address = mylist[3] #4번째 요소를 주소로 설정
                phone = mylist[5] #6번째 요소를 번호로 설정

                if len(address) >= 2: #주소의 길이가 2 이상
                    imsi = address.split() #공백을 기준으로 주소 분리
                    sido = imsi[0] #1번째 요소 = 시/도
                    gungu = imsi[1] #2번째 요소 = 군/구

                mydata = [brandName, store, sido, gungu, address, phone] #추출한 정보를 리스트 형태로 저장
                print(mydata)
                savedData.append(mydata) #추출한 상점 정보를 saveData리스트에 추가

print(brandName + ' 매장 크롤링 시작')
getData()
print(brandName + ' 매장 크롤링 끝')