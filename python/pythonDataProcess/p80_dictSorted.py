wordInfo = {'세탁기' : 50, '선풍기' : 30, '청소기' : 40, '냉장고' : 60} #{}를 이용해 wordInfo dictionary 생성

myxticks = sorted(wordInfo, key=wordInfo.get, reverse=True) #wordInfo 딕셔너리를 value값을 기준으로 내림차순 정렬
#key=wordInfo.get: wordInfo의 각 요소에 대해 그 값을 기준으로 비교
#reverse=True: 값이 큰요소부터 작은순으로 정렬
print(myxticks)

revers_key = sorted(wordInfo.keys(), reverse=True) #key값들을 내림차순으로 정렬하여 list로 반환
print(revers_key)#ㅊ->ㅅ->ㄴ

chartdata = sorted(wordInfo.values(), reverse=True) #wordinfo 딕셔너리 값들을 내림차순정렬
print(chartdata) #60->50->40->30