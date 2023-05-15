from pandas import Series

print('\nUnique, count, isin')
mylist = ['라일락', '코스모스', '코스모스', '백일홍', '코스모스', '코스모스', '들장미', '들장미', '라일락', '라일락']
myseries = Series(mylist) #index인자가 없기에 myseries 객체는 리스트의 값들과 그 순서가 그대로 유지되면서, 각 값에 대응하는 인덱스를 자동으로 부여됨
# print(myseries)
# 0     라일락
# 1    코스모스
# 2    코스모스
# 3     백일홍
# 4    코스모스
# 5    코스모스
# 6     들장미
# 7     들장미
# 8     라일락
# 9     라일락
# dtype: object (데이터값이 문자열)

# unique()메소드: 중복되지 않은 값만을 리스트로 반환. 이때 반환값은 중복되지 않은 순서대로 정렬되어 1차원 배열형태로 반환됨
print('\nunique()')
myunique = myseries.unique() #series객체에서 중복을 제거한 값을 반환
print(myunique) # ['라일락' '코스모스' '백일홍' '들장미'] <-numpy.ndarray 1차원 배열로 출력됨

#value_counts() 함수: 시리즈의 값들을 카운트하고, 각각의 값이 나온 빈도수를 계산하여 반환. 반환값은 시리즈 형태
print('\nvalue_count()')
print(myseries.value_counts())
# 코스모스    4 (인덱스 - 값, value- 빈도수)
# 라일락     3
# 들장미     2
# 백일홍     1
# Name: count, dtype: int64

#isin() 메소드: 해당 Series 객체의 값이 주어진 리스트/배열에 포함되는지 여부를 True/False로 반환
print('\nisin()')
mask = myseries.isin(['들장미', '라일락'])
print(mask)
# 0     True
# 1    False
# 2    False
# 3    False
# 4    False
# 5    False
# 6     True
# 7     True
# 8     True
# 9     True
# dtype: bool
print('-' * 50)

print(myseries[mask]) #maks가 '들장미'와 '라일락'이기에, 들장미와 라일락을 갖는 값을 출력
# 0    라일락
# 6    들장미
# 7    들장미
# 8    라일락
# 9    라일락
# dtype: object
print('-' * 50)

print('\nfinished')