import cx_Oracle
import pandas as pd
import matplotlib.pyplot as plt 
from pandas import Series

#cx_Oracle 패키지: Python에서 Oracle 데이터베이스에 연결하고 데이터를 조회
cx_Oracle.init_oracle_client(lib_dir="/usr/local/OracleXE/instantclient_19_19") cx_Oracle 패키지를 사용하기 전에 Oracle 클라이언트 라이브러리를 초기화
# lib_dir 매개변수: Oracle 클라이언트 라이브러리의 경로를 지정

plt.rc('font', family="AppleGothic") # matplotlib의 기본 폰트 설정을 변경

conn = None  #conn 변수:Oracle 데이터베이스에 대한 연결 객체를 저장하기 위한 변수
cur = None #cur 변수: 데이터베이스에서 쿼리를 실행하기 위한 커서 객체를 저장하기 위한 변수

# Oracle 데이터베이스에 연결하고 쿼리를 실행하여 결과를 시각화
try:
    loginfo = 'hr/1234@192.168.1.146:1521/xe' #데이터베이스에 접속하기 위한 사용자 이름과 비밀번호, 호스트 및 포트 정보
    conn = cx_Oracle.connect(loginfo) #cx_Oracle.connect() 함수를 사용하여 Oracle 데이터베이스에 접속
    cur = conn.cursor() #conn.cursor() 메서드 => 데이터베이스에서 쿼리를 실행할 커서 객체를 생성

    sql = 'select * from country_summary_top_10' #"country_summary_top_10"라는 테이블에서 모든 열을 조회하는 쿼리를 실행
    cur.execute(sql) #execute() 메서드 => SQL 쿼리를 실행

    #조회 결과를 저장할 리스트 초기화
    data = []
    country = []

    for result in cur: #cur 객체를 순회하며 각 결과를 리스트에 추가
        data.append(result[1])
        country.append(result[0])
    
    mycolor = ['r', 'g','b','y','m','c','#fff0f0','#ccffbb','#05ccFF','#11ccff'] #색상을 지정하는 리스트 지정

    charData  = Series(data, index=country) #data리스트를 기반 -> country를 인덱스로 하는 Series 객체를 생성

    #charData를 기반으로 막대 그래프를 그림
    charData.plot(kind='bar', rot=18, grid=False, title='범죄 빈도 Top 10 국가',color=mycolor, alpha=0.7)
    #alpha=0.7: 막대의 투명도를 조정

    plt.ylabel('빈도 수', rotation=0) #y축 레이블에 '빈도 수'라는 텍스트를 추가

    filename = 'oracleChart01.png'
    plt.savefig(filename, dpi=400, bbox_inches='tight') #그래프를 이미지 파일로 저장
    print(filename + ' file saved...')

    plt.show()

    #pd.read_sql() 함수를 사용하여 데이터베이스에서 SQL 쿼리 결과를 읽어옴
    myframe = pd.read_sql(sql, conn, index_col="COUNTRY_TXT") #sql은 실행할 쿼리를, conn은 데이터베이스 연결 객체를, index_col은 인덱스로 사용할 열을 지정.
    print(type(myframe))
    print(myframe)

except Exception as err: #예외처리
    print(err) #코드 실행 중 발생하는 예외를 처리하고 에러메시지 출력

finally: #예외 발생 여부에 관계없이 항상 실행
    if cur != None: #커서 객체(cur)가 None이 아닌 경우
        cur.close()

    if conn != None: #연결 객체(conn)가 None이 아닌 경우
        conn.close()
print('finished')
