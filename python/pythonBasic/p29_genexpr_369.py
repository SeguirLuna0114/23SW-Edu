numbers = (i for i in range(1, 101))

data = list(numbers)

item = [3, 6, 9]

for i in data:
    n10 = int(i / 10)
    n1 = i % 10
    if i % 10 == 1:
        print() #=> newline(줄바꾸기) 출력됨
    if i < 10:
        if i in item: #i가 3,6,9리스트와 같은게 있다면
            print('  👏', end="") #줄바꿈 안하기 위해서 end=""
        else:
            print("%4d" % i, end="")
    else:
        if n10 in item and n1 in item:#10의자리가 item에 들어가 있고, 1의자리도 item에 있으면
            print(' 👏👏', end="")
        elif n10 in item or n1 in item:
            print('  👏', end="")
        else:
            print("%4d" % i, end="")