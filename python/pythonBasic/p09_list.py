#!/usr/bin/env python

numbers = [0, 1, 2, 3]
names = ["kim", "Lee", "Park", "Choi"]
print(numbers[0]) # 0번째 출력
print(names[2:]) # 2번째 부터 출력
print(numbers[-1]) # 마지막 번째 출력
print(numbers + names) # 합해서 출력
empty=[]
print(empty)

# append
names.append("Moon")
print(names) # 맨 마지막에 'Moon'을 추가해서 출력

# insert
names.insert(1, "Gang")
print(names) # 1번째에 Gang 추가하여 출력

# delete
del names[1] # del을 이용하여 1번째 삭제(index에 의한 삭제)
print(names)

# remove
names.remove("Moon") # Moon을 지정하여 삭제(값에 의한 삭제)
print(names)

# pop
value = names.pop() # pop명령어를 이용하여 맨 끝의 값이 삭제됨
print(value)

# pop
value = names.pop(1) #번호 지정하여 해당번째 값 삭제 가능
print(value)

# extend
numbers.extend([4, 5, 6, 4, 4, 5, 6])
print(numbers)

# count
print(numbers.count(4)) #4의 개수 출력

# sort
numbers.sort()
print(numbers)

# reverse
numbers.reverse()
print(numbers)

# clear
numbers.clear() # 빈 리스트로 만들어버림
print(numbers)

