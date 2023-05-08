#!/usr/bin/env python

# f(x) = f(x-1) + f(x-2) #Fibonacci 수열임...강사님 오타

num = 1
prev = 0
cur = 1

while num < 10:
    next = cur + prev
    print("%3d : %d " % (num, next)) # %3d : 3은 전체 자릿수, %03d: 앞 빈공간을 0으로 채워줌
    prev = cur
    cur = next
    num += 1 #num = num + 1과 같음
