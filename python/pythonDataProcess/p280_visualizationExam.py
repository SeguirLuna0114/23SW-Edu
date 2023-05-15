import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
from math import sqrt

#matplotlib 라이브러리에서 한글 폰트를 사용하기 위한 설정
font_location = 'c:/windows/fonts/malgun.ttf' #사용할 폰트 파일의 경로 지정
font_name = font_manager.FontProperties(fname=font_location).get_name() #font_manager.FontProperties 클래스를 사용하여 해당경로 폰트파일의 이름을 가져와(.get_name())font_name변수에 저장
matplotlib.rc('font', family=font_name)#전역적으로 폰트패밀리를 지정한 폰트이름으로 설정

#theater 데이터프레임 생성
theaterfile = 'theater.csv' #저장할 파일명 지정
colnames = ['id', 'theater', 'region', 'bindo'] #column 이름을 list형태로 지정
dftheater = pd.read_csv(theaterfile, names=colnames, header=None) #기본적으로 read_csv()파일은 첫번째 행을 열 이름으로 생성=>첫번째 행이 열이름이 아닌 실제 데이터인 경우, None으로 설정하여 데이터를 정상적으로 읽음

#.rename()메서드를 사용 => 데이터프레임의 값 변경
dftheater = dftheater.rename(index=dftheater.id) #데이터프레임의 인덱스를 id열(column)의 값으로 변경
# set_index메소드 사용: dftheater = dftheater.set_index('id')로도 인덱스를 'column=id'로 변경 가능

#.reindex(columns= [list]): 데이터프레임의 열(column) 순서 변경 <-열 순서를 리스트형태로 전달
dftheater = dftheater.reindex(columns=['theater', 'region', 'bindo']) #열(column) 순서를 'theater', 'region', 'bindo'로 변경

#.index.name: 인덱스의 이름 변경 코드
dftheater.index.name = 'id' #인덱스의 이름이 id로 변경됨

print('전체 조회')
print(dftheater)
#         theather region  bindo
# id
# brother   daehan     강남     15
# brother  megabox     강남     15
# brother      cgv     강남     30
# brother   daehan     신촌     20
# brother  megabox     신촌     30
# brother      cgv     신촌     15
# hulk      daehan     강남     25
# hulk     megabox     강남     15
# hulk         cgv     강남     15
# hulk      daehan     신촌     25
# hulk     megabox     신촌     20
# hulk         cgv     신촌     15
# king      daehan     강남     30
# king     megabox     강남     20
# king         cgv     강남     25
# king      daehan     신촌     25
# king     megabox     신촌     25
# king         cgv     신촌     15
# lucky     daehan     강남     25
# lucky    megabox     강남     20
# lucky        cgv     강남     25
# lucky     daehan     신촌     30
# lucky    megabox     신촌     15
# lucky        cgv     신촌     20
print('-' * 50)

#.groupby('column')['column2']메서드: 데이터프레임을 'column'열 기준으로 그룹화하여 'column2'열에 대한 연산을 수행
print('극장별 상영 횟수 집계')
mygrouping = dftheater.groupby('theater')['bindo'] #'theater'열 기준으로 데이터프레임 그룹화
#'bindo'열에 대한 연산을 수행
sumSeries = mygrouping.sum() #합계 계산
# theater
# cgv        160
# daehan     195
# megabox    160
# Name: bindo, dtype: int64

meanSeries = mygrouping.mean() #평균 계산
# theater
# cgv        20.000
# daehan     24.375
# megabox    20.000
# Name: bindo, dtype: float64

sizeSeries = mygrouping.size() #그룹 크기 계산
print(sizeSeries)
# theater
# cgv        8
# daehan     8
# megabox    8
# Name: bindo, dtype: int64

#.agg(['인자'])메서드: 전달하는 인자를 통해 원하는 연산 가능
# result = mygrouping.agg(['sum', 'mean', 'size']) 라고 작성하여 여러개의 연산을 한번에 수행 가능

#concat() 메서드: 여러 시리즈를 합쳐서 새로운 데이터프레임 생성
print('3개의 시리즈 이용 데이터프레임 생성')
df = pd.concat([sumSeries, meanSeries, sizeSeries], axis=1) #axis=1: 열 방향으로 데이터를 합침
df.columns = ['합계', '평균', '개수'] #생성한 데이터프레임(df)의 열 이름 설정
print(df)
#           합계      평균  개수
# theater
# cgv      160  20.000   8
# daehan   195  24.375   8
# megabox  160  20.000   8
print('-' * 50)
print(len(df)) #len(데이터프레임 이름): 데이터프레임의 행(row)개수 반환 => 3

# plot(kind='barh')메서드 => '가로막대' 그래프 생성
df.plot(kind='barh', rot=0) #rot=0: x축 눈금 레이블이 수평으로 표시
plt.title(str(len(df)) + '개 매장 집계 데이터') #그래프의 제목을 생성

filename = 'visualizationExam_01.png' #저장할 파일 이름 설정
plt.savefig(filename)
print(filename + ' saved...')
plt.show()

#열(column)마다 어떤 함수를 적용할지 dictionary 정의
# 각 key는 데이터프레임의 열(column)이름을 지정
# 각 value는 해당 열에 적용할 함수 지정
print('집계 메소드를 사전에 담아 전달')
print('지역의 개수와 상영 횟수의 총합')
mydict = {'bindo':'sum', 'region':'size'} #mydict는 'bindo' 열(column)에는 sum 함수를 적용하고, 'region' 열(column)에는 size 함수를 적용
result = dftheater.groupby('theater').agg(mydict)
# 'theater' 열(column)로 그룹화한 후, mydict 딕셔너리에 지정된 함수를 각 열(column)에 적용
print(result)
#          bindo  region
# theater
# cgv        160       8
# daehan     195       8
# megabox    160       8
print('-' * 50)

print('numpy를 이용한 출력')
result = mygrouping.agg([np.count_nonzero, np.mean, np.std])
# count_nonzero() 함수는 0이 아닌 값의 개수를 반환
# mean() 함수는 평균 반환
# std() 함수는 표준편차를 반환
print(result)
#          count_nonzero    mean       std
# theater
# cgv                  8  20.000  5.976143
# daehan               8  24.375  4.955156
# megabox              8  20.000  5.345225
print('-' * 50)

def myroot(values): #values의 합계를 구하고, 제곱근을 계산
    mysum = sum(values)
    return sqrt(mysum)

def plus_add(values, somevalue): #values의 합계를 구하고, 이를 제곱근을 계산한 후(myroot함수), 함수 인자로 전달된 somevalue와 더함
    result = myroot(values)
    return result + somevalue

mygrouping = dftheater.groupby('theater')['bindo']
print('groupby와 사용자 정의 함수 사용')
result = mygrouping.agg(myroot)
print(result)
print('-' * 50)

# plus_add()를 활용하여 그룹별로 'bindo' 열(column)의 값을 계산
print('groupby와 사용자 정의 함수(매개변수 2개) 사용')
result = mygrouping.agg(plus_add, somevalue=3) #somevalue=3: 함수를 사용하여 그룹별 'bindo' 열(column)의 값을 계산할 때 somevalue 값으로 3을 사용
print(result)
print('-' * 50)

print('컬럼 2개 이상을 그룹핑')
newgroping = dftheater.groupby(['theater', 'region'])['bindo']
result = newgroping.count() #newgroping 그룹 객체에서 'bindo' 열(column)만 추출한 후, count() 메소드를 호출하여 각 그룹의 원소 개수를 계산
print(result) # 'theater'와 'region' 열(column)의 고유한 값의 조합에 대해 'bindo' 열(column)의 원소 개수를 계산한 결과가 포함된 Series
# cgv      강남        4
#          신촌        4
# daehan   강남        4
#          신촌        4
# megabox  강남        4
#          신촌        4
# Name: bindo, dtype: int64
print('-' * 50)

#.plot(kind='bar'): 막대그래프 생성
newDf = df.loc[:, ['평균','개수']] #'평균'과 '개수' 열(column)만 추출하여 새로운 DataFrame newDf를 생성
newDf.plot(kind='bar', rot=0)
plt.title('3개 극장의 평균과 상영관 수') #제목 정의

filename = 'visualizationExam_02.png'
plt.savefig(filename)
print(filename + ' saved...')

lables = [] #빈 리스트로 초기화
explode = (0, 0.03, 0.06) #각 항목이 파이 차트에서 돌출되는 정도를 나타내는 튜플(tuple)

# Series의 인덱스를 사용하여 라벨을 생성하는 반복문
for key in sumSeries.index: #key는 인덱스를 나타냄
    mydata = key + '(' + str(sumSeries[key]) + ')'
    lables.append(mydata)

# ax1.pie() 함수를 호출하여 파이 차트를 생성: sumSeries Series를 이용하여 파이 차트(pie chart)를 그리는 코드
fig1, ax1 = plt.subplots() #plt.subplots() 함수를 호출하여, 플롯(plot)과 축(axis) 객체를 생성
mytuple = tuple(lables) #lables 리스트를 튜플(tuple)로 변환
ax1.pie(sumSeries, explode=explode, labels=mytuple, autopct='%1.1f%%', shadow=True, startangle=90)
# shadow=True: 파이 차트의 외곽선에 그림자 효과를 추가
# startangle=90은 파이 차트의 시작 각도를 90도로 설정
ax1.axis('equal') # ax1.axis('equal')을 호출하여 파이 차트를 원형으로 출력
plt.show()

filename = 'visualizationExam_03.png'
plt.savefig(filename)
print(filename + ' saved...')
print('finished')