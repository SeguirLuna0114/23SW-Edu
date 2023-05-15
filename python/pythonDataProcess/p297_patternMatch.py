import re

mylist = ['ab123', 'cd456', 'ef789', 'adc12']

regex = '[a-z]{2}\d{3}' # 알파벳 2개와 숫자 3개가 반복되는 패턴
# [a-z]: 소문자 알파벳을 의미
#{2}: 앞의 문자 또는 문자열이 2회 반복되는 것 의미
# \d : 숫자를 의미
#{3}: 앞의 문자 또는 문자열이 3회 반복되는 것 의미
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

#mylist에 있는 각각의 문자열이 regex 변수에서 지정한 정규표현식 패턴에 맞는지 확인 -> 맞으면 totallist 리스트에 추가
print('# 문자열 2개, 숫자 3개 패턴 찾기')
totallist = []
for item in mylist:
    #.match()메소드: 리스트의 각 항목을 확인하면서 일치하는지 검사
    if pattern.match(item): #일치하는 경우
        print(item, '은(는) 조건에 적합')
        totallist.append(item) #totallist 리스트에 해당항목 추가
        # ab123 은(는) 조건에 적합
        # cd456 은(는) 조건에 적합
        # ef789 은(는) 조건에 적합
    else: #일치하지 않는 경우
        print(item, '은(는) 조건에 부적합')
        # adc12 은(는) 조건에 부적합

print('\n# 조건에 적합한 항목들')
print(totallist)
# ['ab123', 'cd456', 'ef789']