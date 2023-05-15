from urllib.request import urlopen
from bs4 import BeautifulSoup

# urllib.request 모듈의 urlopen 함수를 사용
myurl = 'https://comic.naver.com/webtoon/weekday.naver' #주어진 URL로 HTTP 요청을 보냄
response = urlopen(myurl) #그 결과로 받은 응답을 나타내는 HTTPResponse 객체(response)를 생성

print(type(response))
# <class 'http.client.HTTPResponse'>

soup = BeautifulSoup(response, 'html.parser') #response로부터 받은 HTML 코드를 BeautifulSoup 객체로 만들어줌

title = soup.find('title').string #해당 웹페이지의 <title> 태그 내용을 찾음 -> 문자열로 저장
print(title)
# 네이버 웹툰
