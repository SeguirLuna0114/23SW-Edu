import numpy as np
import pandas as pd
from pandas import Series, DataFrame

mydata = [[10.0, np.nan, 20.0], \
          [20.0, 30.0, 40.0], \
          [np.nan, np.nan, np.nan], \
          [40.0, 50.0, 30.0]]
myindex = ['이순신', '김유신', '윤봉길', '계백']
mycolumns = ['국어', '영어', '수학']
myframe = DataFrame(data=mydata, index=myindex, columns=mycolumns)
print('\n성적 데이터프레임 출력')
print(myframe)
#        국어    영어    수학
# 이순신  10.0   NaN  20.0
# 김유신  20.0  30.0  40.0
# 윤봉길   NaN   NaN   NaN
# 계백   40.0  50.0  30.0

print('\n# 집계함수는 기본적으로 NaN은 제외하고 연산')
print('\n# sum(), axis = 0, 열방향')
print(myframe.sum(axis=0))
# 국어    70.0
# 영어    80.0
# 수학    90.0
# dtype: float64

print('\n# sum(), axis = 1, 행방향')
print(myframe.sum(axis=1))
# 이순신     30.0
# 김유신     90.0
# 윤봉길      0.0
# 계백     120.0
# dtype: float64

print('\n# mean(), axis = 1, skipna=False')
print(myframe.mean(axis=1, skipna=False))
# 이순신     NaN
# 김유신    30.0
# 윤봉길     NaN
# 계백     40.0
# dtype: float64
print('-' * 40)

print('\n# mean(), axis = 1, skipna=True')
print(myframe.mean(axis=1, skipna=True))
# 이순신    15.0
# 김유신    30.0
# 윤봉길     NaN
# 계백     40.0
# dtype: float64
print('-' * 40)

print('\n# idxmax() 최대값을 가진 색인 출력')
print(myframe.idxmax())
# 국어     계백
# 영어     계백
# 수학    김유신
# dtype: object

print('\n# 원본 데이터프레임 출력')
print(myframe)
#        국어    영어    수학
# 이순신  10.0   NaN  20.0
# 김유신  20.0  30.0  40.0
# 윤봉길   NaN   NaN   NaN
# 계백   40.0  50.0  30.0

#.cumsum()메소드: 누적합(cumulative sum)을 계산하여 새로운 DataFrame을 반환
#.cumsum(axis=0): 각 행들의 누적합을 계산하여 새로운 데이터프레임을 반환(axis=0은 행(row)을 기준으로 누적된 값을 계산)
print('\n# cumsum 메소드, axis=0 출력')
print(myframe.cumsum(axis=0)) #데이터프레임 myframe의 열들을 따라 각 행(axis = 0)들의 누적합을 계산

#.cumsum(axis=1): 각 컬럼(열)들의 누적합을 계산하여 새로운 데이터프레임을 반환(axis=1은 열(column)을 기준으로 누적된 값을 계산)
print('\n# cumsum 메소드, axis=1 출력')
print(myframe.cumsum(axis=1)) #데이터프레임 myframe의 행들을 따라 각 열(axis = 1)들의 누적합을 계산

#.cummax()메소드: cumulative maximum. 최대값을 누적해서 계산하는 메소드
#.cummax(axis=1): 각 행(Row)에서 해당 행까지의 최댓값을 반환. 결과값의 첫번째 열은 데이터프레임의 값이고, 두번째 열은 첫번째 열과 두번째 열 중에서 각 행의 값 중 최대값을 선택하여 출력 => 결과적으로 각 행(row)의 누적된 최대값을 반환(행의 원소 중 가장 큰 값이 각 행의 끝까지 누적된 결과)
#.cummax(axis=0): 각 열(Column)에서 해당 열까지의 최댓값을 반환. 결과값의 첫번째 행은 데이터프레임의 값이고, 두번째 행은 첫번째 행과 두번째행에서 각 열의 값 중 최대값을 선택하여 출력 => 결과적으로 각 열(column)에서 누적된 최대값을 반환(열의 원소 중 가장 큰 값이 각 열의 끝까지 누적된 결과)
print('\n# cummax 메소드, axis=1 출력')
print(myframe.cummax(axis=1)) #행(row)의 원소 중 가장 큰 값이 각 행의 끝까지 누적된 결과

#.cummin()메소드: cumulative minumum. 최소값을 누적해서 계산하는 메소드
# 열(axis=0) 또는 행(axis=1) 방향으로 누적된 최소값을 반환
print('\n# cummin 메소드, axis=1 출력')
print(myframe.cummin(axis=1)) #행(row)을 따라 누적된 최소값을 반환

#.mean()메소드: 데이터프레임의 열(column)별 평균을 계산
print('\n# 평균')
print(np.floor(myframe.mean()))
#np.floor() 함수: 입력값을 '내림'하여 정수로 반환

#.min()메소드: Series나 DataFrame에서 최소값(minimum)을 출력하는 메소드
myframe.loc[myframe['국어'].isnull(), '국어'] = np.min(myframe['국어'])-5
#myframe 데이터프레임에서 국어 점수가 결측치인 경우, 해당 값을 국어 점수의 최소값에서 5를 뺀 값으로 대체
myframe.loc[myframe['영어'].isnull(), '영어'] = np.min(myframe['영어'])-5
myframe.loc[myframe['수학'].isnull(), '수학'] = np.min(myframe['수학'])-5

print(myframe)

#.describe()메소드: 데이터프레임의 요약 통계정보 출력
print(np.round(myframe.describe()))
