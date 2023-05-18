import json

# JSON 데이터를 생성하고, JSON 문자열로 변환한 뒤, 다시 JSON 데이터로 변환하고 출력

#딕셔너리 형태의 데이터인 data를 정의
data = {'age':30, 'name':"홍길동", 'address':'마포구 공덕동', \
        'broadcast':{
            'sbs':5, 'kbs':9, 'mbc':11
        }
    }

#json.dumps() 함수: data 딕셔너리를 JSON 형식의 문자열로 변환
json_str = json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True)
#ensure_ascii=False 옵션: ASCII 이외의 문자를 유니코드로 인코딩
#indent 옵션: 들여쓰기 칸 설정
#sort_keys=True 옵션: 키를 기준으로 정렬

print(json_str) #변환된 JSON 문자열인 json_str을 출력
print(type(json_str))
#문자열의 타입인 str
print('-' * 40)

#json.loads() 함수: JSON 형식의 문자열인 json_str을 파이썬 객체로 변환
json_data = json.loads(json_str)
print(json_data) #변환된 JSON 데이터인 json_data를 출력
print(type(json_data))
#딕셔너리의 타입인 dict
print('-' * 40)

#json_data 딕셔너리의 특정 키에 해당하는 값을 출력
print(json_data['name'])
print(json_data['age'])
print(json_data['broadcast']['kbs'])

print('finished')
