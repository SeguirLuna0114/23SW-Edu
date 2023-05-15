import re #re 모듈을 불러옴

mylist = ['ab123', 'cd4#6', 'cf79a', 'adc1'] # 문자열 리스트 생성

#정규표현식 패턴을 저장하는 문자열 변수 regex 생성
regex = '[ac]{1}\w{4}'
# '[ac]{1}' : [ ] 안에 존재하는 문자 중 하나를 선택 <-  'a'나 'c' 중 하나를 선택.
#  {1}은 이 문자가 정확히 1번 등장해야 한다는 것 의미(=문자열이 a나 c로 시작해야 함)
# '\w{4}' : \w는 유니코드 글자 문자(character)에 대응(모든 글자에 대응). {4}는 이 글자들이 정확히 4번 등장해야 한다는 것을 나타냄

# re.compile() 메서드: regex에 저장된 정규표현식 패턴을 컴파일하여 pattern 객체를 생성
pattern = re.compile(regex)

print('# 문자 a 또는 c로 시작하고, 이후 숫자 또는 알파벳이 4개로 끝나는 패턴 찾기')
totallist = [] #정규표현식 패턴과 매치되는 문자열 저장하기 위한 빈 리스트 생성
for item in mylist: #mylist에 저장된 각 문자열에 대해서 반복문 실행
    #.match 메소드: 문자열의 시작 부분에서 매치 검색
    if pattern.match(item): #item과 정규표현식 패턴과 매치되는지 확인
        print(item, '은(는) 조건에 적합')
        totallist.append(item) #매치되는 문자열이 있으면 해당 문자열을 totallist 리스트에 추가
        # ab123 은(는) 조건에 적합
        # cf79a 은(는) 조건에 적합
    else: #매치되는 문자열이 없을 경우
        print(item, '은(는) 조건에 부적합')
        # cd4#6 은(는) 조건에 부적합
        # adc1 은(는) 조건에 부적합

print('\n# 조건에 적합한 항목들')
print(totallist)
# ['ab123', 'cf79a']
print('-' * 50)