import cx_Oracle
from xml.etree.ElementTree import parse

cx_Oracle.init_oracle_client(lib_dir="/usr/local/OracleXE/instantclient_19_19") #cx_Oracle를 사용하기 전에 Oracle 클라이언트를 초기화

#conn과 cur 변수를 None으로 초기화
conn = None
cur = None

#parse함수: XML파일을 읽어들여 파싱
tree = parse('xmlEx_04_total.xml') #'xmlEx_04_total.xml' 파일을 파싱하기 위해 parse 함수를 사용 => XML 트리 생성
myroot = tree.getroot() # XML 트리에서 최상위 요소, 즉 루트 요소를 가져와 myroot 변수에 저장

try:
    loginfo = 'hr/1234@192.168.1.146:1521/xe' #데이터베이스에 연결할 때 사용할 사용자 이름, 비밀번호, 호스트 및 포트 정보를 loginfo 변수에 저장
    conn = cx_Oracle.connect(loginfo, encoding='utf-8') #cx_Oracle.connect() 함수를 사용하여 Oracle 데이터베이스에 연결
    print(type(conn))
    #cx_Oracle.Connection 클래스

    mycursor = conn.cursor() #cursor() 메서드를 호출하여 커서 객체를 생성
    print(type(mycursor))
    #cx_Oracle.Cursor 클래스

    items = myroot.findall('item') #'item' 요소를 찾아서 items 변수에 저장

    for oneitem in items: #items 리스트의 각 요소를 순회
        #oneitem 요소의 텍스트를 사용하여 SQL 문을 생성
        sql = " insert into shops"
        sql += " values("
        sql += oneitem[0].text + "', '"
        sql += oneitem[1].text + "', '"
        sql += oneitem[2].text + "', '"
        sql += oneitem[3].text + "', '"
        sql += oneitem[4].text + "', '"
        sql += oneitem[5].text + "', '"
        sql += oneitem[6].text + "', '"
        sql += oneitem[7].text + "' "
        sql += " )"
        
        #SQL 문을 실행하여 데이터베이스에 데이터를 삽입
        mycursor.execute(sql)
    
    conn.commit() #데이터베이스의 변경 사항을 커밋하여 영구적으로 저장(데이터베이스에 실제로 데이터가 저장)

except Exception as err: # 실행 중에 오류가 발생할 경우 예외 처리를 수행
    if conn != None: # 데이터베이스 연결이 존재하는지
        conn.rollback() #데이터베이스에 대한 아직 커밋되지 않은 변경 사항을 롤백 => 데이터베이스가 일관된 상태 유지 가능
    print(err)

finally:
    if cur != None:
        cur.close()
    
    if conn != None:
        conn.close()
print('finished')
