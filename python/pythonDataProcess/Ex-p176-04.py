from pandas import DataFrame

sdata = {
    '국어' : [40, 60, 80, 50, 30],
    '영어' : [55, 65, 75, 85, 60],
    '수학' : [30, 40, 50, 60, 70]
}

myindex = ['강감찬', '이순신', '김유신', '김구', '안중근']
myframe = DataFrame(sdata, index=myindex)
print(myframe)
#      국어  영어  수학
# 강감찬  40  55  30
# 이순신  60  65  40
# 김유신  80  75  50
# 김구   50  85  60
# 안중근  30  60  70

print('\n짝수 행만 읽어보세요.')
result = myframe.iloc[0::2]
print(result)
#      국어  영어  수학
# 강감찬  40  55  30
# 김유신  80  75  50
# 안중근  30  60  70

print('\n이순신 행만 시리즈로 읽어보세요.')
result = myframe.loc[['이순신']]
print(result)
#      국어  영어  수학
# 이순신  60  65  40

print('\n강감찬의 영어 점수를 읽어보세요.')
result = myframe.loc[['강감찬'],['영어']]
print(result)
#      영어
# 강감찬  55

print('\n안중근과 강감찬의 국어/수학 점수를 읽어보세요.')
result = myframe.loc[['안중근', '강감찬'],['국어', '수학']]
print(result)
#      국어  수학
# 안중근  30  70
# 강감찬  40  30

print('\n이순신과 강감찬의 영어 점수를 80으로 변경하세요.')
result = myframe.loc[['이순신', '강감찬'],['영어']] = 80
print(myframe)
#      국어  영어  수학
# 강감찬  40  80  30
# 이순신  60  80  40
# 김유신  80  75  50
# 김구   50  85  60
# 안중근  30  60  70

print('\n이순신부터 김구까지 수학 점수를 100으로 변경하세요.')
result = myframe.loc['이순신' : '김구',['수학']] = 100
print(myframe)
#      국어  영어   수학
# 강감찬  40  80   30
# 이순신  60  80  100
# 김유신  80  75  100
# 김구   50  85  100
# 안중근  30  60   70