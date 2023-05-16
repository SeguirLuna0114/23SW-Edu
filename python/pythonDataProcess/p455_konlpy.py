from konlpy.tag import Komoran #Komoran 클래스를 konlpy.tag 모듈에서 import

#Komoran 형태소 분석기를 사용하여 형태소 단위로 분석하고, 분석 결과를 출력
sentence = '코로나 바이러스 태블릿 PC, 설진욱, 가나다라'
print('# before user dic') # 분석할 문장을 sentence 변수에 할당
komo = Komoran() #Komoran 클래스의 객체를 생성하여 komo 변수에 할당
#.pos()메서드: 주어진 문장을 형태소 단위로 분석하여 (형태소, 품사) 형태의 튜플로 반환
print(komo.pos(sentence)) #komo.pos(sentence)를 호출하여 문장의 형태소를 분석
# [('코로나', 'NNP'), ('바이러스', 'NNP'), ('태블릿 PC', 'NNP'), (',', 'SP'), ('설', 'NNB'), ('진', 'NNP'), ('욱', 'NA'), (',', 'SP'), ('가나', 'NNP'), ('다라', 'NNP')]
print('-' * 40)

komo = Komoran(userdic='user_dic.txt') #userdic 매개변수에 'user_dic.txt'라는 사용자 사전 파일을 지정
print('# after user dic')
print(komo.pos(sentence)) #문장의 형태소를 분석
# [('코로나 바이러스', 'NNP'), ('태블릿 PC', 'NNP'), (',', 'SP'), ('설진욱', 'NNP'), (',', 'SP'), ('가나다라', 'NNP')]
print('-' * 40)

#Komoran 형태소 분석기를 사용하여 문장에서 명사만 추출
print('# komo.nouns')
#nouns() 메서드: 주어진 문장에서 명사만 추출하여 리스트로 반환
result = komo.nouns(sentence)
print(result)
# ['코로나 바이러스', '태블릿 PC', '설진욱', '가나다라']
print('-' * 40)

#morphs() 메서드: 주어진 문장을 형태소 단위로 분석하여 리스트로 반환
print('# komo.morphs')
result = komo.morphs(sentence)
print(result)
# ['코로나 바이러스', '태블릿 PC', ',', '설진욱', ',', '가나다라']
print('-' * 40)