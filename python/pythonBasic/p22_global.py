m = 0
n = 1
def func():
    m = 0
    global n # n은 global변수이기에, func에도 n=1이 적용됨
    m += 1 # m=m+1=1
    n += 1 # n=n+1=2
    print(f'{m} vs {n}')
func() # func()을 해야 print(f'{m} vs {n}')가 출력됨
print(m, n)