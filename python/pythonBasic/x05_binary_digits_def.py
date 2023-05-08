import random

def binary_digits(digit, lists):
    n = digit // 2
    r = digit % 2
    lists.append(r)
    if n == 0:
        lists.reverse()
        return lists
    else:
        return binary_digits(n, lists)

lists =[]
digit = random.randrange(4, 17)
print(f'{digit} binary number is : {binary_digits(digit, lists)}')