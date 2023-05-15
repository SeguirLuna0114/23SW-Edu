from pandas import Series, DataFrame
import numpy as np

myindex = ['윤봉길', '김유신', '신사임당']
mylist = [30, 40, 50]

myseries = Series(data=mylist, index=myindex)
print('\n시리즈의 결과 출력')
print(myseries)
# 윤봉길     30
# 김유신     40
# 신사임당    50
# dtype: int64

myindex = ['윤봉길', '김유신', '이순신']
mycolumns = ['용산구', '마포구', '서대문구']
mylist = list(3 * onedata for onedata in range(1, 10))

myframe = DataFrame(np.reshape(np.array(mylist), (3, 3)), index=myindex, columns=mycolumns)
print('\n데이터프레임 출력')
print(myframe)
#      용산구  마포구  서대문구
# 윤봉길    3    6     9
# 김유신   12   15    18
# 이순신   21   24    27

myindex2 = ['윤봉길', '김유신', '이완용']
mycolumns2 = ['용산구', '마포구', '은평구']
mylist2 = list(5 * onedata for onedata in range(1, 10))

myframe2 = DataFrame(np.reshape(np.array(mylist2), (3, 3)), index=myindex2, columns=mycolumns2)
print('\n데이터프레임2 출력')
print(myframe2)
#      용산구  마포구  은평구
# 윤봉길    5   10   15
# 김유신   20   25   30
# 이완용   35   40   45

print('\nDataframe + Series')
result = myframe.add(myseries, axis = 0)
print(result)
#        용산구   마포구  서대문구
# 김유신   52.0  55.0  58.0
# 신사임당   NaN   NaN   NaN
# 윤봉길   33.0  36.0  39.0
# 이순신    NaN   NaN   NaN

print('\nDataframe + Dataframe')
result = myframe.add(myframe2, fill_value = 20)
print(result)
#       마포구  서대문구   용산구   은평구
# 김유신  40.0  38.0  32.0  50.0
# 윤봉길  16.0  29.0   8.0  35.0
# 이순신  44.0  47.0  41.0   NaN
# 이완용  60.0   NaN  55.0  65.0

print('\nDataframe - Dataframe')
result = myframe.sub(myframe2, fill_value = 10)
print(result)
#       마포구  서대문구   용산구   은평구
# 김유신 -10.0   8.0  -8.0 -20.0
# 윤봉길  -4.0  -1.0  -2.0  -5.0
# 이순신  14.0  17.0  11.0   NaN
# 이완용 -30.0   NaN -25.0 -35.0
