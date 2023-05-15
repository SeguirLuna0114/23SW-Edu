import re
from bs4 import BeautifulSoup

myencoding = 'utf-8'
myparser = 'html.parser'
filename = 'css01.html'

#css01.html 파일을 열어서 변수 html에 저장
html = open(filename, encoding=myencoding)
#html = open('css01.html', encoding="utf-8")과 같음

#html문서 파싱하여 파이썬에서 사용하기 쉬운 형태로 만들어주는 라이브러리
soup = BeautifulSoup(html, myparser)
#soup = BeautifulSoup(html, 'html.parser')과 같음

#CSS selector(선택자)를 활용한 태그 선택
#.select_one 메서드: CSS selector를 활용하여 하나의 요소를 선택
h1 = soup.select_one("div#cartoon > h1").string
# div#cartoon > h1: <div> 태그 중 id 속성값이 cartoon인 태그 하위에 위치한 첫번째 <h1> 태그를 선택
#.string: 문자열로 반환(<h1>좋아하는 만화</h1> -> 좋아하는 만화)
print("h1 =", h1)
# h1 = 좋아하는 만화

#CSS selector(선택자)를 활용한 태그 선택
#.select()메소드: CSS 선택자를 활용해 HTML 문서에서 원하는 태그 또는 속성 등을 선택 -> 해당 선택자에 해당하는 모든 요소들을 '리스트'로 반환
li_list = soup.select("div#cartoon > ul.elements > li")
# div#cartoon > ul.elements > li: html에서 div 태그 중 id 속성 값이 cartoon인 태그의 하위 태그 중(>) class 속성 값이 elements인 ul 태그의 하위 태그인(>) li 태그를 선택
for li in li_list: #li_list에 저장된 모든 li 태그를 순회하면서, 각 태그의 string 속성 값을 출력
    print("li =", li.string) #.string: 해당 태그의 텍스트 내용을 반환
    # li = 피구왕 통키
    # li = 미래 소년 코난
    # li = 로보트 태권 브이
print('-' * 50)

#lambda 함수를 이용
choice = lambda x : print(soup.select_one(x).string) #선택자(x)를 인자로 받아 select_one() 메소드를 호출, 해당 요소의 문자열 값(.string)을 출력하는 함수를 생성
# choice() 함수를 이용 => 해당 함수에 선택자를 전달
# soup.select_one()와 같은 결과를 출력

print('\nchoice("#item5") : ', end='')
choice("#item5") #전달된 선택자 #item5는 CSS 선택자로써, id가 'item5'인 요소의 문자열 값을 출력
# choice("#item5") : 똘이 장군

print('\nchoice("#item4") : ', end='')
choice("#item4") #전달된 선택자 #item4는 CSS 선택자로써, id가 'item4'인 요소의 텍스트를(문자열) 출력
# choice("#item4") : 들장미 소녀 캔디

print('\nchoice("ul > li#item3) : ', end='')
choice("ul > li#item3") #"ul" 태그 바로 아래에 있는(>) "li" 태그 중(#) "id" 속성이 "item3"인 태그의 텍스트를 출력
# choice("ul > li#item3) : 로보트 태권 V

print('\nchoice("li[id=\'item1\']") : ', end='') #'\': 따옴표(')나 쌍따옴표(")를 그대로 사용하기 위해 이스케이프 문자(\)사용
choice("li[id='item1']") # id 속성이 "item1"인 li 태그를 선택
#li[id='item1']에서 "li"는 태그 이름, id는 속성 이름, 그리고 'item1'은 속성 값
# choice("li[id='item1']") : 피구왕 통키

# CSS3의 'nth-of-type' 선택자
print('\nchoice("li:nth-of-type(4)") : ', end='')
choice("li:nth-of-type(4)") # ul 태그 내의 네 번째 li 태그를 선택
# soup.select_one("li:nth-of-type(4)") 와 동일한 결과를 출력
# choice("li:nth-of-type(4)") : 들장미 소녀 캔디

#oup.find_all("li"): HTML 코드에서 모든 <li> 태그를 찾아 리스트로 반환
print('\nchoice("li")[1].string : ', end='')
print(soup.find_all("li")[1].string) #[1]을 이용해 2번째 <li> 태그에 접근 -> 문자열로 반환(.string)
# choice("li")[1].string : 미래 소년 코난

print('\nchoice("li")[3].string : ', end='')
print(soup.find_all("li")[3].string)#[3]을 이용해 4번째 <li> 태그에 접근 -> 문자열로 반환(.string)
# choice("li")[3].string : 피구왕 통키
print('-' * 50)

mytag = soup.select_one('div#cartoon > ul.elements') #"div" 태그의(#) "id" 속성이 "cartoon"인 요소 아래에서(>, 하위요소 중에서) "class" 속성이 "elements"인 "ul" 태그를 선택
mystring = mytag.select_one('li:nth-of-type(3)').string #그 안에서 "li" 태그 중 3번째에 해당하는 요소의 문자열을 가져옴
print(mystring)
# 로보트 태권 브이
print('-' * 50)

mytag = soup.select_one('ul#itemlist') #"ul" 태그의(#) "id" 속성이 "itemlist"인 요소
mystring = mytag.select_one('li:nth-of-type(4)').string #그 안에서 "li" 태그 중 4번째에 해당하는 요소의 문자열을 가져옴
print(mystring)
# 들장미 소녀 캔디
print('-' * 50)

print(soup.select("#vegatables > li[class='us']")[0].string) # id가 "vegetables"인 ul 태그의 하위에(>) 위치한 class 속성 값이 "us"인(class='us') li 태그의 첫 번째 요소[0](인덱스0)를 선택 -> 문자열을 출력
# print(soup.select("#vegatables > li.us")[0].string)와 같은 출력
# 당근
print('-' * 50)

#print(soup.select("#vegatables > li[class='us']")[1].string)과 같은 출력
print(soup.select("#vegatables > li.us")[1].string) # id가 "vegetables"인 ul 태그의 하위에(>) 위치한 class 속성 값이 "us"인(.us) li 태그의 2번째 요소[1](인덱스1)를 선택 -> 문자열을 출력
# 호박
print('-' * 50)

#.select('a[href$="데이터"]'): href 속성 값의 끝($)이 "데이터"으로 끝나는 모든 a 태그 요소
result = soup.select('a[href$=".com"]') # href 속성 값의 끝($)이 ".com"으로 끝나는 모든 a 태그 요소를 선택 -> 리스트로 저장
for item in result: #리스트의 각 요소에서 href 속성 값을 추출하기 위해 반복문을 사용
    print(item['href'])
    # https://www.naver.com
    # http://www.google.com
    # http://www.abcd.com

#.select('a[href*="특정 문자열"]'): "href" 속성 값에 "특정 문자열"이 포함되어 있는 모든 링크를 선택하고 출력하는 코드
result = soup.select('a[href*="daum"]') # "href" 속성 값에 "daum"이라는 문자열이 포함되어 있는 모든 "a" 태그 요소를 선택-> 리스트 형태로 저장
for item in result:
    print(item['href'])
    # https://www.daum.net
print('-' * 50)

#딕셔너리를 활용하여 조건에 맞는 태그 찾는 find()함수
cond = {"id":"ko", "class":"cn"} #id 값이 ko 이고, class 값이 cn인 딕셔너리
print(soup.find("li", cond).string) #li 태그 중에서 id 값이 ko이고, class 값이 cn인 첫 번째 태그를 찾아 해당 태그 내용을 출력
# 가지
print('-' * 50)

print(soup.find(id="vegatables").find("li",cond).string)
#"vegetables"를 가진 id를 가진 태그를 찾은 후(id="vegatables"),
# 해당 태그 내에서 조건으로 주어진 딕셔너리(cond)에 맞는 li 태그를 찾아서(.find),
# 그 태그의 string 값을 출력(.string)
# 가지
print('-' * 50)

# soup.find_all() 메서드: 조건에 해당하는 '모든 요소'들을 찾아서 리스트로 반환
print("# 정규 표현식으로 href에서 https인 것 추출하기")
li = soup.find_all(href=re.compile(r"^https://"))
#href=re.compile(r"^https://"): href 속성 값이 "https://"로 시작하는 것을 찾기 위해 정규표현식을 사용

for e in li: #하나씩 가져와서
    print(e.attrs['href']) #href 속성 값을 출력
    # https://www.naver.com
    # https://www.daum.net
print('-' * 50)
print(soup.select("#fruits > li")[0].string)
# 감

mytag = soup.select_one('ul#fruits') #id 속성 값이(#) fruits인 ul 태그를 찾음 -> list형태로 반환
mystring = mytag.select_one("li:nth-of-type(2)").string #두 번째 li 태그를 선택.
#string 속성을 사용=> 해당 태그 안의 문자열을 가져와 출력
print(mystring)
# 밤

print('\n# finished')