import pandas as pd

mystorefile = 'store.csv'
#csv파일을 읽어 데이터프레임으로 저장
mystore = pd.read_csv(mystorefile, encoding='utf-8', index_col=0, header=0)
#index_col=0: 인덱스 컬럼은 0번째 열로 지정
#header=0: 헤더는 0번째 행으로 지정
print('\n매장 테이블')
print(mystore) #<-type: 데이터프레임(pandas.core.frame.DataFrame)
#   store  sido gungu address
# 0   진해점  경상남도   진해시  진해시진해동
# 1   창원점  경상남도   창원시  창원시팔용동
# 2   여주점   경기도   여주시  여주시행복동
# 3  신여주점   경기도   여주시  여주시망원동

districtfile = 'districtmini.csv'
#csv파일을 읽어 데이터프레임으로 저장
district = pd.read_csv(districtfile, encoding='utf-8', index_col=0, header=0)
#index_col=0: 인덱스 컬럼은 0번째 열로 지정
#header=0: 헤더는 0번째 행으로 지정
print('\n행정구역 테이블')
print(district) #<-type: 데이터프레임(pandas.core.frame.DataFrame)
#      gungu
# sido
# 경상남도   창원시
# 경기도    여주시

#pd.merge()함수: 두 개 이상의 데이터프레임을 합치는데 사용.여러 개의 매개변수를 설정하여 합치는 방식을 지정 가능
result = pd.merge(mystore, district, on=['sido','gungu'], how='outer', suffixes=['','_'], indicator=True)
# on: 병합 기준이 되는 열 또는 열의 [리스트]
# how: 병합 방식을 지정-옵션:'inner'(기본값. 공통된 값만을 기준으로 병합), 'outer'(두 데이터프레임의 모든 행을 포함하는 기준으로 병합), 'left', 'right'
# suffixes: 열 이름 충돌 시 구분을 위해 각 데이터프레임의 열에 붙일 '접미사'를 지정. 접미사 붙이지 않을 경우에는 ''로 표기
# indicator: 결과에 합침 정보를 추가하기 위한 매개변수. True-merge열에는 합치는 과정에서 각 행의 상태가 표기됨

print('\nMerge Result')
print(result)
#   store  sido gungu address     _merge
# 0   진해점  경상남도   진해시  진해시진해동  left_only
# 1   창원점  경상남도   창원시  창원시팔용동       both
# 2   여주점   경기도   여주시  여주시행복동       both
# 3  신여주점   경기도   여주시  여주시망원동       both

#query함수: (문자열로 지정한)특정 조건을 만족하는 행을 필터링하는 작업을 수행
m_result = result.query('_merge == "left_only"') #_merge 열의 값이 "left_only"인 행만 선택
print('\n좌측에만 있는 행')
print(m_result)
#   store  sido gungu address     _merge
# 0   진해점  경상남도   진해시  진해시진해동  left_only

#파일 열기
gungufile = open('./gungufile.txt', encoding='utf-8')
gungu_list = gungufile.readlines() #readlines(): 한 줄씩 읽어와 문자열 리스트 항목으로 저장

gungu_dict = {} #빈 딕셔너리를 생성
for onegu in gungu_list: #gungu_list의 항목에 대해서 반복문 실행
    mydata = onegu.replace('\n', '').split(':') #replace함수를 이용하여 개행문자(\n)를 공백으로 대체(제거함). #split(':'): 콜론(:) 기준으로 분할
    gungu_dict[mydata[0]] = mydata[1] #mydata의 1번째 데이터를 key값으로, mydata의 2번째 데이터를 value값으로 추가
print('\n군구 사전 내용')
print(gungu_dict)
# {'진해시': '창원시', '마산시': '창원시', '여주군': '여주시'}

# lambda 함수를 적용
mystore.gungu = mystore.gungu.apply(lambda data : gungu_dict.get(data, data)) #입력값으로 받은 data를 gungu_dict에서 찾아 해당 값으로 변환. gungu_dict에서 찾을 수 있는 값은 변환하고, 없는 값은 그대로 유지
 # -> mystore.gungu.apply(): 'gungu' 열의 각 항목에 대해 지정된 함수를 적용

print('\n수정된 가게 정보 출력')
print(mystore)
#   store  sido gungu address
# 0   진해점  경상남도   창원시  진해시진해동
# 1   창원점  경상남도   창원시  창원시팔용동
# 2   여주점   경기도   여주시  여주시행복동
# 3  신여주점   경기도   여주시  여주시망원동