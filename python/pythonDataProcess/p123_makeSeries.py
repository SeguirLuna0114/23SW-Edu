from pandas import Series # pandas 패키지에서 Series 모듈을 현재 파일에서 사용하기 위해 불러옴
import numpy as np #NumPy라이브러리를 가져올 때 일반적으로 사용되는 축약어 np

mylist = [10, 40, 30] #정수로 이루어진 list 생성
myindex = ['김유신', '이순신', '강감찬'] #문자열로 이루어진 list 생성

#Series모듈은 1차원 데이터구조를 담당: 인덱스(0부터 시작)와 데이터 값(value)로 구성됨
#Series()함수: Pandas 라이브러리에서 list 데이터를 시리즈객체로 변환
print('\n#Cast 01')
myseries = Series(mylist) #Series()함수를 이용하여 mylist 리스트를 시리즈 객체로 변환한 뒤, myseries 변수에 저장
print(type(myseries)) #데이터타입 'pandas.core.series.Series' : Pandas 라이브러리에서 제공하는 Series 클래스의 데이터 타입
#Series 객체는 각 데이터에 이름(name)을 붙일 수 있고, 누락된 데이터(NaN 값)를 처리할 수 있음
print(myseries) #myseries 변수에 저장된 시리즈 객체를 출력
# 0    10
# 1    40
# 2    30 #시리즈 객체는 1차원 데이터구조를 가지며, 각 데이터값과 해당값의 인덱스(index)를 같이 보여줌
# dtype: int64 #dtype으로 지정한 자료형도 함께 출력됨-지정하지 않을 경우 기본값 정수형(int64)으로 출력됨

#Series 생성자의 data 매개변수에 list를 전달하여 Series 객체를 생성
print('\n#Cast 02')
myseries = Series(data=mylist) #결과로 [10, 40, 30]을 데이터로 갖는 Series 객체가 생성되어 출력됨(myseries = Series(mylist)와 같은 결과)
print(myseries) #myseries 변수에 저장된 시리즈 객체를 출력
# 0    10
# 1    40
# 2    30 #시리즈 객체는 1차원 데이터구조를 가지며, 각 데이터값과 해당값의 인덱스(index)를 같이 보여줌
# dtype: int64 #dtype으로 지정한 자료형도 함께 출력됨-지정하지 않을 경우 기본값 정수형(int64)으로 출력됨

#Series 생성자의 data 매개변수와 index 매개변수에 list를 전달하여 Series 객체를 생성
print('\n#Cast 03')
myseries = Series(data=mylist, index=myindex) #mylist라는 리스트와 myindex라는 인덱스를 가진 pandas Series를 생성: mylist를 series로 변환하여 series값으로, myindex를 series의 인덱스로 지정하여 Series의 인덱스 값으로 들어감
print(myseries)
# 김유신    10 # 정수형 10은 int64데이터타입
# 이순신    40
# 강감찬    30
# dtype: int64 #데이터 타입은 int64

#Series 생성자의 data 매개변수와 index 매개변수에 list를 전달하여 Series 객체를 생성. dtype 매개변수를 지정하여 데이터타입 설정
print('\n#Cast 04')
myseries = Series(data=mylist, index=myindex, dtype=float) #mylist와 myindex로 구성된 pandas Series 객체 생성. 이때 데이터타입을 float(실수)로 지정
print(myseries)
# 김유신    10.0 #10.0은 float64 데이터타입(10.0은 실수형 10)
# 이순신    40.0
# 강감찬    30.0
# dtype: float64 #데이터 타입은 float64 => 출력값들의 소수점 이하도 모두 출력됨