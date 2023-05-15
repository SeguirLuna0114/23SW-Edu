import random
import pandas as pd

result = []
myColumns = ('번호', '이름', '나이') #튜플로 구성된 리스트 생성
myencoding = 'utf-8' #데이터프레임의 인코딩은 utf-8로 설정

for idx in range(1, 3): #1부터 2까지의 인덱스를 가진 레코드 생성 with idx(루프 반복변수)
    sublist = [] #빈 리스트를 생성
    sublist.append(100 * idx) #첫번째 항목을 idx와 100의 곱으로 계산 => 100, 200이 됨
    sublist.append('김철수' + str(idx)) #idx를 문자형태로 변환하여 '김철수'와 결합 => 김철수1, 김철수2가 됨
    sublist.append((random.randint(1, 10))) #randint(1, 10)을 이용하여 1~10사이의 무작위 정수 생성
    result.append(sublist) #위에서 생성한 sublist를 result리스트에 추가
    #result 리스트: [[100, '김철수1', 2], [200, '김철수2', 10]]

#pd.DataFrame()함수: pandas의 DataFrame객체 생성
myframe = pd.DataFrame(result, columns=myColumns)
#result 리스트를 사용하여 데이터프레임 생성. 이때 열 이름은 mycolumns로 지정.
#myframe 생성시 인덱스가 지정되지 않으면, 0부터 순차적으로 정수 인덱스가 할당됨
print(myframe)
#     번호    이름  나이
# 0  100  김철수1   2
# 1  200  김철수2   8

#.to_csv(저장할 파일명): DataFrame 객체를 csv 파일 형태로 저장
filename = 'csv_01_01.csv' #저장할 파일의 이름을 지정
myframe.to_csv(filename, encoding=myencoding, mode='w', index=True) #myframe을 csv 파일 형태로 저장
#encoding: 파일에 사용될 문자 인코딩 방식 지정
#mode: 파일의 모드를 지정(w-쓰기모드)
#index: index열을 저장할 지 여부(True로 지정하면 index를 저장)

filename = 'csv_01_02.csv'
myframe.to_csv(filename, encoding=myencoding, mode='w', index=False) #index: index열을 저장할 지 여부(False로 지정하면 index를 포함X)

filename = 'csv_01_03.csv'
myframe.to_csv(filename, encoding=myencoding, mode='w', index=False, header=False) #header: 열 이름을 CSV 파일에 포함할지 여부를 지정(False로 설정되어 있으므로 열 이름은 포함X)

filename = 'csv_01_04.csv'
myframe.to_csv(filename, encoding=myencoding, mode='w', index=False, sep="%") #sep: 구분자(delimiter)를 지정하여 작성(sep="%":'%'로 구분자 지정)

print(filename + '파일 저장 완료')