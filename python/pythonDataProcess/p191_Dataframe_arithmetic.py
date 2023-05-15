import numpy as np
from pandas import Series, DataFrame

myindex = ['강호민', '유재준', '신동진']
mylist = [30, 40, 50]

#Series: pandas.Series 객체 생성. Series 객체는 1차원의 데이터를 담는 자료형. Series는 데이터와 그에 해당하는 인덱스로 구성됨
# 데이터는 data 파라미터를 통해, 인덱스는 index 파라미터를 통해 입력
myseries = Series(data=mylist, index=myindex) #myindex가 인덱스로, mylist가 데이터로 사용되어 Series 객체 생성
print('\nSeries print')
print(myseries)
# 강호민    30
# 유재준    40
# 신동진    50
# dtype: int64 (이때, mylist 데이터가 정수형이기 때문)

myindex = ['강호민', '유재준', '이수진']
mycolums = ['서울', '부산', '경주']
mylist = list(10 * onedata for onedata in range(1, 10)) #1~9까지의 정수를 10배한 값을 요소로 갖는 리스트

#DataFrame의 인덱스와 컬럼 이름을 설정하여 생성
#mylist의 리스트값을 2차원 배열로 생성하여 pandas의 DataFrame 형태로 변환
myframe = DataFrame(np.reshape(np.array(mylist), (3, 3)), index=myindex, columns=mycolums) #3*3 크기의 2차원 배열을 생성, 이를 pandas의 DataFrame 형태로 변환하는 코드. columns 파라미터에 mycolums를 전달해 DataFrame의 인덱스와 컬럼 이름을 설정
print('\nDataFrame print')
print(myframe)
#      서울  부산  경주
# 강호민  10  20  30
# 유재준  40  50  60
# 이수진  70  80  90

#.add(시리즈명, axis=0): 데이터프레임의 각 행(row, axis = 0)에 시리즈를 더한 값을 가진 새로운 데이터프레임을 생성
print('\nDataFrame + Series')
result = myframe.add(myseries, axis = 0) #axis=0 옵션을 주어서 2차원 배열과 1차원 배열을 행 방향으로 더함. myseries 배열의 값들이 myframe의 행에 따라서 반복해서 더해짐
#axis=0은 두 DataFrame을 세로로(concatenate vertically) 합치는 역할을 합니다. 만약 두 DataFrame의 index가 서로 일치하지 않는다면, 그 위치의 값을 NaN으로 채
print(result)
#        서울    부산     경주
# 강호민  40.0  50.0   60.0
# 신동진   NaN   NaN    NaN
# 유재준  80.0  90.0  100.0
# 이수진   NaN   NaN    NaN

myindex2 = ['강호민', '유재준', '김병준']
mycolums2 = ['서울', '부산', '대구']
mylist2 = list(5 * onedata for onedata in range(1, 10)) #1~9까지의 정수를 5배한 값을 요소로 갖는 리스트

# DataFrame(myframe, myframe2)의 같은 위치에 있는 요소끼리 더한 결과를DataFrame에 저장
myframe2 = DataFrame(np.reshape(np.array(mylist2), (3, 3)), index=myindex2, columns=mycolums2)
print('\nDataFrame print')
print(myframe2)
#      서울  부산  대구
# 강호민   5  10  15
# 유재준  20  25  30
# 김병준  35  40  45

print('\nDataFrame + DataFrame')
result = myframe.add(myframe2, fill_value = 0) #myframe과 myframe2의 같은 위치에 있는 요소끼리 더한 결과를 반환. 해당 요소가 없는 경우 fill_value값으로 대체
print(result)
#        경주    대구    부산    서울
# 강호민  30.0  15.0  30.0  15.0
# 김병준   NaN  45.0  40.0  35.0
# 유재준  60.0  30.0  75.0  60.0
# 이수진  90.0   NaN  80.0  70.0