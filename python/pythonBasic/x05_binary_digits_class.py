import random

class Binary_digits(object):
    def __init__(self, digit, lists):
        self.digit = digit
        self.lists = lists

    def convert(self):
        n = self.digit
        lists = self.lists
        while True:
            n1 = n % 2
            n = n // 2
            lists.append(n1)
            if n == 0:
                break
        lists.reverse()
        return lists

lists =[]
digit = random.randrange(4, 16)
binary = Binary_digits(digit, lists)
print(f'{digit} binary number is :{binary.convert()}')