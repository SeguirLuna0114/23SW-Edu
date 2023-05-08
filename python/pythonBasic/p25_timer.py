def counter2():
    t = [0] #t는 배열[0]
    def increment():
        t[0] += 1 # t[0] = t[0] + 1
        return t[0] #1을 증가시킨 t[0] return
    return increment # increment함수 반환

timer = counter2() # timer를 counter2()함수라고 함
print(timer())

print(timer())
