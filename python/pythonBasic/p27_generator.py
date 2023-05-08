def counter3(max):
    t = 0
    while t < max: #주어진 max값보다 t가 작으면
        yield t #generator를 구현하기 위함
        t += 1 # t값을 하나씩 증가
    return

timer = counter3(5)
print(timer.__next__()) #generator 객체의 next호출 => yield 0 => 변수i = 0
print(timer.__next__()) #0번째 호출! 1
print(timer.__next__()) #1번째 호출! 2