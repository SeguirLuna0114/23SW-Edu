import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pandas import DataFrame

#soup 객체에 myurl 웹페이지를 분석한 결과 저장 => soup 객체를 활용해서 웹페이지에서 원하는 정보를 추출하거나 조작 가능
myparser = 'html.parser'
myurl = 'https://comic.naver.com/webtoon/weekday.nhn'
response = urlopen(myurl)
soup = BeautifulSoup(response, myparser)
# soup = BeautifulSoup(response, 'html.parser')와 같음

weekday_dict = {'mon': '월요일', 'tue': '화요일', 'wed': '수요일',
                'thu': '목요일', 'fri': '금요일', 'sat': '토요일',
                'sun': '일요일'} #요일별 웹툰 목록 페이지의 URL에서 요일을 나타내는 영문 축약어와 한글 요일명 간의 대응 관계를 나타내는 딕셔너리
myfolder = './imsi' #다운로드 받은 이미지 파일들을 저장할 폴더의 경로를 지정

#os.path.exists(path) 함수: 주어진 경로(path)가 존재하는지 여부를 확인
# 경로가 존재하면 True를 반환하고, 경로가 존재하지 않으면 False를 반환. 파일 또는 디렉토리의 존재 여부를 확인하는 데 사용됨.
try:
    if not os.path.exists(myfolder): #myfolder 경로('./imsi')가 존재하지 않는 경우
        os.mkdir(myfolder) #myfolder 경로('./imsi') 새로생성
    for mydir in weekday_dict.values(): #딕셔너리의 값들(요일 이름)을 반복
        mypath = myfolder + mydir #해당 이름을 가진 하위 디렉토리를 myfolder 경로에 생성
        if os.path.exists(mypath): #이미 해당 디렉토리가 존재하는 경우
            pass #아무 일도 하지 않음
        else: #존재하지 않는 경우
            os.mkdir(mypath) #mypath 경로 생성(./imsi/월요일, ./imsi/화요일, ... 등의 하위 디렉토리를 생성)
except FileExistsError as err: #FileExistsError 예외가 발생한 경우
    pass #아무 일도 하지 않음

# 이미지 URL, 요일(한글), 제목을 받아 해당 요일 디렉토리에 해당 제목으로 된 jpg 파일을 생성하는 함수
def saveFile(mysrc, myweekday, mytitle):
    image_file = urlopen(mysrc) #mysrc 로부터 이미지를 열어 image_file 객체에 저장
    filename = myfolder + myweekday + '\\' + mytitle + '.jpg' #해당 요일의 디렉토리와 제목을 이용하여 파일 이름을 생성
    myfile = open(filename, mode='wb') #filename 경로에 파일을 생성하고 wb 모드로 파일을 열기
    myfile.write(image_file.read()) #image_file 객체에서 이미지를 읽어 myfile 에 쓰고 파일을 저장

mytarget = soup.find_all('div', attrs={'class': 'thumb'}) # div 태그 중 class 속성이 'thumb'인 요소들을 모두 찾아 mytarget에 저장
print('만화 총 개수 : %d' % (len(mytarget))) #len()을 이용하여 해당 요소의 개수를 출력
# 만화 총 개수 : 0

# mytarget에 저장된 요소들을 순회하면서 필요한 정보를 추출 -> mylist에 추가 -> 해당 이미지파일 다운로드
mylist = []
for abcd in mytarget: #mytarget에 저장된 요소들을 하나씩 순회
    myhref = abcd.find('a').attrs['href'] #해당 요소에서 a 태그를 찾고, 그 href 속성 값을 가져옴
    myhref = myhref.replace('./webtoon/list.nhn?', '') #myhref 문자열에서 './webtoon/list.nhn?' 부분을 공백으로 대체(제거와 같은 의미)
    result = myhref.split('&') #myhref 문자열을 '&' 기준으로 분리 -> 리스트로 저장
    mytitleid = result[0].split('=')[1] #result 리스트의 1번째 요소에서 '='을 기준으로 분리하여 2번째 값 가져옴
    myweekday = result[1].split('=')[1] #result 리스트의 2번째 요소에서 '='을 기준으로 분리하여 2번째 값 가져옴
    myweekday = weekday_dict[myweekday] #myweekday 값을 weekday_dict 딕셔너리를 사용 => 한글요일로 변환

    imgtag = abcd.find('img') #해당요소에서 img태그 찾음
    mysrc = imgtag.attrs['src'] #img 태그의 src 속성 값
    mytitle = imgtag.attrs['title'].strip() #img 태그의 title 속성 값 가져옴. #.strip(): 문자열 양쪽의 공백을 제거
    mytitle = mytitle.replace('?', '').replace(':', '') #mytitle 문자열에서 '?'와 ':' 문자를 제거(''공백으로 대체=제거 와 같은 의미)

    mytuple = tuple([mytitleid, myweekday, mytitle, mysrc]) #필요한 정보들을 튜플로 묶음
    mylist.append(mytuple) #mylist에 튜플을 추가

    saveFile(mysrc, myweekday, mytitle) #이미지 파일을 다운로드하여 저장

print(mylist)

myframe = DataFrame(mylist, columns=['타이틀 번호', '요일', '제목', '링크'])
filename = 'cartoon.csv'
myframe.to_csv(filename, encoding='utf-8', index=False)
print(filename, ' saved....')
print('\n# finished.')
