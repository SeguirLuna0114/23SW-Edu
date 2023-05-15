import pandas as pd

#.read_csv함수를 이용하여 파일을 읽어들여서 DataFrame 객체로 변환한 후 출력
filename = 'seoul.csv' #filename변수에 seoul.csv 파일명 저장
df = pd.read_csv(filename) #pd.read_csv함수를 이용하여 DataFrame객체로 변환
#파일 내용을 바탕으로 DataFrame이 생성되면서 index와 columns이 자동으로 생성됨
print(df)
print('-' * 50)

#df.loc[조건식] : DataFrame에서 조건식에 해당하는 행(row) 출력
#Dataframe['컬럼 명'] == '데이터 값' : 해당하는 열의 값이 데이터값인 행을 추출함
result =df.loc[(df['시군구'] == ' 서울특별시 강남구 신사동')] #DataFrame에서 '시군구' 열의 값이 '서울특별시 강남구 신사동'인 모든 행을 result 변수에 저장
print(result) #이때 데이터프레임 형태로 저장됨
print('-' * 50)

#df.loc[(조건식) & (조건식)] :&(and)
result =df.loc[(df['시군구'] == ' 서울특별시 강남구 신사동') & (df['단지명'] == '삼지')] # '시군구'열의 값이 '서울특별시 강남구 신사동'이고, '단지명'열의 값이 '삼지'인 행 출력
print(result)
print('-' * 50)

#.set_index() 메소드: 인덱스를 변경
#keys 매개변수에 바꾸고자 하는 인덱스로 사용할 열(column)을 리스트 형태로 전달
newdf = df.set_index(keys=['도로명']) #인덱스가 도로명으로 변경된 새로운 DataFrame 객체 생성
print(newdf)
print('-' * 50)

#.loc[]: 해당하는 인덱스를 포함하는 모든 행 출력
result = newdf.loc['동일로'] #동일로'를 포함하는 모든 도로명 주소가 포함된 데이터프레임 생성
count = len(newdf.loc['동일로']) #동일로'를 포함하는 모든 도로명 주소의 개수를 반환한 정수데이터 저장
print(result)
print('count : ', count)
