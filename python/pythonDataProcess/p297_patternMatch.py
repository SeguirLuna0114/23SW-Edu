import re

mylist = ['ab123', 'cd456', 'ef789', 'adc12']

regex = '[a-z]{2}\d{3}'
pattern = re.compile(regex)

### 정규 표현식 플래그
# ^ : start string
# $ : end string
# * : 반복(all)
# + :  반복, 1번 이상
# ?  : 반복, 있거나 없거나
# {} : 반복 횟수
#
# [a-zA-Z] : 알파벳
# [0-9] : 숫자
# [^0-9] : 숫자가 아닌 것
# g : 전역 탐색
# i : 대소문자 구별하지 않음
# \d : 숫자
# \D : 숫자가 아닌 것
# \w :  문자, 숫자
# \W : 문자, 숫자 아닌 것
# \s : white space
# \S : white space 아닌 것
# Dot(.) : \n을 제외한 모든 문자

print('# 문자열 2개, 숫자 3개 패턴 찾기')
totallist = []
for item in mylist:
    if pattern.match(item):
        print(item, '은(는) 조건에 적합')
        totallist.append(item)
        # ab123 은(는) 조건에 적합
        # cd456 은(는) 조건에 적합
        # ef789 은(는) 조건에 적합
    else:
        print(item, '은(는) 조건에 부적합')
        # adc12 은(는) 조건에 부적합

print('\n# 조건에 적합한 항목들')
print(totallist)
# ['ab123', 'cd456', 'ef789']