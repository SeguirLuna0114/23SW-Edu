#!/usr/bin/env python

person = ("Kim", 24, "male")
print(person)

a = ()
print(a)

b = (person, )
print(b)

name, age, gender = person #값을 하나씩 나눠서 필드 분할 시 사용
print("name : ", name)
print("age : ", age)
print("gender : ", gender)

n = 1
numbers = [1, 2]

print(type(person)) # person의 데이터 타입에 대하여 출력
print(type(n)) # n의 데이터 타입에 대하여 출력
print(type(numbers)) # numbers의 데이터 타입에 대하여 출력

print(person[0]) #index로 접근 가능
print(person[-1]) #index로 접근 가능

fruits = ("apple", ("banana", "cherry"), ("strawberry", "watermelon"))
print(fruits)
print(fruits[0])
print(fruits[1][0]) #1번째의 0번째 index 출력
print(fruits[1][1]) #1번째의 0번째 index 출력
print(fruits[2][0]) #1번째의 0번째 index 출력
print(fruits[2][1]) #2번째의 0번째 index 출력
