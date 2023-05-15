import numpy as np
from pandas import DataFrame

mydata = [[60.00, np.nan, 90.00], [np.nan, 80.00, 50.00], [40.00, 50.00, np.nan]] # 3*3행렬
myindex =['강감찬', '김유신', '이순신']
mycolumn = ['국어', '영어', '수학']

#index_col 매개변수: 파일에서 읽어온 데이터를 데이터프레임의 인덱스로 사용하고자 할 때 사용(인덱스로 사용할 파일의 열이름)
# columns 매개변수: 파일에서 읽어온 데이터를 데이터프레임의 열 이름으로 사용하고자 할 때 사용

myframe = DataFrame(data=mydata, index=myindex, columns=mycolumn)
print('\nBefore')
print(myframe)
#        국어    영어    수학
# 강감찬  60.0   NaN  90.0
# 김유신   NaN  80.0  50.0
# 이순신  40.0  50.0   NaN

#.mean() 메서드: 평균값을 계산하여 반환
myframe.loc[myframe['국어'].isnull(),'국어'] = myframe['국어'].mean()
# myframe['국어'].isnull(): myframe에서 국어 column의 값이 결측값인지 여부를 불리언 마스크로 반환 => 결측값이 True
# 국어 column이 결측값인 행에 대해서만 국어 column을 선택하여, 그 값을 국어 column 전체의 평균값으로 대체
myframe.loc[myframe['영어'].isnull(),'영어'] = myframe['영어'].mean()
myframe.loc[myframe['수학'].isnull(),'수학'] = myframe['수학'].mean()

print('\nAfter')
print(myframe)
#        국어    영어    수학
# 강감찬  60.0  65.0  90.0
# 김유신  50.0  80.0  50.0
# 이순신  40.0  50.0  70.0
print('-' * 40)

#.describe() 메소드: 기초 통계 정보를 출력
# count: 해당 column에 값이 있는 데이터 개수
# mean: 해당 column의 평균값
# std: 해당 column의 표준편차
# min: 해당 column의 최솟값
# 25%: 해당 column의 하위 25% 지점 값
# 50%: 해당 column의 중간값 (50% 지점 값)
# 75%: 해당 column의 상위 25% 지점 값
# max: 해당 column의 최댓값
print(myframe.describe())
#          국어    영어    수학
# count   3.0   3.0   3.0
# mean   50.0  65.0  70.0
# std    10.0  15.0  20.0
# min    40.0  50.0  50.0
# 25%    45.0  57.5  60.0
# 50%    50.0  65.0  70.0
# 75%    55.0  72.5  80.0
# max    60.0  80.0  90.0