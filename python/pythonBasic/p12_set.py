#!/usr/bin/env python

even = set([0, 2, 4, 6, 8]) #set자체가 집합이기에 대괄호[]필요
print(even)

hello = set("Hello") #set함수로 객체 생성 가능
print(hello)

s = even | hello #|(or) 이기에 양쪽 결과물 모두 출력. union과 같은 의미
print(s)

p = even & hello # & = intersection과 같은 의미
print(p)

even.add(10)
print(even)

hello.remove('e')
print(hello)

s1 =set([1, 2, 3, 4, 5])
s2 =set([4, 5, 6, 7, 8])

# intersection 교집합
print(s1.intersection(s2)) #s1과 s2의 교집합
print(s1 & s2) #s1과 s2의 교집합

# uniton 합집합
print(s1.intersection(s2)) #s1과 s2의 합집합
print(s1 | s2) #s1과 s2의 합집합

# difference
print(s1.difference(s2)) # s1과 s2의 차집합
print(s1 - s2) #s1에서 s1과 s2의 교집합 제거

print(s2.difference(s1)) # s2과 s1의 차집합
print(s2 - s1) #s2에서 s1과 s2의 교집합 제거

s3 = {1, 2, 3, 4, 5} # s3 = set([1, 2, 3, 4, 5])과 같은 방식

if s1 == s2: #같은지 다른지를 확인하는 방법
    print("s1, s2 is same...")
else:
    print("s1, s2 is not same...")

if s1 == s3: #같은지 다른지를 확인하는 방법
    print("s1, s3 is same...")
else:
    print("s1, s3 is not same...")

s4 = {6, 7, 8, 9, 10}

if s1.isdisjoint(s2): # 공통사항 유무 확인: True/False 출력됨
    print("s1, s2 have in common")
else:
    print("s1, s2 not have in common")

if s3.isdisjoint(s4): # 공통사항 유무 확인: True/False 출력됨
    print("s3, s4 have in common")
else:
    print("s3, s4 not have in common")

print(s1.issubset(s2))

s5 = {4, 5}

print(s2.issubset(s5))

s = {1, 2, 3}
print(f'set : {s}') # f''를 써주고 그 안에 작성

s.update({'a', 'b', 'c'}) #순서가 중요한 게 아니고, 그 안에 들어있는지 아닌지만 확인
print(f'set : {s}')

s.update([11, 12, 13]) # 무작위로 추가됨
print(f'set : {s}')

s.remove('a') #내부에 값이 없을경우 error
print(f'set : {s}')

s.discard("a") # 내부에 값이 없어도 그냥 출력됨
print(f'set : {s}')

s.discard("b")
print(f'set : {s}')

s = {'r', 'd', 'n', 'd', 'o', 'm'}

print(f'set.pop() : {s.pop()}') # set에 넣어두고 pop출력하면, 순서가 의미없이 random으로 꺼내고, 지워짐
print(f'set : {s}')

print(f'set.pop() : {s.pop()}')
print(f'set : {s}')

print(f'set.pop() : {s.pop()}')
print(f'set : {s}')

s.clear() # clear명령어를 통해 s 데이터 값 전부 삭제
print(f'set : {s}')

s = {'a', 'b', 'c'}

if 'a' in s:
    print('a is Exist')
else:
    print('a is not Exist')

if 'z' in s:
    print('z is Exist')
else:
    print('z is not Exist')

print(f'length of set : {len(s)}') # len함수를 통해 집합의 길이 출력 가능

