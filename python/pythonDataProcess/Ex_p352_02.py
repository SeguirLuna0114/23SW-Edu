import pandas as pd
from pandas import DataFrame

#DataFrame() 함수를 사용 => 딕셔너리(dict) 데이터를 데이터프레임(DataFrame)으로 변환
# 이때, key -> column으로, value -> row로 정렬됨
dict1 = {'name':['김유신', '김유신', '이순신', '박영효', '이순신', '이순신', '김유신'], 'korean': [60, 50, 40, 80, 30, 55, 45]} # 2개의 key(name, korean)를 갖는 딕셔너리
df1 = DataFrame(dict1) #dict1 딕셔너리 데이터를 데이터프레임으로 변환 => 데이터프레임은 'name'과 'korean' 두 개의 열(column)을 가지며, 각 열에 따라 해당되는 값들이 행(row)으로 정렬

dict2 = {'name':['이순신', '김유신', '신사임당'], 'english':[60, 55, 80]} # 2개의 key(name, english)를 갖는 딕셔너리
df2 = DataFrame(dict2) #dict2 딕셔너리 데이터를 데이터프레임으로 변환 => 데이터프레임은 'name'과 'english' 두 개의 열(column)을 가지며, 각 열에 따라 해당되는 값들이 행(row)으로 정렬

print('\n# DataFrame 출력 01')
print(df1)
#   name  korean
# 0  김유신      60
# 1  김유신      50
# 2  이순신      40
# 3  박영효      80
# 4  이순신      30
# 5  이순신      55
# 6  김유신      45

print('\n# DataFrame 출력 02')
print(df2)
#    name  english
# 0   이순신       60
# 1   김유신       55
# 2  신사임당       80

#merge() 함수를 사용 => 데이터프레임을 병합하는 것
#on='열 이름' : '열 이름'의 열을 기준으로 병합을 수행
print('\n# merge() 메소드의 on="name"을 이용하여 데이터 합치기')
print(pd.merge(df1, df2, on='name')) # df1과 df2라는 두 개의 데이터프레임을 'name' 열을 기준으로 병합한 새로운 데이터프레임 생성
#   name  korean  english
# 0  김유신      60       55
# 1  김유신      50       55
# 2  김유신      45       55
# 3  이순신      40       60
# 4  이순신      30       60
# 5  이순신      55       60

#how= 를 통해 병합 방법(method)을 지정 가능
# how='outer': 왼쪽 데이터프레임(df1)과 오른쪽 데이터프레임(df2) 모두에 해당되는 모든 데이터를 포함하는 외부 조인을 수행. 데이터가 존재하지 않을 경우 NaN(결측값)으로 처리
print('\n# merge() 메소드의 how="outer"을 이용하여 데이터 합치기')
print(pd.merge(df1, df2, how='outer'))
#    name  korean  english
# 0   김유신    60.0     55.0
# 1   김유신    50.0     55.0
# 2   김유신    45.0     55.0
# 3   이순신    40.0     60.0
# 4   이순신    30.0     60.0
# 5   이순신    55.0     60.0
# 6   박영효    80.0      NaN #데이터가 존재하지 않을 경우 NaN(결측값)으로 처리
# 7  신사임당     NaN     80.0