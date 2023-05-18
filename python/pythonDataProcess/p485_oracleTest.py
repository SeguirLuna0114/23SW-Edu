import cx_Oracle
import pandas as pd
import matplotlib.pyplot as plt 
from pandas import Series

#cx_Oracle 패키지: Python에서 Oracle 데이터베이스에 연결하고 데이터를 조회
cx_Oracle.init_oracle_client(lib_dir="/usr/local/OracleXE/instantclient_19_19") #cx_Oracle 패키지를 사용하기 전에 Oracle 클라이언트 라이브러리를 초기화
# lib_dir 매개변수: Oracle 클라이언트 라이브러리의 경로를 지정

plt.rc('font', family="AppleGothic") # matplotlib의 기본 폰트 설정을 변경

conn = None #conn 변수:Oracle 데이터베이스에 대한 연결 객체를 저장하기 위한 변수
cur = None #cur 변수: 데이터베이스에서 쿼리를 실행하기 위한 커서 객체를 저장하기 위한 변수

# Oracle 데이터베이스에 연결하고 쿼리를 실행하여 결과를 시각화
try:
    loginfo = 'hr/1234@192.168.1.146:1521/xe' #데이터베이스에 접속하기 위한 사용자 이름과 비밀번호, 호스트 및 포트 정보
    conn = cx_Oracle.connect(loginfo) #cx_Oracle.connect() 함수를 사용하여 Oracle 데이터베이스에 접속
    cur = conn.cursor() #conn.cursor() 메서드 => 데이터베이스에서 쿼리를 실행할 커서 객체를 생성

    sql = 'select * from three_country' #"three_country"라는 테이블에서 모든 열을 조회하는 쿼리를 실행
    cur.execute(sql) #execute() 메서드 => SQL 쿼리를 실행

    #조회 결과를 저장할 리스트 초기화
    name = []
    year = []
    bindo = []

    for result in cur: #cur 객체를 순회하며 각 결과를 리스트에 추가
        name.append(result[0])
        year.append(result[1])
        bindo.append(result[2])

    myseries  = Series(bindo, index=[name, year]) #bindo 리스트를 기반 - name과 year를 인덱스로 하는 Series 객체를 생성
    print(myseries)

    for idx in range(0, 2): #idx는 0부터 2까지의 범위
        myframe = myseries.unstack(idx) #myseries를 idx를 기준으로 피봇하여 데이터프레임 myframe을 생성
        print(myframe)
        myframe.plot(kind='barh', rot=0) #myframe을 가지고 막대 그래프(barh)를 그리고, 그래프를 이미지 파일로 저장
        plt.title('3개국 테러 발생 현황') #그래프에 제목을 추가
        
        filename = 'oracleChart02_0' + str(idx + 1) + '.png'
        plt.savefig(filename, dpi=400, bbox_inches='tight')
        print(filename + ' file saved...')

        plt.show()

except Exception as err: #예외처리
    print(err) #코드 실행 중 발생하는 예외를 처리하고 에러메시지 출력

finally: #예외 발생 여부에 관계없이 항상 실행
    if cur != None: #커서 객체(cur)가 None이 아닌 경우
        cur.close()

    if conn != None: #연결 객체(conn)가 None이 아닌 경우
        conn.close()
print('finished')
