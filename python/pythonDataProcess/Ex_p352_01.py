import pandas as pd

afile = 'data03.csv'
bfile = 'data04.csv'

#read_csv()함수: csv파일을 읽어와 데이터프레임 객체로 변환
# header: 첫 번째 행을 헤더로 사용할지 여부를 지정
# encoding: 파일의 인코딩 방식을 지정(utf-8 방식으로 인코딩된 파일)
# names: 새로운 열 이름을 지정(header=None => 헤더가 없다는 것을 지정한 후)
atable = pd.read_csv(afile, header=0, encoding='utf-8') #afile을 읽어와 atable이라는 데이터프레임으로 변환(첫번째 행이 헤더역할 수행&각 열의 이름으로 사용)
btable = pd.read_csv(bfile, header=None, encoding='utf-8', names=['이름','성별','국어','영어','수학']) #bfile을 읽어와 btable이라는 데이터프레임으로 변환

print(atable)
#     이름  성별  국어  영어  수학
# 0  임하용   1  10  40  20
# 1  최양진   1  20  30  40
# 2  이경식   2  30  40  50
# 3  황진이   2  30  60  20
print('-' * 40)

print(btable)
#      이름  성별  국어  영어  수학
# 0   강호민   1  10  40  20
# 1  신사임당   2  20  30  40
# 2   박영희   2  30  60  20
# 3   심형식   1  60  50  30
print('-' * 40)

#데이터프레임에 열(column)을 추가
atable['반'] = '1반' # atable 데이터프레임에 '반' 열을 추가하고, 모든 행에 '1반' 값을 할당
#     이름  성별  국어  영어  수학   반
# 0  임하용   1  10  40  20  1반
# 1  최양진   1  20  30  40  1반
# 2  이경식   2  30  40  50  1반
# 3  황진이   2  30  60  20  1반

btable['반'] = '2반' # btable 데이터프레임에 '반' 열을 추가하고, 모든 행에 '2반' 값을 할당
#      이름  성별  국어  영어  수학   반
# 0   강호민   1  10  40  20  2반
# 1  신사임당   2  20  30  40  2반
# 2   박영희   2  30  60  20  2반
# 3   심형식   1  60  50  30  2반

mylist = []
mylist.append(atable) #atable 데이터프레임을 mylist에 추가
mylist.append(btable) #btable 데이터프레임을 mylist에 추가

# pd.concat(): 데이터프레임을 합쳐서 새로운 데이터프레임 객체 생성
# objs 인자: 리스트, 튜플, 혹은 딕셔너리 형태로 여러 개의 데이터프레임을 받음
# 수직 방향(axis=0)이나 수평 방향(axis=1)으로 합침
# ignore_index=True: 합쳐진 결과 데이터프레임의 인덱스를 재설정
result = pd.concat(objs=mylist, axis=0, ignore_index=True) #ylist에 있는 두 개의 데이터프레임을 수직 방향으로 합침
print(result) #result 데이터프레임의 '반' 열은 첫 번째 데이터프레임의 모든 행에는 '1반'이 할당되어 있고, 두 번째 데이터프레임의 모든 행에는 '2반'이 할당됨
#      이름  성별  국어  영어  수학   반
# 0   임하용   1  10  40  20  1반
# 1   최양진   1  20  30  40  1반
# 2   이경식   2  30  40  50  1반
# 3   황진이   2  30  60  20  1반
# 4   강호민   1  10  40  20  2반
# 5  신사임당   2  20  30  40  2반
# 6   박영희   2  30  60  20  2반
# 7   심형식   1  60  50  30  2반
print('-' * 40)

# 데이터프레임에서 '이름' 열의 값이 '심형식'인 행의 인덱스를 구함
dropIndex = result[result['이름'] == '심형식'].index
# result['이름']: '이름'의 열값은 시리즈 형태로 반환.
# result['이름'] == '심형식'은 '이름' 열에서 값이 '심형식'인 행에 대한 boolean 마스크를 반환 => True되는 행만 선택
#.index: 해당 행의 인덱스를 반환하여 변수에 저장
print(dropIndex) #'이름' 열의 값이 '심형식'인 행의 인덱스=[7]
# Index([7], dtype='int64')
print('-' * 40)

#.drop()메서드: 인덱스나 열을 삭제할 때 사용
newResult = result.drop(dropIndex)
print(newResult)
#      이름  성별  국어  영어  수학   반
# 0   임하용   1  10  40  20  1반
# 1   최양진   1  20  30  40  1반
# 2   이경식   2  30  40  50  1반
# 3   황진이   2  30  60  20  1반
# 4   강호민   1  10  40  20  2반
# 5  신사임당   2  20  30  40  2반
# 6   박영희   2  30  60  20  2반
print('-' * 40)

filename = 'result.csv'
newResult.to_csv(filename, encoding='utf-8')
print(filename + ' saved...')
# result.csv saved...
