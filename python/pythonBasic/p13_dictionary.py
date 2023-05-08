#!/usr/bin/env python

me = {"name" : "Moon", "age" : 22, "gender" : "male"} # 중복자체가 불가하기에
print(me)

myname = me["name"]
print(myname)

me["age"] = 25
print(me)

dict = {}
print(dict)

me[10] = 10 # 10(숫자키): 10(숫자값) 값이 추가되었음을 확인
print(me)

me['10'] = 10 # '10'(문자키): 10(숫자값) 값이 추가되었음을 확인(숫자키와 문자키 구별함)
print(me)

me['job'] = "teacher" # 문자키: 문자값
print(me)

me['list'] = [1, 2, 3, 4, 5] # 문자키: list
print(me)

me[(1, 2)] = "this is value" # 튜플은 데이터 값을 변경할 수 없기에(불변) list가 올 수 없음
print(me)

me[3] = (3, 'aa', 5)
print(me)

print("===========")
print(f'me[list] : {me["list"]}')
print(f'me[(1, 2)] : {me[(1, 2)]}')
print(f'me[3] : {me[3]}')

print(f'me[(1, 2)] : {me[(1, 2)]}')
me[(1,2)] = "This is real value"
print(f'me[(1, 2)] : {me[(1, 2)]}') #변경된 me[(1,2)]의 값이 출력됨

dic = {'a' : 1234, "b" : "blog", "c" : 3333}

# in
if 'b' in dic:
    print("b is exist")
else:
    print("b is not exist")

if 'e' in dic:
    print("e is exist")
else:
    print("e is not exist")

# keys()
print(dic.keys())

for k in dic.keys(): #특정 key값 검사할 경우 유용
    print(f'key : {k}') #key값이 순차적으로 출력됨

# values()
if 'blog' in dic.values(): #value가 공백인지 아닌지 확인
    print("value is exist")
else:
    print("value is not exist")

print(dic.values())

for v in dic.values():
    print(f'value : {v}')

# items()
print(dic.items())

for i in dic.items():
    print(f'all : {i}')
    print(f'key : {i[0]}') #item에서 key 출력
    print(f'key : {i[1]}') #item에서 value 출력
    print() #빈 공백 출력-가시성 높이기 위함

# get()
v1 = dic.get('b') #get을 통해 b값 불러옴
print(f"dic.get['b'] : {v1}")

v2 = dic.get('z') #get을 통해 z값 불러옴
print(f"dic.get['z'] : {v2}") #값이 없으므로 None 출력됨

# del
print(f'before : {dic}')

del dic['c']

print(f'after : {dic}')

# clear
dic.clear()
print(f'clear : {dic}')
