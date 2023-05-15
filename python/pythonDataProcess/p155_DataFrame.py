from pandas import DataFrame

#DataFrame을 활용하여 데이터를 생성
sdata = {
    '도시' : ['서울', '서울', '서울', '부산', '부산'],
    '연도' : [2000, 2001, 2002, 2001, 2002],
    '실적' : [150, 170, 360, 240, 290]
} #dictionary 객체 생성
#DataFrame함수는 dictionary를 인자로 받아 데이터프레임 생성
myindex = ['one', 'two', 'three', 'four', 'five']
myframe = DataFrame(sdata, index=myindex) #데이터프레임의 행(row)은 myindex값으로, 열(column)은 sdata의 key값으로 지정됨
print('\nType : ', type(myframe)) #myframe변수에 저장된 데이터자료형 : pandas.core.frame.DataFrame-Pandas에서 제공하는 DataFrame클래스: 2차원데이터를 표형태로 표현
# Type :  <class 'pandas.core.frame.DataFrame'>

#columns.name 으로 pandas DataFrame 객체의 열 이름에 대한 정보 설정
myframe.columns.name = 'Columns1' #데이터프레임 객체인 myframe의 열(칼럼) 이름에 대한 정보를 설정
print('\nColumns Information')
print(myframe.columns) #출력에서는 열이름이 저장된 index와 dtype이 출력
# Index(['도시', '연도', '실적'], dtype='object', name='Columns1')

#index.name으로 pandas DataFrame의 index에 이름 지정
myframe.index.name = 'Index1' #인덱스 이름을 "Index1"로 설정
print('\nIndex Information')
print(myframe.index) #해당 DataFrame의 인덱스 정보를 출력
# Index(['one', 'two', 'three', 'four', 'five'], dtype='object', name='Index1')

#.values 속성 => 해당 DataFrame 내의 데이터를 numpy array 형태로 반환(단순하게 numpy array 형태로 데이터를 다루기 위해 사용)
print('\ninner data Information')
print(type(myframe.values)) # <class 'numpy.ndarray'>
print(myframe.values) #myframe.values: myframe의 데이터를 numpy array 형태로 반환
# [['서울' 2000 150]
#  ['서울' 2001 170]
#  ['서울' 2002 360]
#  ['부산' 2001 240]
#  ['부산' 2002 290]]

#.dtypes 속성 => DataFrame 객체의 각 열(column)의 데이터 타입 정보 출력
print('\nData Type Information')
print(myframe.dtypes) #myframe의 각 열(column)의 데이터 타입 정보를 출력
# Columns1
# 도시    object
# 연도     int64
# 실적     int64
# dtype: object

#Dataframe이 출력됨
print('\nContext Information')
print(myframe) #5개의 행과 3개의 열로 이루어져 있으며, '도시', '연도', '실적'이라는 열 이름을 가지고 있습니다. 인덱스는 'one', 'two', 'three', 'four', 'five'
# Columns1  도시    연도   실적
# Index1
# one       서울  2000  150
# two       서울  2001  170
# three     서울  2002  360
# four      부산  2001  240
# five      부산  2002  290

#.T => 전치(transpose)는 DataFrame의 행과 열을 바꾸는 연산
print('\nrow, col transform')
print(myframe.T) # 열 이름이 행 이름으로, 행 이름이 열 이름으로 바뀜
# Index1     one   two three  four  five
# Columns1
# 도시          서울    서울    서울    부산    부산
# 연도        2000  2001  2002  2001  2002
# 실적         150   170   360   240   290

# 딕셔너리 객체를 이용해 새로운 데이터프레임을 생성
print('\nColumns property usage')
mycolumns = ['실적', '도시', '연도']
newframe = DataFrame(sdata, columns=mycolumns) #newframe의 열 이름은 mycolumns 리스트에 지정된 순서로 지정. 해당 열에 대한 값을 딕셔너리 sdata에서 가져옴
print(newframe)
#     실적  도시    연도
# 0  150  서울  2000
# 1  170  서울  2001
# 2  360  서울  2002
# 3  240  부산  2001
# 4  290  부산  2002