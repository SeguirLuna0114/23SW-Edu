from konlpy.tag import Komoran

sentence = '코로나 바이러스 태블릿 PC, 설진욱, 가나다라'
print('# before user dic')
komo = Komoran()
print(komo.pos(sentence))
# [('코로나', 'NNP'), ('바이러스', 'NNP'), ('태블릿 PC', 'NNP'), (',', 'SP'), ('설', 'NNB'), ('진', 'NNP'), ('욱', 'NA'), (',', 'SP'), ('가나', 'NNP'), ('다라', 'NNP')]
print('-' * 40)

komo = Komoran(userdic='user_dic.txt')
print('# after user dic')
print(komo.pos(sentence))
# [('코로나 바이러스', 'NNP'), ('태블릿 PC', 'NNP'), (',', 'SP'), ('설진욱', 'NNP'), (',', 'SP'), ('가나다라', 'NNP')]
print('-' * 40)

print('# komo.nouns')
result = komo.nouns(sentence)
print(result)
# ['코로나 바이러스', '태블릿 PC', '설진욱', '가나다라']
print('-' * 40)

print('# komo.morphs')
result = komo.morphs(sentence)
print(result)
# ['코로나 바이러스', '태블릿 PC', ',', '설진욱', ',', '가나다라']
print('-' * 40)