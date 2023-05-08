def handler():
    while True:
        n1, n2 = (yield)
        print(f'{n1} + {n2} = {n1 + n2}')

listener = handler()

listener.__next__() # next를 한번 던져주면 while 반복문이 멈추게 됨
#yield에 send라는 키워드 전달을 위해서
listener.send([5, 4])
listener.send([3, 6])
