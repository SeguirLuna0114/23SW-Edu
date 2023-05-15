import numpy as np
import pandas as pd
from pandas import DataFrame, Series

#Series객체는 인덱스와 value가 짝지어진 일련의 데이터
print('\n# 시리즈의 누락 데이터 처리')
print('#원본 시리즈')
myseries = Series(['강감찬', '이순신', np.nan, '광해군']) # '강감찬', '이순신', '광해군' 이라는 문자열로 이루어진 3개의 값과 NaN 이라는 결측치를 가지는 4개의 값이 들어가 있는 Series 객체가 생성
#np.nan: Not a Number. 숫자가 아니라는 것을 나타내는 특수 값. 결측치(missing value)를 나타내는데 자주 사용됨. 파이썬의 기본 데이터타입인 float(실수)타입으로 처리됨
print(myseries)
# 0    강감찬
# 1    이순신
# 2    NaN
# 3    광해군
# dtype: object (문자열과 결측치가 함께 존재하기 때문)

#.isnull() 메서드: myseries 시리즈 객체의 각 원소가 결측치인지 아닌지를 판별하여, 결과를 불리언(boolean) 형태로 반환
print('\n# isnull() 함수 : NaN이면 True')
print(myseries.isnull())
# 0    False
# 1    False
# 2     True #결측치이기에 True가 나옴
# 3    False
# dtype: bool

#.isnotnull() 메서드: myseries 시리즈 객체의 각 원소가 결측치인지 아닌지를 판별하여, 결과를 불리언(boolean) 형태로 반환
print('\n# notnull() 함수 : NaN이 아니면 True')
print(myseries.notnull())
# 0     True
# 1     True
# 2    False #결측치이기에 False가 나옴
# 3     True
# dtype: bool
print("-" * 40)

#.notnull(): 시리즈에서 null이 아닌 데이터들의 boolean mask(마스크)를 반환
print('\n# notnull() 이용하여 참인 항목만 출력')
print(myseries[myseries.notnull()]) #boolean mask를 활용하여 True인 데이터만 선택하여 출력
# 0    강감찬
# 1    이순신
# 3    광해군
# dtype: object

#.dropna() 메서드: 결측값이 있는 데이터를 제거한 새로운 시리즈를 반환
print('\n# dropna() 이용하여 누락 데이터 처리')
print(myseries.dropna())
# 0    강감찬
# 1    이순신
# 3    광해군
# dtype: object
print("-" * 40)

filename = 'excel02.csv'
myframe = pd.read_csv(filename, index_col='이름', encoding='utf-8') #index_col 매개변수를 사용하여 DataFrame의 인덱스를 '이름'으로 설정. 인코딩은 utf-8로 지정
print(myframe)
#        국어    영어    수학
# 이름
# 강감찬  10.0  20.0  30.0
# 홍길동  40.0   NaN   NaN
# 박영희   NaN   NaN   NaN
# 김철수   NaN  50.0  60.0

#.dropna(axis=0) 메서드: 결측치가 있는 행(axis=0)을 기준으로 행 제거
print('\n# dropna() 이용하여 누락 데이터 처리')
cleaned = myframe.dropna(axis=0) #결측치가 있는 행(axis=0)을 기준으로 제거
print(cleaned)
#        국어    영어    수학
# 이름
# 강감찬  10.0  20.0  30.0

#how 매개변수: 삭제할 대상을 지정하는 역할
#.dropna(axis=0, how='all'): 모든 값이 NaN인 행을 삭제
print('\n# how="all" 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=0, how='all') #axis=0은 행을 의미. how='all'을 설정하면 모든 값이 NaN인 행을 삭제
print(cleaned)
#        국어    영어    수학
# 이름
# 강감찬  10.0  20.0  30.0
# 홍길동  40.0   NaN   NaN
# 김철수   NaN  50.0  60.0

#.dropna(axis=0, how='any') : 하나라도 결측치가 있는 행을 제거
print('\n# how="any" 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=0, how='any')
print(cleaned)
#        국어    영어    수학
# 이름
# 강감찬  10.0  20.0  30.0

#subset 매개변수를 사용하여 특정 컬럼에 NaN이 있는 행만 제거
print('\n# [영어] 컬럼에서 NaN 제거')
print(myframe.dropna(subset=['영어'])) #'영어' 컬럼에 NaN이 있는 행(row)을 제거
#        국어    영어    수학
# 이름
# 강감찬  10.0  20.0  30.0
# 김철수   NaN  50.0  60.0

#.dropna(axis=1, how='all'): 모든 값이 NaN인 컬럼(열)을 삭제
print('\n# 컬럼 기준, how="all" 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=1, how='all') #axis=1은 열을 기준으로 데이터를 처리. #how='all'은 해당 열의 모든 값이 결측치일 때만 해당 열을 삭제
print(cleaned)
#        국어    영어    수학
# 이름
# 강감찬  10.0  20.0  30.0
# 홍길동  40.0   NaN   NaN
# 박영희   NaN   NaN   NaN
# 김철수   NaN  50.0  60.0

#.dropna(axis=1, how='any') : 하나라도 결측치가 있는 컬럼(열)을 제거
print('\n# 컬럼 기준, how="any" 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=1, how='any')
print(cleaned)
# Empty DataFrame
# Columns: []
# Index: [강감찬, 홍길동, 박영희, 김철수]

#.loc[] 메소드: 행과 열의 라벨을 기반으로 데이터를 선택
print('\n## before')
print(myframe)
# ## before
#        국어    영어    수학
# 이름
# 강감찬  10.0  20.0  30.0
# 홍길동  40.0   NaN   NaN
# 박영희   NaN   NaN   NaN
# 김철수   NaN  50.0  60.0
myframe.loc[['강감찬','홍길동'], ['국어']] = np.nan
# '강감찬'과 '홍길동' 행에 해당하는 '국어' 열(column)의 값을 np.nan으로 변경
print('## after')
print(myframe)
# ## after
#      국어    영어    수학
# 이름
# 강감찬 NaN  20.0  30.0
# 홍길동 NaN   NaN   NaN
# 박영희 NaN   NaN   NaN
# 김철수 NaN  50.0  60.0

print()
print(myframe.dropna(axis=1, how="all")) #모든 값이 NaN인 열(column)을 제거
#        영어    수학
# 이름
# 강감찬  20.0  30.0
# 홍길동   NaN   NaN
# 박영희   NaN   NaN
# 김철수  50.0  60.0

#thresh 매개변수: 유효한(non-NA) 값의 개수가 thresh 이상인 행(axis=0)/열(axis=1)만 남기고 나머지는 삭제
print('## thresh option')
print(myframe.dropna(axis=1, thresh=2)) #thresh=2 옵션을 주어 유효한 값의 개수가 2개 이상인 열(axis=1)만 남기고 나머지는 삭제
# ## thresh option
#        영어    수학
# 이름
# 강감찬  20.0  30.0
# 홍길동   NaN   NaN
# 박영희   NaN   NaN
# 김철수  50.0  60.0

print()
print(myframe.dropna(axis=1, how="any")) #해당 열(axis=1)에서 하나 이상의 결측치가 있으면 해당 열을 삭제하라는 의미
# Empty DataFrame
# Columns: []
# Index: [강감찬, 홍길동, 박영희, 김철수]