import numpy as np
from pandas import DataFrame

myindex = ['이순신', '김유신', '강감찬', '광해군', '연산군'] #리스트 생성
mycolumns = ['서울', '부산', '광주', '목포', '경주'] #리스트 생성
mylist = list(10 * onedata for onedata in range(1, 26)) #리스트 생성:1~25까지 정수를 생성 -> 정수에 10배를 한 mylist 생성
print(mylist)
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]

# DataFrame 클래스를 사용하여 데이터프레임 생성
myframe = DataFrame(np.reshape(mylist, (5, 5)), index=myindex, columns=mycolumns) #mylist라는 리스트를 5*5크기의 2차원 배열로 변환 -> 이를 데이터프레임의 값으로 사용. 데이터프레임의 인덱스는 myindex 리스트로, 컬럼은 mycolumns로 설정
print(myframe)
#       서울   부산   광주   목포   경주
# 이순신   10   20   30   40   50
# 김유신   60   70   80   90  100
# 강감찬  110  120  130  140  150
# 광해군  160  170  180  190  200
# 연산군  210  220  230  240  250

#iloc을 이용하여 해당 인덱스의 데이터를 추출(iloc은 인덱스 숫자로 데이터에 접근할 경우 사용)
print('\n1 row data read of series')
result = myframe.iloc[1] #데이터프레임의 두 번째 행(인덱스=1)에 해당하는 데이터를 추출한 결과를 Series 객체로 반환
print(type(result)) #result의 값이 Series 클래스
# 데이터타입은 'pandas.core.series.Series'
print(result) #series 클래스의 인스턴스. myframe 데이터프레임에서 첫번째 행을 추출한 결과
# 서울     60
# 부산     70
# 광주     80
# 목포     90
# 경주    100 (인덱스=myframe데이터프레임의 칼럼)
# Name: 김유신, dtype: int32

print('\nmulti row data read of series')
result = myframe.iloc[[1, 3]] #myframe 데이터프레임의 두 번째(인덱스1)와 네 번째 행(인덱스3)에 해당하는 데이터를 추출한 결과를 DataFrame 객체로 반환
print(type(result))
# 데이터타입은 'pandas.core.frame.DataFrame'
print(result)
#       서울   부산   광주   목포   경주
# 김유신   60   70   80   90  100
# 광해군  160  170  180  190  200

#iloc 인덱서: 슬라이싱[0:2] 대신에 인덱스를 통해 데이터를 추출[0:2]
print('\neven row data read of series')
result = myframe.iloc[0::2] # myframe 데이터프레임에서 첫 번째 행부터 끝 행까지 두 칸 간격으로 데이터를 추출(1,3,5행)
print(type(result))
# 데이터타입은 'pandas.core.frame.DataFrame'
print(result)
#       서울   부산   광주   목포   경주
# 이순신   10   20   30   40   50
# 강감찬  110  120  130  140  150
# 연산군  210  220  230  240  250

print('\nodd row data read of series')
result = myframe.iloc[1::2] # myframe 데이터프레임에서 두 번째 행부터 끝 행까지 두 칸 간격으로 데이터를 추출(2,4행)
print(type(result))
# 데이터타입은 'pandas.core.frame.DataFrame'
print(result)
#       서울   부산   광주   목포   경주
# 김유신   60   70   80   90  100
# 광해군  160  170  180  190  200

#.loc['데이터']: 데이터프레임에서 '데이터'라는 인덱스를 가진 행에 해당하는 데이터 추출
print('\n김유신 included row data read of series')
result = myframe.loc['김유신'] # 데이터프레임에서 '김유신'이라는 인덱스를 가진 행에 해당하는 데이터를 추출
print(type(result)) #데이터프레임 중 하나의 행 데이터를 불러오기에 Series 타입
# 데이터타입은 'pandas.core.series.Series'
print(result)
# 서울     60
# 부산     70
# 광주     80
# 목포     90
# 경주    100
# Name: 김유신, dtype: int32

# .loc[['데이터']]: 인덱스를 리스트 형태로 전달 => '데이터'를 가진 행을 포함하는 데이터프레임을 반환
print('\n김유신 included row data read of Dataframe')
result = myframe.loc[['김유신']] #데이터로 읽으려면 loc[[]]
print(type(result)) #대괄호를 두번 사용하여 리스트형태로 전달한 경우, 데이터타입은 DataFrame이다.
# 데이터타입은 'pandas.core.frame.DataFrame'
print(result)
#      서울  부산  광주  목포   경주
# 김유신  60  70  80  90  100

#loc 인덱서_[[]] 대괄호를 두 번 사용하여 인덱스를 리스트 형태로 전달 => 해당 인덱스를 가진 모든 행을 포함하는 데이터프레임을 반환
print('\n이순신, 강감찬 included row data read of Dataframe')
result = myframe.loc[['이순신', '강감찬']] # myframe 데이터프레임에서 '이순신'과 '강감찬'이라는 인덱스를 가진 행에 해당하는 데이터를 추출 => DataFrame 데이터타입으로 반환
print(type(result))
# 데이터타입은 'pandas.core.frame.DataFrame'
print(result)
#       서울   부산   광주   목포   경주
# 이순신   10   20   30   40   50
# 강감찬  110  120  130  140  150

#.index: 해당 데이터프레임의 인덱스 반환
print(myframe.index) #myframe 데이터프레임의 인덱스를 반환
# Index(['이순신', '김유신', '강감찬', '광해군', '연산군'], dtype='object') <-인덱스의 라벨 값들이 포함된 Index객체가 반환됨. 문자열로 이루어짐
print('-' * 50)

#.loc[['인덱스 데이터'], ['컬럼 데이터']]: 인덱스와 컬럼명을 각각 리스트 형태로 전달하면, 해당 인덱스와 컬럼명을 가진 하위 데이터프레임을 반환
print('\n이순신, 광주 실적 included row data read of Dataframe')
result = myframe.loc[['이순신'], ['광주']] #'이순신'인덱스를 가진 행과 '광주' 컬럼을 가진 열에 해당하는 데이터 추출
print(type(result))
# 데이터타입은 'pandas.core.frame.DataFrame'
print(result)
#      광주
# 이순신  30

print('\n연산군, 강감찬 / 광주, 목포 실적 included row data read of Dataframe')
result = myframe.loc[['이순신', '강감찬'], ['광주', '목포']] #'이순신', '강감찬' 인덱스를 가진 행과 '광주', '목포' 컬럼을 가진 열에 해당하는 데이터 추출
print(type(result))
# 데이터타입은 'pandas.core.frame.DataFrame'
print(result)
#       광주   목포
# 이순신   30   40
# 강감찬  130  140

#index 범위로 사용할 경우 대괄호[]하나만 사용
#.loc[시작 인덱스:끝 인덱스, 시작 컬럼 : 끝 컬럼]: loc 인덱서에서 ':' 기호를 사용하여 행과 열의 범위를 지정
print('\n이순신 ~ 강감찬 / 서울 ~ 목포 실적 included row data read of Dataframe')
result = myframe.loc['이순신' : '강감찬', '서울' : '목포'] #'이순신'~'강감찬' 인덱스를 가진 행과 '서울'~'목포' 컬럼을 가진 열에 해당하는 데이터 추출
print(type(result))
# 데이터타입은 'pandas.core.frame.DataFrame'
print(result)
#       서울   부산   광주   목포
# 이순신   10   20   30   40
# 김유신   60   70   80   90
# 강감찬  110  120  130  140

print('\n김유신 ~ 광해군 / 부산 실적 included row data read of Dataframe')
result = myframe.loc['김유신' : '광해군', ['부산']] #index 범위로 사용할 경우 대괄호[]하나만 사용
print(type(result))
# 데이터타입은 'pandas.core.frame.DataFrame'
print(result)
#       부산
# 김유신   70
# 강감찬  120
# 광해군  170

#.loc[인덱스를 지정하는 부울 리스트]=> True가 지정된 인덱스에 해당하는 행만 추출
print('\nBoolean Data process')
result = myframe.loc[[False, True, True, False, True]] #1,2,4행만 추출
print(result) #True만 갖고와서 출력
#       서울   부산   광주   목포   경주
# 김유신   60   70   80   90  100
# 강감찬  110  120  130  140  150
# 연산군  210  220  230  240  250

#.loc 인덱서의 부울 시리즈 => 값의 대소비교하여 True와 False 추출
print('\n부산 실적 <= 100')
result = myframe.loc[myframe['부산'] <= 100] # '부산' 열의 값을 비교하여 100 이하인 경우 True를, 그렇지 않은 경우 False를 반환
print(result)
#      서울  부산  광주  목포   경주
# 이순신  10  20  30  40   50
# 김유신  60  70  80  90  100

print('\n목포 실적 == 140')
result = myframe.loc[myframe['목포'] == 140]
print(result)
#       서울   부산   광주   목포   경주
# 강감찬  110  120  130  140  150

#True와 False를 반환한 부울 시리즈
cond1 = myframe['부산'] >= 70 #'부산' 열의 값이 70 이상
cond2 = myframe['목포'] >= 140 #'목포' 열의 값이 140 이상

print(type(cond1)) #pandas에서 제공하는 시리즈 데이터 타입. 1차원 배열과 유사하게 값과 인덱스를 가짐
# pandas.core.series.Series
print('-' * 40)

#시리즈를 원소로 갖는 리스트를 이용하여 데이터프레임 생성 => 각 시리즈가 데이터프레임의 행으로 들어감.
df = DataFrame([cond1, cond2]) #cond1과 cond2 두 개의 시리즈를 원소로 갖는 리스트를 이용하여 데이터프레임을 생성.
print(df)
#       이순신    김유신   강감찬   광해군   연산군
# 부산  False   True  True  True  True
# 목포  False  False  True  True  True
print('-' * 40)

#.all(): DataFrame의 모든 값이 True인 경우 True를 반환하고, 하나라도 False가 있다면 False를 반환
print(df.all()) #df 데이터프레임의 각 열(axis=0)이 모두 True인지 아닌지를 판별 => 시리즈형태로 반환(열을 index값으로)
# 이순신    False
# 김유신    False
# 강감찬     True
# 광해군     True
# 연산군     True
# dtype: bool
print('-' * 40)

# df.any():  DataFrame의 값 중에서 하나라도 True가 있다면 True를 반환합니다. 즉, DataFrame의 모든 값이 False일 경우 False를 반환
print(df.any())
# 이순신    False
# 김유신     True
# 강감찬     True
# 광해군     True
# 연산군     True
# dtype: bool
print('-' * 40)

#.loc[df.all()]: 두 조건식이 모두 참인 행을 골라낸 후, 열이 참인지 검사하여 결과를 Series객체로 반환 ->  df.all()의 결과를 인덱싱하여, 두 조건식이 모두 참인 행을 추출
result = myframe.loc[df.all()]
print(result)
#       서울   부산   광주   목포   경주
# 강감찬  110  120  130  140  150
# 광해군  160  170  180  190  200
# 연산군  210  220  230  240  250
print('-' * 40)

#.loc[df.any()]: 두 조건식중 하나 이상이 참인 행을 골라낸 후, 열이 참인지 검사하여 결과를 Series객체로 반환 ->  df.any()의 결과를 인덱싱하여, 두 조건식중 하나라도 참인 행을 추출
result = myframe.loc[df.any()]
print(result)
#       서울   부산   광주   목포   경주
# 김유신   60   70   80   90  100
# 강감찬  110  120  130  140  150
# 광해군  160  170  180  190  200
# 연산군  210  220  230  240  250
print('-' * 40)

#lambda 함수: 한 줄로 간단한 함수를 생성
print('\nlambda function')
result = myframe.loc[lambda df : df['광주'] >= 130] # '광주' 열의 값을 가져와 130 이상인지 검사하여 True 또는 False 값을 반환하는 함수를 생성하고, 이 함수를 loc[]의 인자로 전달
print(result)
#       서울   부산   광주   목포   경주
# 강감찬  110  120  130  140  150
# 광해군  160  170  180  190  200
# 연산군  210  220  230  240  250

print('\ndata set 30 => 이순신, 강감찬 부산 실적')
myframe.loc[['이순신', '강감찬'], ['부산']] = 30
print(myframe)
#       서울   부산   광주   목포   경주
# 이순신   10   30   30   40   50
# 김유신   60   70   80   90  100
# 강감찬  110   30  130  140  150
# 광해군  160  170  180  190  200
# 연산군  210  220  230  240  250

print('\ndata set 80 => 김유신 ~ 광해군 경주 실적')
myframe.loc['김유신' : '광해군', ['경주']] = 80
print(myframe)
#       서울   부산   광주   목포   경주
# 이순신   10   30   30   40   50
# 김유신   60   70   80   90   80
# 강감찬  110   30  130  140   80
# 광해군  160  170  180  190   80
# 연산군  210  220  230  240  250

#콜론(:)을 사용 => 모든 범위를 나타내는 역할
print('\ndata set 50 => 연산군 모든 실적')
myframe.loc[['연산군'], :] = 50
print(myframe)
#       서울   부산   광주   목포  경주
# 이순신   10   30   30   40  50
# 김유신   60   70   80   90  80
# 강감찬  110   30  130  140  80
# 광해군  160  170  180  190  80
# 연산군   50   50   50   50  50

print('\ndata set 60 => 모든 사람의 광주 실적')
myframe.loc[:, ['광주']] = 60
print(myframe)
#       서울   부산  광주   목포  경주
# 이순신   10   30  60   40  50
# 김유신   60   70  60   90  80
# 강감찬  110   30  60  140  80
# 광해군  160  170  60  190  80
# 연산군   50   50  60   50  50

print('\ndata set 0 : 경주 실적 <= 60인 사람의 경주, 광주 실적')
myframe.loc[myframe['경주'] <= 60, ['경주', '광주']] = 0
print(myframe)
#       서울   부산  광주   목포  경주
# 이순신   10   30   0   40   0
# 김유신   60   70  60   90  80
# 강감찬  110   30  60  140  80
# 광해군  160  170  60  190  80
# 연산군   50   50   0   50   0