from sqlalchemy import Column, TEXT, INT
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy를 사용하여 두 개의 테이블을 정의
# SQLAlchemy ORM의 기능을 사용하여 데이터베이스와 상호작용

#declarative_base()를 통해 생성한 Base 클래스를 상속받음
# Base 클래스는 데이터베이스 모델을 정의하기 위한 기본 클래스
Base = declarative_base()

class St_info(Base): #St_info 클래스
    __tablename__ = "st_info"

    ST_ID = Column(INT, nullable=False, primary_key=True) #INT 타입의 컬럼, NULL이 허용되지 않고, 기본키(primary key)로 설정됨
    NAME = Column(TEXT, nullable=False) #TEXT 타입의 컬럼, NULL이 허용되지 않음
    DEPT = Column(TEXT, nullable=False) #TEXT 타입의 컬럼, NULL이 허용되지 않음

class St_grade(Base): #St_grade 클래스
    __tablename__ = "st_grade"

    ST_ID = Column(INT, nullable=False, primary_key=True) # INT 타입의 컬럼, NULL이 허용되지 않고, 기본키(primary key)로 설정됨
    Linux = Column(TEXT, nullable=False) #TEXT 타입의 컬럼, NULL이 허용되지 않음
    DB = Column(TEXT, nullable=False) #TEXT 타입의 컬럼, NULL이 허용되지 않음
