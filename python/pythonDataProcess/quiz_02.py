import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic' #Matplotlib의 기본 글꼴을 'Malgun Gothic'으로 설정

#urlopen 함수: 주어진 URL에서 HTML 페이지를 가져옴
url = "https://movie.daum.net/ranking/reservation"
#urllib.request.urlopen(url): 주어진 URL에 HTTP 요청을 보내고, 해당 페이지의 HTML 데이터를 가져옴
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser') # HTML 데이터를 파싱하여 BeautifulSoup 객체를 생성

#.findAll(): 특정 요소를 모두 찾는 예제
infos = soup.findAll('div', attrs={'class':'thumb_cont'}) #soup에서 div 요소 중 class 속성 값이 'thumb_cont'인 모든 요소를 찾음
# print('-' * 40)
print(infos)
# [<div class="thumb_cont">
# <strong class="tit_item">
# <a class="link_txt" data-tiara-layer="moviename" href="/moviedb/main?movieId=167558">분노의 질주: 라이드 오어 다이</a>
# ...
# </div>, <div class="thumb_cont">
# <strong class="tit_item">
# ...
print('-' * 40)

no = 0 #각 요소의 순번을 나타내기 위한 변수
result = [] #추출된 데이터를 추가하기 위한 빈 리스트 생성
for info in infos: #infos 리스트에 있는 각 요소들을 순회하면서 필요한 정보를 추출
    no += 1
    #info.find('특정 클래스', attrs='요소'): info 요소에서 특정 클래스를 가진 하위 요소를 찾음
    mytitle = info.find('a', attrs={'class':'link_txt'})
    title = mytitle.string #.string => 텍스트(문자열)로 변환

    mygrade = info.find('span', attrs={'class':'txt_grade'})
    grade = mygrade.string

    mynum = info.find('span', attrs={'class':'txt_num'})
    num = mynum.string

    myrelease = info.find('span', attrs={'class':'txt_info'})
    release = myrelease.span.string

    result.append((no, title, grade, num, release)) #추출한 정보를 (no, title, grade, num, release) 형태의 튜플로 result 리스트에 추가
print(result) #infos 리스트의 각 요소에 대한 정보가 순서대로 저장
# [(1, '분노의 질주: 라이드 오어 다이', '7.8', '47.1%', '23.05.17'), (2, '가디언즈 오브 갤럭시: Volume 3', '8.9', '20.8%', '23.05.03'), ..., (20, '클로즈', '7.1', '0.2%', '23.05.03')]
print('-' * 40)

#result 리스트를 활용하여 데이터프레임 생성
mycolumn = ['순위', '제목', '평점', '예매율', '개봉일'] #데이터프레임의 열(column) 이름을 정의
myframe = DataFrame(result, columns=mycolumn) #result 리스트를 데이터프레임으로 변환하고, 열 이름은 mycolumn으로 지정
newdf = myframe.set_index(keys=['순위']) #데이터프레임의 인덱스(index)를 '순위' 열로 설정
print(newdf)
#                             제목   평점    예매율       개봉일
# 순위
# 1            분노의 질주: 라이드 오어 다이  7.8  47.1%  23.05.17
# 2        가디언즈 오브 갤럭시: Volume 3  8.9  20.8%  23.05.03
# ...
# 20                         클로즈  7.1   0.2%  23.05.03
print('-' * 40)

filename = 'daumMovie.csv'
myframe.to_csv(filename, encoding='utf8', index=False)
print(filename, ' saved...', sep='')
print('finished')

# reindex() 함수: 데이터프레임의 행(rows=[])과 열(columns=[])을 재정렬
dfmovie = myframe.reindex(columns=['제목', '평점', '예매율'])
print(dfmovie)
#                             제목   평점    예매율
# 0            분노의 질주: 라이드 오어 다이  7.8  47.1%
# 1        가디언즈 오브 갤럭시: Volume 3  8.9  20.8%
# ...
# 19                         클로즈  7.1   0.2%
print('-' * 40)

mygroup0 = dfmovie['제목'] #dfmovie의 열을 기준으로 '제목' 열을 선택
mygroup1 = dfmovie['평점'] # dfmovie의 열을 기준으로 '평점' 열을 선택
mygroup2 = dfmovie['예매율'] # dfmovie의 열을 기준으로 '예매율' 열을 선택
mygroup2 = mygroup2.str.replace('%','') # '예매율' 열의 값에서 '%' 기호를 제거(.replace('%',''))

df = pd.concat([mygroup1, mygroup2], axis=1) #mygroup1과 mygroup2를 수평으로(axis=1) 병합(pd.concat)
df = df.set_index(mygroup0) #'제목'열을 인덱스로 설정
df.columns = ['평점', '예매율'] #df의 열 이름을 '평점', '예매율'로 변경
print(df) # '제목'을 인덱스로, '평점'과 '예매율'을 열로 가지는 데이터프레임
#                              평점   예매율
# 제목
# 분노의 질주: 라이드 오어 다이           7.8  47.1
# 가디언즈 오브 갤럭시: Volume 3       8.9  20.8
# ...
# 클로즈                         7.1   0.2

#데이터프레임을 이용하여, 수평 막대 그래프(plot(kind='barh)) 생성
df.astype(float).plot(kind='barh', title='영화별 평점과 예매율', rot=0)
filename = 'daumMovieGraph.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
plt.show()
