n = 0

while True :
    n += 1 # n=n+1과 같음

    if n > 10 :
        break
    if ((n % 2) == 0) : #2의 배수만 출력
        print(n)