import json

def get_Json_data(): #주어진 JSON 파일을 읽고 내용을 처리
    filename = 'jumsu.json'
    myfile = open(filename, 'rt', encoding='utf-8') #텍스트 모드로 파일을 열고(rt)
    print(type(myfile))
    # 파일 객체의 타입인 TextIOWrapper 클래스
    print('-' * 40)

    myfile = myfile.read() #파일 객체를 읽어 전체 내용을 문자열로 가져옴
    print(type(myfile))
    #문자열 타입인 str
    print('-' * 40)

    jsondata = json.loads(myfile) #문자열로 된 JSON 데이터를 파이썬 객체로 변환
    print(type(jsondata))
    #변환된 파이썬 객체의 타입인 list
    print('-' * 40)

    for oneitem in jsondata: #jsondata 리스트의 각 요소를 순회
        print(oneitem.keys()) #키 목록을 출력
        print(oneitem.values()) #값 목록을 출력
        print('이름 :', oneitem['name']) #oneitem의 'name' 키에 해당하는 값을 출력
        
        #각 과목의 점수를 가져와서 총점을 계산하고 출력
        kor = float(oneitem['kor'])
        eng = float(oneitem['eng'])
        math = float(oneitem['math'])
        total = kor + eng + math

        print('국어 : ', kor)
        print('영어 : ', eng)
        print('수학 : ', math)
        print('총점 : ', total)

        if 'hello' in oneitem.keys(): #'hello' 키가 oneitem의 키 목록에 있는지 확인
            message = oneitem['hello']
            print('message : ', message)

        _gender = oneitem['gender'].upper() #oneitem의 'gender' 키에 해당하는 값을 대문자로 변환하여 _gender 변수에 저장

        #성별 출력
        if _gender == "M":
            gender = '남자' 
            print('성별 : ', gender)       
        elif _gender == "F":
            gender = '여자' 
            print('성별 : ', gender)  
        else:
            print('미정')
    print('-' * 40)

if __name__ == '__main__': #현재 스크립트가 직접 실행될 때만 실행
    get_Json_data() # 스크립트 파일이 직접 실행될 때만 get_Json_data() 함수가 호출되어 실행
