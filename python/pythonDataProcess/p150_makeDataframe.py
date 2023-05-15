from pandas import DataFrame as dp
import numpy as np

#DataFrame() 함수를 이용하여 데이터프레임 객체로 변환
mydata = np.arange(9).reshape((3, 3)) #0~8까지 정수를 3*3형태의 2차원 배열 생성
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
myframe = dp(data=mydata, index=['용산구', '마포구', '은평구'], columns=['김철수', '이영희', '정준수']) # 2차원 배열 mydata를 이용해, index에는 ['용산구', '마포구', '은평구'], columns에는 ['김철수', '이영희', '정준수']를 설정한 DataFrame 객체를 생성
print(myframe)
#      김철수  이영희  정준수
# 용산구    0    1    2
# 마포구    3    4    5
# 은평구    6    7    8
print('-', 50)

#sdata를 이용해 DataFrame 객체 생성
sdata = {'지역' : ['용산구', '마포구'], '연도' : [2019, 2020]} #dictionary 객체로, 지역과 연도라는 key값 갖고있음
myframe = dp(data=sdata)
print(myframe)
#     지역    연도
# 0  용산구  2019
# 1  마포구  2020
print('-', 50)

#sdata를 이용해 DataFrame 객체 생성
sdata = {'용산구' : {2020:10, 2021:20}, '마포구' : {2020:30, 2021:40, 2022:50}}
myframe = dp(data=sdata) #DataFrame객체. sdata를 data로 지정하여 생성 => '지역'과 '연도'라는 두개의 column이 생성되며 sdata의 key값에 대응하는 리스트의 값이 해당 column의 값으로 사용됨
print(myframe)
#        용산구  마포구
# 2020  10.0   30
# 2021  20.0   40
# 2022   NaN   50
print('-', 50)

#sdata를 이용해 DataFrame 객체 생성
sdata = {'지역' : ['용산구', '마포구', '용산구', '마포구', '마포구'], '연도' : [2019, 2020, 2021, 2020, 2021], '실적' : [20, 30, 35, 25, 45]} # dictionary객체로 '지역', '연도', '실적'이라는 key값 갖고있음
myframe = dp(data=sdata) #sdata 딕셔너리의 key값인 '지역', '연도', '실적'은 각각 DataFrame의 열(column)을 구성. 딕셔너리의 value값은 열(column)에 해당하는 값
print(myframe)
#     지역    연도  실적
# 0  용산구  2019  20
# 1  마포구  2020  30
# 2  용산구  2021  35
# 3  마포구  2020  25
# 4  마포구  2021  45
print('-', 50)
