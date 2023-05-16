import pandas as pd

afile = 'cheogajip.csv'
bfile = 'pelicana.csv'

#csv파일을 읽어 데이터프레임으로 저장
atable = pd.read_csv(afile, index_col=0, header=0, encoding='utf-8')
#index_col=0: 인덱스 컬럼은 0번째 열로 지정
#header=0: 헤더는 0번째 행으로 지정
btable = pd.read_csv(bfile, index_col=0, header=0, encoding='utf-8')
#index_col=0: 인덱스 컬럼은 0번째 열로 지정
#header=0: 헤더는 0번째 행으로 지정

print(atable) #<-type: 데이터프레임(pandas.core.frame.DataFrame)
#           brand  ...         phone
# 0     cheogajip  ...  031-582-7114
# 1     cheogajip  ...  031-862-9902
# 2     cheogajip  ...   02-455-8292
# ...         ...  ...           ...
# 1233  cheogajip  ...  033-452-5592
# 1234  cheogajip  ...  043-642-6992
# 1235  cheogajip  ...  043-535-9998
# [1236 rows x 6 columns]
print('-' * 50)

print(btable) #<-type: 데이터프레임(pandas.core.frame.DataFrame)
#          brand  ...         phone
# 0     pelicana  ...  043-233-4091
# 1     pelicana  ...  031-883-5746
# 2     pelicana  ...  031-855-6126
# ...        ...  ...           ...
# 1047  pelicana  ...  033-763-4291
# 1048  pelicana  ...  031-903-1333
# 1049  pelicana  ...   02-123-1234
# [1050 rows x 6 columns]
print('-' * 50)

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
#           brand  ...         phone
# 0     cheogajip  ...  031-582-7114
# 1     cheogajip  ...  031-862-9902
# 2     cheogajip  ...   02-455-8292
# ...         ...  ...           ...
# 2283   pelicana  ...  033-763-4291
# 2284   pelicana  ...  031-903-1333
# 2285   pelicana  ...   02-123-1234
# [2286 rows x 6 columns]

filename = 'ChickenResult.csv'
result.to_csv(filename, encoding='utf-8')
print(filename+' saved...')
