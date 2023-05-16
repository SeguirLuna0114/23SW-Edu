import pandas as pd

afile = 'android.csv'
bfile = 'iphone.csv'

#csv파일을 읽어 데이터프레임으로 저장
atable = pd.read_csv(afile, encoding='utf-8')
btable = pd.read_csv(bfile, encoding='utf-8')

print(atable) #<-type: 데이터프레임(pandas.core.frame.DataFrame)
#  name  value
# 0  kim    100
# 1  lee    200
print('-' * 50)

print(btable)
#    name  value
# 0  choi    300
# 1  park    400
print('-' * 50)

#dictionary객체에 'key'라는 키를 추가하고 키에 해당되는 value를 할당
atable['phone']='안드로이드' #'phone'이라는 키를 가진 딕셔너리 요소를 생성하고, '안드로이드' value 할당
btable['phone']='아이폰' #'phone'이라는 키를 가진 딕셔너리 요소를 생성하고, '아이폰' value 할당

#.append(): 두개의 table(데이터프레임)을 "순차적으로" 리스트(mylist)에 추가
# -> pd.contact함수가 list를 인자로 받아 이를 연결(concatenate)하여 새로운 테이블(데이터프레임)을 생성
mylist = []
mylist.append(atable) #atable을 mylist에 추가
mylist.append(btable) #btable을 mylist에 추가
result = pd.concat(objs=mylist, axis=0, ignore_index=True)
# pd.concat() 함수: 두 데이터프레임(table)을 수직/세로(axis=0)으로 결합
# objs: 리스트로 전달된 데이터프레임들을 결합
# ignore_index=True: 결합된 데이터프레임의 인덱스를 재설정(reindex하라는 의미)
print(result) #<-type: 데이터프레임(pandas.core.frame.DataFrame)
#    name  value  phone
# 0   kim    100  안드로이드
# 1   lee    200  안드로이드
# 2  choi    300    아이폰
# 3  park    400    아이폰
filename = 'result.csv'
result.to_csv(filename, encoding='utf-8')
print(filename+' saved...')
