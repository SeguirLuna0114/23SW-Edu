numbers = [1, 2, 3, 4, 5]
evens = (2 * i for i in numbers)

print(evens) #evens 출력 => generator object ID가 출력됨
print(evens.__next__()) # yield가 내부에 있기에, next를 해야 실행됨
print(evens.__next__())
print(sum(evens)) #__next__를 2번 출력했기에, numbers[2]에 yield가 멈춰있음 => 3+4+5=24가 출력됨. sum을 이용해 끝까지 출력되었음
#print(evens.__next__()) #sum의 경우에는 더이상 꺼낼 것이 없어서 error

print(numbers)
numbers.reverse()
print(numbers) #reverse된 것 print

evens = (2 * i for i in numbers)

print(evens)
print(evens.__next__()) #0번째 값 출력
print(evens.__next__()) #1번째 값 출력
print(numbers)
print(evens.__next__()) #2번째 값 출력
