import numpy as np
import pandas as pd
from pandas import Series

filename = 'CNCapaData_Transposed_All.csv'

#index_col 매개변수: DataFrame에서 index로 사용할 열을 지정
print('\n#누락된 데이터 샘플 데이터프레임')
csvDataframe = pd.read_csv(filename, index_col='구분') #이름 열을 index로 사용
print(csvDataframe)
#            방직 당월 (억 미터)  방직 누계 (억 미터)  ...  핸드폰 전년동기대비 증가율 (%)  핸드폰 누계 증가율(%)
# 구분                                     ...
# 2017년 7월           60.2         216.8  ...                 4.1            9.8
# 2017년 8월           62.9         280.0  ...                 0.0            9.1

# fillna() 메소드: DataFrame이나 Series에서 결측치를 지정된 값으로 대체
#inplace=False: 원본 데이터프레임은 변경되지 않고, 새로운 데이터프레임이 반환 => 원본은 결측치가 있는 상태로 유지됨
print('\n fillna() 메소드 이용')
print(csvDataframe.fillna(0, inplace=False)) #결측치를 0으로 대체한 새로운 데이터프레임을 반환

#inplace=True: inplace 매개변수가 True인 경우 반환값을 따로 할당하지 않고 원본 데이터프레임을 변경
print('\n#inplace=True 이므로 원본 변동이 생김.')
csvDataframe.fillna(0, inplace=True) #myframe의 NaN 값이 모두 0으로 대체되어 원본이 변경되어 출력됨
print(csvDataframe)