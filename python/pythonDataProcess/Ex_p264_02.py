import re

mylist = ['ab123', 'cd4#6', 'cf79a', 'adc1']

regex = '[ac]{1}\w{4}'
pattern = re.compile(regex)

print('# 문자 a 또는 c로 시작하고, 이후 숫자 또는 알파벳이 4개로 끝나는 패턴 찾기')
totallist = []
for item in mylist:
    if pattern.match(item):
        print(item, '은(는) 조건에 적합')
        totallist.append(item)
        # ab123 은(는) 조건에 적합
        # cf79a 은(는) 조건에 적합
    else:
        print(item, '은(는) 조건에 부적합')
        # cd4#6 은(는) 조건에 부적합
        # adc1 은(는) 조건에 부적합

print('\n# 조건에 적합한 항목들')
print(totallist)
# ['ab123', 'cf79a']
print('-' * 50)