from bs4 import BeautifulSoup
from pandas import DataFrame as df
import numpy as np
import matplotlib.pyplot as plt

#Matplotlib의 기본 글꼴을 'Malgun Gothic'으로 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
#plt.rc('font', family='Malgun Gothic') 와 같은 결과를 출력

#html 파일을 열어 BeautifulSoup을 사용하여 파싱
html = open('ex5-10.html', 'r', encoding="utf-8") #'ex5-10.html' 파일을 읽기 모드('r')로 열어서 변수 html에 저장
# r 모드: 일반적인 텍스트 파일을 읽을 때 사용

#BeautifulSoup 라이브러리를 사용하여 HTML 문서를 파싱
soup = BeautifulSoup(html, 'html.parser') #html문서 파싱하여 파이썬에서 사용하기 쉬운 형태로 만들어주는 라이브러리

# soup.find() 메소드: soup 객체 안에서 찾고자 하는 '태그'나 '속성'을 검색할 때 사용. 찾고자하는 태그나 속성의 이름을 문자열 형태로 전달. 여러 태그 존재시, 첫번째 태그만 반환
tbody = soup.find("tbody") #HTML에서 'tbody 태그'를 찾음
tds = tbody.findAll('td') #tbody 태그 안에서 하위태그인 'td 태그'를 찾음

result = []
for data in tds: #td태그의 데이터에 한해서
    #.text 속성: 텍스트 데이터만 추출
    result.append(data.text) #td 태그 안의 텍스트를 추출한 것(data.text)들을 result 리스트에 추가
print(result) # HTML에서 선택한 <td> 태그들의 텍스트 데이터만 모두 포함
# ['황기태', '80', '70', '이재문', '95', '99', '이병은', '85', '90', '김남윤', '50', '40']
print('-' * 50)

#pandas 라이브러리의 DataFrame 객체로 변환
mycolumns = ['이름', '국어', '영어'] #DataFrame 객체의 열 이름을 지정
myframe = df(np.reshape(np.array(result), (4, 3)), columns=mycolumns)
# np.reshape(np.array(result), (4, 3)): array 함수를 사용하여 추출된 데이터를 4행 3열의 행렬 형태(np.array)로 변환(np.reshape)
# df 함수: pandas 라이브러리의 DataFrame 객체를 생성
myframe = myframe.set_index('이름') #set_index 함수: DataFrame 객체의 인덱스를 '이름' 열로 설정
print(myframe)
#      국어  영어
# 이름
# 황기태  80  70
# 이재문  95  99
# 이병은  85  90
# 김남윤  50  40
print('-' * 50)

# Pandas DataFrame 객체를 line chart로 시각화
myframe.astype(float).plot(kind='line', title='Score', legend=True)
# .astype(float): 데이터프레임의 모든 값을 실수형(float)으로 변환한 새로운 데이터프레임 반환. 수치계산에 활용 가능
# title: 그래프의 제목 지정
# legend: 범례의 표시 여부(True/False) 결정

filename = 'scoreGraph.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved...')
plt.show()
