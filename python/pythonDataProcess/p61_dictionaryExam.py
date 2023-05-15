dictionary = {'김유신' : 50, '윤봉길' : 40, '김구' : 60} #dictionary 데이터 타입
print('dictionary list : ', dictionary) #dictionary는 key값 : value값 과 같이 구분

for key in dictionary.keys():
    print(key) #dictionary의 key값 출력

for value in dictionary.values():
    print(value) #dictionary의 value값 출력

for key in dictionary.keys():
    print('{}의 나이는 {}입니다.'.format(key, dictionary[key])) #dictionary[key]: key값에 해당하는 value 출력

print() #빈칸

for key, value in dictionary.items(): #dictionary.items()를 이용해 key값과 value값 모두
    print('{}의 나이는 {}입니다.'.format(key, value))

print() #빈칸

findKey = '유관순'
if findKey in dictionary:
    print(findKey + '(은)는 존재합니다.')
else:
    print(findKey + '(은)는 존재하지 않습니다.') #유관순은 key값에 없음

print() #빈칸

result = dictionary.pop('김구') #key값이 '김구'에 해당하는 값 뽑아냄(삭제)
print('After pop dictionary : ', dictionary) #'김구'key값 및 value값 삭제한 dictionary 출력됨: {'김유신': 50, '윤봉길': 40}
print('pop value :', result) #result값은 '김구'의 value값인 60

print() #빈칸

dictionary.clear() #모든 데이터 삭제
print('dictionary list : ', dictionary) #비어있는 dictionary 출력됨
