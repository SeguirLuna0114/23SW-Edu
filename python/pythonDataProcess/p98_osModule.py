import os #os 모듈을 사용하여 디렉토리 및 하위폴더 생성

#현재 디렉토리 내에 work 폴더를 생성
myfolder = './' #현재 디렉토리'.'를 myfolder변수에 저장. 이때 myfolder는 문자열
newpath = os.path.join(myfolder, 'work') #새로 생성할 디렉토리 경로(work디렉토리)를 os.path.join()함수를 사용하여 결합

#work 폴더 내에 somefolder01부터 somefolder10까지의 하위 폴더를 생성
try: #try와 finally는 Exception이 발생하더라도 반드시 실행되는 코드 블록. 예외 발생시 블록 내 코드는 실행 중단되고 exception블록으로 넘어감
    os.mkdir(path=newpath) #os.mkdir()함수를 사용하여 새 디렉토리 생성 in path=newpath='./work'경로

    for idx in range(1, 11):#1~10범위까지 각각의 하위폴더를 생성
        newfile = os.path.join(newpath, 'somefolder' + str(idx).zfill(2)) #str.zfill()메서드를 사용하여 각 하위폴더 이름에 01~10까지 두자리숫자(zfill(2)=>2자리 숫자)를 추가
        #os.path.join()함수: myfolder 변수에 지정된 현재 디렉토리와 newfile 변수에 저장된 경로를 연결하여 전체 경로를 생성
        os.mkdir(path=newfile) #os.mkdir()함수: path매개변수로 전달된 경로에서 마지막 디렉토리 이름인 somefolder01, somefolder02와 같이 새로운 디렉토리 생성

#만약 work 폴더가 이미 존재하는 경우 "Dictionary exist already..." 메시지를 출력하고 생성하지 않음
except FileExistsError: # 생성한 디렉토리가 존재한다면 FileExistsError가 발생
    print('Dictionary exist already...') #이미 존재할 경우 메시지 출력
finally: #finally 블록: try 블록 내 코드들이 성공적으로 완료 or 예외 발생 하더라도 반드시 실행되는 코드
    print('finished')