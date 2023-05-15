from pandas import Series, DataFrame

myindex1 = ['성춘향', '이몽룡', '심봉사']
mylist1 = [40, 50, 60]

myindex2 = ['성춘향', '이몽룡', '뺑덕어멈']
mylist2 = [20, 40, 70]

myseries1 = Series(data=mylist1, index=myindex1)
myseries2 = Series(data=mylist2, index=myindex2)

print('\n# 시리즈 01')
print(myseries1)
# 성춘향    40
# 이몽룡    50
# 심봉사    60
# dtype: int64

print('\n# 시리즈 02')
print(myseries2)
# 성춘향     20
# 이몽룡     40
# 뺑덕어멈    70
# dtype: int64

print('\n# 두 시리즈 덧셈')
newseries = myseries1.add(myseries2, fill_value = 10)
print(newseries)
# 뺑덕어멈    80.0
# 성춘향     60.0
# 심봉사     70.0
# 이몽룡     90.0
# dtype: float64

print('\n# 두 시리즈 뺄셈')
newseries = myseries1.sub(myseries2, fill_value = 30)
print(newseries)
# 뺑덕어멈   -40.0
# 성춘향     20.0
# 심봉사     30.0
# 이몽룡     10.0
# dtype: float64