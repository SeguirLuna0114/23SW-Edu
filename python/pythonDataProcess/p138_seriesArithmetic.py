from pandas import Series, DataFrame

myindex1 = ['강호민', '유재준', '김제명', '신동진']
mylist1 = [30, 40, 50, 60]

myindex2= ['강호민', '유재준', '김제명', '이수진']
mylist2 = [20, 40, 60, 70]

myseries1 = Series(data=mylist1, index=myindex1)
myseries2 = Series(data=mylist2, index=myindex2)

print('\n# data of series1')
print(myseries1)
# 강호민    30
# 유재준    40
# 김제명    50
# 신동진    60
# dtype: int64

print('\n# data of series2')
print(myseries2)
# 강호민    20
# 유재준    40
# 김제명    60
# 이수진    70
# dtype: int64

#arithmetic - Pandas에서는 많은 연산이 메소드나 연산자 둘 다로 구현가능
# add()메소드 & '+'연산자
print(myseries1 + 5) #myseries1의 모든 요소에 5를 더한 값을 출력
# 강호민    35
# 유재준    45
# 김제명    55
# 신동진    65
# dtype: int64
print('-' * 50) #'-'가 50개 출력됨

print(myseries1.add(5)) #print(myseries1 + 5)와 같은 결과 출력
# 강호민    35
# 유재준    45
# 김제명    55
# 신동진    65
# dtype: int64
print('-' * 50)

# sub() 메소드 & '-' 연산자
print(myseries1 - 10) #myseries1의 모든 요소에 10를 뺀 값을 출력
# 강호민    20
# 유재준    30
# 김제명    40
# 신동진    50
# dtype: int64
print('-' * 50)

print(myseries1 * 2) #myseries1의 모든 요소에 2를 곱한 값을 출력
# 강호민     60
# 유재준     80
# 김제명    100
# 신동진    120
# dtype: int64
print('-' * 50)

print(myseries1 / 3) #myseries1의 모든 요소에 3를 나눈 값을 출력
# 강호민    10.000000
# 유재준    13.333333
# 김제명    16.666667
# 신동진    20.000000
# dtype: float64 ('/'연산자는 출력값을 실수형으로 생성)
print('-' * 50)

# relation operation
print(myseries1 >= 40) # myseries1의 각 원소가 40보다 크거나 같은지 여부를 True/False로 반환
# 강호민    False
# 유재준     True
# 김제명     True
# 신동진     True
# dtype: bool (해당 연산 결과를 나타내기 위해 참(True)을 1, 거짓(False)을 0으로 표현)
print('-' * 50)

print('\nadd of series(if nodata then NaN)')
newseries = myseries1 + myseries2 #두 개의 Series 객체의 index가 서로 다르기 때문에 같은 index에 대해서만 연산을 수행. 나머지 index는 NaN 값을 가짐
print(newseries)
# 강호민     50.0
# 김제명    110.0
# 신동진      NaN
# 유재준     80.0
# 이수진      NaN ('이수진' index에 대해서는 myseries1에는 없고, myseries2에는 있기에 NaN으로 표기)
# dtype: float64

print('\nsub of series(operation after fill value 0)')
newseries = myseries1.sub(myseries2, fill_value = 0) #myseries1 - myseries2 결과를 새로운 Series 객체에 저장. #fill_value=0: myseries2에 있는 인덱스가 myseries1에는 없을 때, 뺄셈 결과를 0으로 처리하도록 지정
print(newseries)
# 강호민    10.0
# 김제명   -10.0
# 신동진    60.0
# 유재준     0.0
# 이수진   -70.0
# dtype: float64