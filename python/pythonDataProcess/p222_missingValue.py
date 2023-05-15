import numpy as np
import pandas as pd
from pandas import Series

filename = "excel02.csv"

#index_col 매개변수: DataFrame에서 index로 사용할 열을 지정
print('\n 누락된 데이터 샘플 데이터프레임')
myframe = pd.read_csv(filename, index_col='이름') #이름 열을 index로 사용
print(myframe)
#        국어    영어    수학
# 이름
# 강감찬  10.0  20.0  30.0
# 홍길동  40.0   NaN   NaN
# 박영희   NaN   NaN   NaN
# 김철수   NaN  50.0  60.0

# fillna() 메소드: DataFrame이나 Series에서 결측치를 지정된 값으로 대체
#inplace=False: 원본 데이터프레임은 변경되지 않고, 새로운 데이터프레임이 반환 => 원본은 결측치가 있는 상태로 유지됨
print('\n fillna() 메소드 이용')
print(myframe.fillna(0, inplace=False)) #결측치를 0으로 대체한 새로운 데이터프레임을 반환
#        국어    영어    수학
# 이름
# 강감찬  10.0  20.0  30.0
# 홍길동  40.0   0.0   0.0
# 박영희   0.0   0.0   0.0
# 김철수   0.0  50.0  60.0

print('\n# inplace=False 이므로 원본 변동은 없음.')
print(myframe)
#        국어    영어    수학
# 이름
# 강감찬  10.0  20.0  30.0
# 홍길동  40.0   NaN   NaN
# 박영희   NaN   NaN   NaN
# 김철수   NaN  50.0  60.0

#inplace=True: inplace 매개변수가 True인 경우 반환값을 따로 할당하지 않고 원본 데이터프레임을 변경
print('\n# inplace=True 이므로 원본 변동이 생김.')
myframe.fillna(0, inplace=True) #myframe의 NaN 값이 모두 0으로 대체되어 원본이 변경되어 출력됨
print(myframe)
#        국어    영어    수학
# 이름
# 강감찬  10.0  20.0  30.0
# 홍길동  40.0   0.0   0.0
# 박영희   0.0   0.0   0.0
# 김철수   0.0  50.0  60.0

print('\n 누락된 데이터 샘플 데이터프레임')
myframe.loc[['강감찬', '홍길동'], ['국어', '영어']] = np.nan
myframe.loc[['박영희', '김철수'], ['수학']] = np.nan
print(myframe)
#       국어    영어    수학
# 이름
# 강감찬  NaN   NaN  30.0
# 홍길동  NaN   NaN   0.0
# 박영희  0.0   0.0   NaN
# 김철수  0.0  50.0   NaN

print('\n# 임의의 값을 다른 값으로 치환')
print('\n# 국어, 영어, 수학 컬럼의 NaN 값들을 일괄 변경')
mydict = {'국어':15, '영어':25, '수학':35}
myframe.fillna(mydict, inplace=True) #mydict에 저장된 값으로 NaN값(결측값)을 대체
print(myframe)
#        국어    영어    수학
# 이름
# 강감찬  15.0  25.0  30.0
# 홍길동  15.0  25.0   0.0
# 박영희   0.0   0.0  35.0
# 김철수   0.0  50.0  35.0
print('-' * 40)

myframe.loc[['박영희'],['국어']] = np.nan
myframe.loc[['홍길동'],['영어']] = np.nan
myframe.loc[['김철수'],['수학']] = np.nan

print(myframe)
#        국어    영어    수학
# 이름
# 강감찬  15.0  25.0  30.0
# 홍길동  15.0   NaN   0.0
# 박영희   NaN   0.0  35.0
# 김철수   0.0  50.0   NaN
print('-' * 40)

mydict = {'국어': np.ceil(myframe['국어'].mean()),
          '영어': np.ceil(myframe['영어'].mean()),
          '수학': np.ceil(myframe['수학'].mean())}

myframe.fillna(mydict, inplace=True) #mydict에 저장된 값으로 NaN값(결측값)을 대체
print(myframe)
#        국어    영어    수학
# 이름
# 강감찬  15.0  25.0  30.0
# 홍길동  15.0  25.0   0.0
# 박영희  10.0   0.0  35.0
# 김철수   0.0  50.0  22.0
print('-' * 40)