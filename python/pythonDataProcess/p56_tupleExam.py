tuple01 = (10, 20, 30)
tuple02 = tuple01 + (40, ) #tuple02는 tuple01에 마지막 40을 더함: (10, 20, 30, 40)

print('print Tuple : ', tuple01)

tuple02 = 10, 20, 30, 40 #[]를 치지 않고도 tuple 생성 가능

mylist = [10, 20, 30, 40] #class = list
tuple03 = tuple(mylist) #list값을 tuple로 변환 가능

if tuple02 == tuple03:
    print("Component equal") #tuple02가 tuple03과 같음
else:
    print("Component not equal")

tuple04 = (10, 20, 30)
tuple05 = (40, 50, 60)
tuple06 = tuple04 + tuple05
print(tuple06) # tuple06 = (10, 20, 30, 40, 50, 60)

tuple07 = tuple04 * 3 #tuple04의 데이터를 3번 반복한 튜플값 => tuple07
print(tuple07) # tuple07 = (10, 20, 30, 10, 20, 30, 10, 20, 30)

a, b = (11, 22) #a는 정수 11, b는 정수 22
a, b = b, a #a와 b 값 변환
print('a =', a, 'b =', b) #a는 정수 22, b는 정수 11

tuple08 = (11, 22, 33, 44, 55, 66)
print(tuple08[1:3]) #1~2번째 tuple08값 출력: (22, 33)
print(tuple08[3:]) #3~마지막번째 tuple08값 출력: (44, 55, 66)
