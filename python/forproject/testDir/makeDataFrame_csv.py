import numpy as np
import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt

filename = 'CNCapaData_Transposed_All.csv'

#index_col 매개변수: DataFrame에서 index로 사용할 열을 지정
print('\n#누락된 데이터 샘플 데이터프레임')
csvDataframe = pd.read_csv(filename, index_col='구분') #이름 열을 index로 사용
csvDataframe.index.name = '년도(YYY년 M월)'
csvDataframe.columns.name = '공장가동(FabCapa)'
print(csvDataframe)
# 공장가동(FabCapa)  방직 당월 (억 미터)  방직 누계 (억 미터)  ...  핸드폰 전년동기대비 증가율 (%)  핸드폰 누계 증가율(%)
# 년도(YYY년 M월)                              ...
# 2017년 7월               60.2         216.8  ...                 4.1            9.8
# 2017년 8월               62.9         280.0  ...                 0.0            9.1

# fillna() 메소드: DataFrame이나 Series에서 결측치를 지정된 값으로 대체
#inplace=False: 원본 데이터프레임은 변경되지 않고, 새로운 데이터프레임이 반환 => 원본은 결측치가 있는 상태로 유지됨
#print('\n fillna() 메소드 이용')
#print(csvDataframe.fillna(0, inplace=False)) #결측치를 0으로 대체한 새로운 데이터프레임을 반환

#inplace=True: inplace 매개변수가 True인 경우 반환값을 따로 할당하지 않고 원본 데이터프레임을 변경
print('\n#fillna(inplace=True) 이므로 원본 변동이 생김.')
csvDataframe.fillna(0, inplace=True) #myframe의 NaN 값이 모두 0으로 대체되어 원본이 변경되어 출력됨
print(csvDataframe)

print('\n#csv데이터프레임의 열 list')
print(csvDataframe.columns)

x_axis_data = input('x축 데이터를 입력해주세요. : ')

year_data = input('연도(YYYY)를 입력해주세요. : ')
month_data = input('월(M)을 입력해주세요. : ')
target_date = f'{year_data}년 {month_data}월'
print(target_date)
#target = pd.to_datetime(target_date).strftime('%년 %m월')
#y_axis_data = csvDataframe.loc[target_date, :]
print(y_axis_data)

csvDataframe.plot(x=x_axis_data, y='년도(year-MM)',kind='')
