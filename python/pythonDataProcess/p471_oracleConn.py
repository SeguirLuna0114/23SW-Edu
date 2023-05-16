import cx_Oracle

#Oracle 클라이언트를 초기화
cx_Oracle.init_oracle_client(lib_dir="/OracleXE/instantclient_19_18")
#lib_dir 매개변수: Oracle 클라이언트 라이브러리의 경로를 지정

#Oracle 데이터베이스에 접속하고 데이터베이스 작업을 수행하기 위한 연결 객체와 커서 객체
#conn 변수와 cur 변수를 초기화
conn = None #접속 객체
cur = None #커서 객체

#try-except 블록을 사용하여 예외 처리를 수행
try:
    #loginfo 변수: 아이디/비번@hostname:port_number/sid
    loginfo = 'hr/1234@192.168.1.146:1521/xe'
    #cx_Oracle.connect(loginfo)를 호출하여 Oracle 데이터베이스에 접속
    #connect() 함수에는 접속 정보를 전달
    conn = cx_Oracle.connect(loginfo)
    print(type(conn)) #conn 객체의 타입을 출력
    # <class 'cx_Oracle.Connection'> #cx_Oracle 라이브러리에서 제공하는 Connection 클래스

    cur = conn.cursor() #객체를 생성
    print(type(cur))
    # <class 'cx_Oracle.Cursor'> #cx_Oracle.Cursor는 cx_Oracle 라이브러리에서 제공하는 Cursor 클래스

    sql = 'select power(2, 10) from dual' #Oracle 데이터베이스에서 'dual' 테이블을 사용하여 2의 10승을 계산하는 SQL 쿼리를 작성
    #sql = 'select * from USERTBL'
    #=> ('LSG     ', '이승기', 1987, '서울', '011', '11111111', 182, datetime.datetime(2008, 8, 8, 0, 0))
    #=> ('KBS     ', '김범수', 1979, '경남', '011', '22222222', 176, datetime.datetime(2012, 4, 4, 0, 0))

    #execute() 메서드는 커서 객체를 사용하여 SQL 쿼리를 실행
    cur.execute(sql) #SQL 쿼리를 실행

    for item in cur: #실행 결과는 item 변수에 할당
        print(item)
        # (1024,)

except Exception as err: #모든 예외를 처리하는 except 블록
    print(err) #예외 메시지를 출력

finally: #예외 발생 여부와 관계없이 항상 실행되는 코드 블록
    if cur != None: #cur 객체가 생성된 상태
        cur.close() #커서 객체를 닫음
    if conn != None: #conn 객체가 생성된 상태
        conn.close() #연결 객체를 닫음

print('finished')