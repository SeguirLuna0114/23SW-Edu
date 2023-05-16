#파이썬에서 사용되는 모듈 및 라이브러리 임포트
import time, datetime, ssl #시간관련 함수, 날짜와 시간을 다루는 클래스와 함수, Sssl(Secure Sockets Layer)프로토콜과 관련된 클래스와 함수 제공 모듈
import pandas as pd #데이터 분석과 조작을 위한 라이브러리
import urllib.request #URL을 열고 데이터 가져오는 기능 제공 모듈

#Selenium을 사용하여 웹 페이지를 자동으로 조작

from selenium import webdriver #웹 브라우저 자동으로 조작 가능
from selenium.webdriver.common.by import By #요소 탐색 방법을 지정하는데 사용
from bs4 import BeautifulSoup #HTML 또는 XML 문서를 파싱하기 위한 파이썬 라이브러리

#BeautifulSoup 객체를 생성할 때는 파싱할 문서와 파서 종류를 인자로 전달(html.parser)
#beautifulSoup 클래스를 사용하여 웹 페이지의 HTML을 파싱하는 ChickenStore 클래스 정의

class ChickenStore():
    myencoding = 'utf-8'  #클래스의 멤버 변수. 인코딩 방식을 나타내는 문자열

    def getWebDriver(self, cmdJavaScript): #getWebDriver 메서드: 자바스크립트 커맨드를 실행->실행 결과로 얻은 웹 페이지의 소스를 beautifulSoup 객체로 변환하여 반환
        # cmdJavaScript 매개변수: 문자열로 구성된 자바 스크립트 커맨드
        print(cmdJavaScript) #cmdJavaScript를 실행하기 전에 해당 커맨드 출력
        self.driver.execute_script(cmdJavaScript) #self.driver 객체의 execute_script 함수를 호출하여 cmdJavaScript를 실행
        # execute_script()함수: 자바스크립트 코드인 스크립트 형식으로 작동
        wait = 5 #wait 변수에 5를 할당
        # self.driver.implicitly_wait(wait)
        time.sleep(wait) #time.sleep()함수: 일정 시간동안(wait=5이기에, 5초동안) 대기한 후 페이지 소스를 얻음
        mypage = self.driver.page_source #self.driver 객체의 page_source 속성을 사용=> 현재 웹 페이지의 소스를 mypage 변수에 할당

        return BeautifulSoup(mypage, 'html.parser') #mypage 변수에 할당된 웹 페이지 소스를 BeautifulSoup 객체로 변환하여 반환.
        # 'html.parser': 파싱에 사용되는 파서의 종류를 나타냄

    def getSoup(self): #getSoup메서드: 현재 객체의 soup속성을 기반으로 BeautifulSoup객체를 생성하여 반환
        if self.soup == None: #객체의 soup속성=None인 경우(soup 속성이 설정되지 않은 경우)
            return None #None반환
        else: #self.soup != None(None이 아닌 경우)
            if self.brandName != 'pelicana': #brandName 속성이 'pelicana'가 아닌 경우
                return BeautifulSoup(self.soup, 'html.parser') #: self.soup을 BeautifulSoup 객체로 변환하여 반환
            else:  # #brandName 속성이 'pelicana'인 경우 # Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
                return BeautifulSoup(self.soup, 'html.parser') #self.soup을 BeautifulSoup 객체로 변환하여 반환(현재의 soup 속성을 파싱)
                # return BeautifulSoup(self.soup, 'html.parser', from_encoding="iso-8859-1") #from_encoding 인자를 추가=>인코딩 지정('iso-8859-1' 인코딩)

    def get_request_url(self): #get_request_url 메서드: 해당 객체의 url 속성을 기반으로 HTTP 요청을 보내고, 응답을 받음
        request = urllib.request.Request(self.url) #urllib.request.Request 함수를 사용=> HTTP 요청 객체를 생성
        try: #예외처리 시작
            context = ssl._create_unverified_context() #ssl._create_unverified_context() 함수를 호출 => (인증서 검증 없이) SSL 연결을 위한 context를 생성
            response = urllib.request.urlopen(request, context=context) #urllib.request.urlopen 함수를 호출=> HTTP 요청을 보내고, 응답을 받음.
            # context: SSL 연결을 위함
            if response.getcode() == 200: #응답의 상태 코드가 200인 경우(응답이 성공적인 경우)
                # print('[%s] url request success' % datetime.datetime.now())

                if self.brandName != 'pelicana': #brandName 속성이 'pelicana'이 아닌 경우
                    return response.read().decode(self.myencoding) #response.read()함수: 응답데이터를 가져옴
                      #self.myencoding에 지정된 인코딩을 사용하여 디코딩
                else: ##brandName 속성이 'pelicana'인 경우
                    return response #응답객체 자체를 그대로 반환

        except Exception as err: #Exception 클래스: 모든 예외를 다룸
            print(err) #err변수: 발생한 예외 객체
            now = datetime.datetime.now() #현재 시간을 now 변수에 할당(에러메시지에 현재시간 포함시키기 위함)
            msg = '[%s] error for url %s' % (now, self.url) #에러메시지 생성: %s 포맷 문자열을 사용=>현재 시간(now)과 self.url 속성을 메시지에 포함
            print(msg) #에러 메시지 출력
            return None #예외 처리가 완료되면 None을 반환

    def save2Csv(self, result): #save2Csv 메서드: 결과 데이터(result)를 받아와서 DataFrame으로 변환 -> CSV 파일로 저장
        data = pd.DataFrame(result, columns=self.mycolumns) #result(결과 데이터)를 기반으로 DataFrame 생성
        data.to_csv(self.brandName + '.csv', \
                    encoding=self.myencoding, index=True) #DataFrame 객체인 data를 CSV 파일로 저장(파일명: self.brandName + '.csv')

    def __init__(self, brandName, url): #__init__메서드: 초기화 메서드는 객체가 생성될 때 호출되며, 초기화 작업을 수행
        #매개변수를 받아와서 현재객체(self.)의 속성에 할당
        self.brandName = brandName
        self.url = url

        self.mycolumns = ['brand', 'store', 'sido', 'gungu', 'address'] #기본 column 추가(공통으로 사용되는 column)

        if self.brandName in ['pelicana']: #현재 객체의 brandName이 'pelicana'과 일치하는 경우(pelicana 브랜드인 경우)
            self.mycolumns.append('phone') #self.mycolumns 리스트에 'phone' 컬럼을 추가

        elif self.brandName in ['nene', 'cheogajip', 'goobne']: #brandName이 'nene', 'cheogajip', 'goobne' 중 하나와 일치하는 경우
            self.mycolumns.append('phone') #self.mycolumns 리스트에 'phone' 컬럼을 추가

        else:
            pass # 아무 작업도 수행하지 않음

        if self.brandName != 'goobne': #goobne' 브랜드가 아닌 경우
            self.soup = self.get_request_url() #get_request_url 메서드를 호출 => 웹 페이지의 소스를 가져옴 -> 현재 객체의 soup 속성에 할당(BeautifulSoup 객체로 변환된 웹 페이지 소스 의미)
            self.driver = None #self.driver 속성을 None으로 초기화
        else:  #goobne' 브랜드인 경우
            self.soup = None # 웹 페이지 소스를 가져오지 않음
            filepath = 'C:/Users/USER/Downloads/chromedriver_win32/chromedriver.exe' #Chrome 드라이버 파일의 경로를 filepath 변수에 할당(in Windows 운영체제)
            # filepath = '/Users/lune/chromedriver_mac64/chromedriver'
            self.driver = webdriver.Chrome(filepath) #chrome 드라이버를 사용(in filepath)하여 웹 드라이버 객체 생성 => 웹 페이지를 조작
            self.driver.get(self.url) #웹 드라이버 객체의 get메서드를 호출하여 self.url에 지정된 url로 이동 -> chrome 브라우저를 열고 해당 url 로드
        print('생성자 호출됨')
# end class ChickenStore()
