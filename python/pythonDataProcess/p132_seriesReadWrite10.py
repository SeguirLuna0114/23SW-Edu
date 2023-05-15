from pandas import Series

myindex = ['용산구', '마포구', '영등포구', '서대문구', '광진구', '은평구', '서초구'] #문자열 요소 list 생성
mylist = [50, 60 , 40, 80, 70, 30, 20] #정수형 요소 list 생성
myseries = Series(data=mylist, index=myindex) # myindex라는 인덱스로 mylist의 값을 가지는 Series 생성
print(myseries)
#용산구     50
#마포구     60
#영등포구    40
#서대문구    80
#광진구     70
#은평구     30
#서초구     20
#dtype: int64 #데이터타입은 data에 할당된 list가 정수형이기에 46비트의 정수형 데이터 타입으로 생성됨

print('\nread value')
print(myseries[['서대문구']]) # '서대문구'인덱스를 갖는 값만 출력됨(['서대문구']는 문자열)
# 서대문구    80
# dtype: int64

#Pandas에서는 인덱스 기반 slicing이 가능함
print('\nslicing label name')
print(myseries['서대문구':'은평구']) #서대문구~은평구까지의 인덱스를 가진 데이터만 출력
# 서대문구    80
# 광진구     70
# 은평구     30
# dtype: int64

#특정 인덱스를 가진 데이터만 선택하여 출력
print('\ndata read')
print(myseries[['서대문구','서초구']]) #['서대문구', '서초구'] 인덱스를 가진 데이터만 선택하여 출력
# 서대문구    80
# 서초구     20
# dtype: int64

#특정 인덱스 요소에 대한 슬라이싱 수행
print('\nread index')
print(myseries[[2]]) #인덱스가 2인 '영등포구' 요소에 대한 값인 40을 가진 시리즈 형태의 객체가 반환
# 영등포구    40
# dtype: int64

print('\nread index 0, 2, 4')
print(myseries[0:5:2]) # 0부터 5까지(5는 포함X) 2의 간격으로 인덱싱하여 출력 => 인덱스가 0, 2, 4인 요소 출력
# 용산구     50
# 영등포구    40
# 광진구     70
# dtype: int64

print('\nread index 1, 3, 5')
print(myseries[[1, 3, 5]]) #인덱스가 1, 3, 5인 요소 출력
# 마포구     60
# 서대문구    80
# 은평구     30
# dtype: int64

print('\nslicing')
print(myseries[3:6]) #3~5번째 인덱스까지의 값을 출력
# 서대문구    80
# 광진구     70
# 은평구     30
# dtype: int64

#Series 값 변경
myseries[2] = 90 # 2번째 인덱스에 해당하는 40을 90으로 변경
myseries[2:5] = 33 # 2번째 인덱스부터 5번째 인덱스까지의 값들을 모두 33으로 변경
myseries[['용산구', '서대문구']] = 55 #'용산구'와 '서대문구'의 값을 모두 55로 변경
myseries[0::2] = 80 #첫 번째 인덱스부터 끝까지, 두 칸씩 건너뛰며 해당하는 값들을 모두 80으로 변경
print('\nSeries list')
print(myseries)
# 용산구     80
# 마포구     60
# 영등포구    80
# 서대문구    55
# 광진구     80
# 은평구     30
# 서초구     80
# dtype: int64