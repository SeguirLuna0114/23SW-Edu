from fastapi import FastAPI 
from pydantic import BaseModel
from database import db_conn
from models import St_info, St_grade

app = FastAPI()

db = db_conn()
session = db.sessionmaker()

class Item(BaseModel):
    name : str 
    number : int 

#FastAPI 애플리케이션에서 다양한 엔드포인트를 정의
#엔드포인트는 HTTP GET 요청을 처리하며, 데이터베이스의 정보를 조회하거나 수정하는 기능을 제공

@app.get('/')
#async def 구문을 사용하여 비동기 함수로 정의
async def healthCheck():
    return "OK"

@app.get('/stinfo')
async def select_st_info(): #St_info 테이블의 모든 정보를 조회하여 반환
    #session.query(): 테이블의 쿼리 객체를 생성
    result = session.query(St_info)
    #.all(): 모든 결과를 반환
    return result.all()

@app.get('/stgrade')
async def select_st_grade(): #St_grade 테이블의 모든 정보를 조회하여 반환
    result = session.query(St_grade).all()
    return result

@app.get('/getuser')
async def getuser(id=None, name=None): #학번(id) 또는 이름(name)으로 사용자 정보를 검색
    #학번과 이름은 선택적 매개변수로 받음
    if (id is None) and (name is None): #둘 중 하나가 없는 경우
        return "학번 또는 이름으로 검색하세요."
    else:
        #매개변수에 따라 St_info 테이블에서 필터링하여 결과를 반환
        if name is None:
            result = session.query(St_info).filter(St_info.ST_ID == id).all()
        elif id is None:
            result = session.query(St_info).filter(St_info.NAME == name).all()
        else:
            result = session.query(St_info).filter(St_info.ST_ID == id, St_info.NAME == name).all()
        return result

@app.get('/useradd')
async def useradd(id=None, name=None, dept=None):
    #학번(id), 이름(name), 학과명(dept)을 매개변수로 받음
    if (id and name and dept) is None: #하나라도 누락된 경우
        return "학번, 이름, 학과명을 입력하세요."
    else:
        user = St_info(ST_ID=id, NAME=name, DEPT=dept) #St_info 객체를 생성
        #session.add()를 통해 세션에 추가
        session.add(user)
        #session.commit()으로 변경 사항을 저장
        session.commit()
        ##session.query(): 테이블의 쿼리 객체를 생성
        result = session.query(St_info).all()
        return result

@app.get("/userupdate")
async def updateadd(id=None, name=None, dept=None):
    #학번(id), 이름(name), 학과명(dept)을 매개변수로 받음
    if id is None:
        return "학번을 입력하세요"
    else:
        #session.query(St_info).filter()를 통해 해당 학번의 사용자 정보를 조회
        user = session.query(St_info).filter(St_info.ST_ID == id).first() #St_info 테이블에서 ST_ID가 id와 일치하는 첫 번째 레코드를 가져옴
        #필드 값을 업데이트
        user.NAME = name
        user.DEPT = dept
        #session.add()를 통해 세션에 추가
        session.add(user)
        #session.commit()으로 변경 사항을 저장
        session.commit()
        result = session.query(St_info).filter(St_info.ST_ID == id).all() #St_info 테이블에서 ST_ID가 id와 일치하는 모든 레코드를 가져
        return result

@app.get("/userdel")
async def updateadd(id=None):
    #학번(id)을 매개변수로 받음
    if id is None:
        return "학번을 입력하세요"
    else:
        session.query(St_info).filter(St_info.ST_ID == id).delete() #St_info 테이블에서 ST_ID가 id와 일치하는 레코드를 삭제
        session.commit() #변경 사항을 커밋
        result = session.query(St_info).all() #모든 St_info 레코드를 가져옴
        return result
