import pandas as pd # pandas 라이브러리를 import

#.read_csv함수를 이용하여 파일을 읽어들여서 DataFrame 객체로 변환한 후 출력
filename = 'memberInfo.csv' #filename변수에 memberInfo.csv파일명 저장
df = pd.read_csv(filename) #pd.read_csv함수를 이용하여 DataFrame객체로 변환
print(df)
#     id  kor  eng
# 0  김철수   60   70
# 1  홍길동   70   75
# 2  박영희   80   80

#set_index() 메소드: 데이터프레임의 특정 컬럼을 새로운 인덱스로 설정
# DataFrame의 index를 id column으로 변경
newdf01 = df.set_index(keys=['id']) #set_index(): index를 지정된 column으로 변경: keys 파라미터에 변경하고자 하는 column 이름을 리스트로 전달 -> id column을 index로 변경
print(newdf01)
#      kor  eng
# id
# 김철수   60   70
# 홍길동   70   75
# 박영희   80   80

newdf02 = df.set_index(keys=['id'], drop=False) # 'id' 컬럼을 새로운 인덱스로 설정. #drop=False로 설정하여 'id' 컬럼을 새로운 컬럼으로 유지
print(newdf02)
#       id  kor  eng
# id
# 김철수  김철수   60   70
# 홍길동  홍길동   70   75
# 박영희  박영희   80   80

#index_col 매개변수를 사용하여 csv 파일에서 특정 열을 인덱스로 지정하여 DataFrame을 생성
df02 = pd.read_csv(filename, index_col='id') #'id'열을 인덱스로 지정 => DataFrame의 인덱스가 됨
print(df02)
#      kor  eng
# id
# 김철수   60   70
# 홍길동   70   75
# 박영희   80   80