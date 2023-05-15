from pandas import Series

#Series(): 일련의 데이터와 데이터에 연관된 인덱스를 묶어서 하나의 객체로 표현
mylist = [10, 40, 30, 20] #정수형 원소를 갖는 list 생성
myseries = Series(data=mylist, index= ['김유신', '이순신', '강감찬', '광해군']) # 정수형으로 이루어진 리스트 mylist와 문자열 리스트 ['김유신', '이순신', '강감찬', '광해군']을 사용하여 판다스의 Series를 생성

print('\nData Type')
print(type(myseries)) #데이터타입: pandas.core.series.Series(Pandas 라이브러리의 자료형으로, 1차원 데이터를 다루는 시리즈(Series) 형태

#myseries에 대한 name속성을 설정하여, 해당 시리즈 객체에 대한 이름 지정
myseries.index.name = '점수' #myseries의 '인덱스 이름'을 '점수'로 설정한 후 출력
print('\nindex name of series') #'점수'라는 이름의 인덱스가 설정됨-데이터타입은 문자열('')
print(myseries.index.name) #점수

myseries.name = '학생들 시험' #myseries에 대한 '이름'을 '학생들 시험'으로 설정
print('\nname of series') #'학생들 시험'이라는 이름이 설정됨-데이터타입은 문자열('')
print(myseries.name) #학생들 시험

#myseries.index: myseries의 인덱스를 나타내는 Index 객체를 반환 - Index 객체에는 인덱스의 이름과 데이터타입 등의 속성도 함께 저장되기에 dtype과 name까지 출력됨
print('\nname of index')
print(myseries.index) #Index(['김유신', '이순신', '강감찬', '광해군'], dtype='object', name='점수')
# 인덱스를 출력, dtype(인덱스 데이터타입)이 object(문자열)이며, name(인덱스의 이름)은 '점수'로 설정되어 있음

#myseries.values: myseries 객체의 데이터 값들만 출력
print('\nvalue of series')
print(myseries.values) #[10 40 30 20]: numpy ndarray 데이터 타입 형태로 출력

#Series 객체를 출력 - 인덱스를 가지는 1차원 배열과 유사한 구조. 각 원소에는 순서대로 정의된 인덱스가 매핑됨
print('\nprint information of series')
print(myseries)
# 점수
# 김유신    10 #인덱스와 데이터 값(정수형)
# 이순신    40
# 강감찬    30
# 광해군    20
# Name: 학생들 시험, dtype: int64

# series 객체의 인덱스와 values를 하나씩 순회하며 출력하는 반복문
print('\nrepeat print')
for idx in myseries.index: #myseries의 인덱스 리스트에서 인덱스를 idx에 대입하여 myseries값에 접근
    print('Index : ' + idx + ', Values : ' + str(myseries[idx])) #myseries의 value는 정수형이기에 str을 이용해 문자열로 변환