import random

class Binary_digits(object): #10진수 -> 2진수 구현
    def __init__(self, digit):
        self.digit = digit
        #self.lists = lists

    def convert(self):
        lists = []
        while True:
            self.digit = int(self.digit // 2)  # '//' => 나머지 출력
            n = int(self.digit % 2)  # n2 => 몫
            if n != 0:
                lists.insert(0, n) #lists.append(n)
            else:
                break
        lists.reverse()
        return lists

digit = random.randrange(4, 17) # 4이상 17미만
binary = Binary_digits(digit) #객체 생성
print(f'Digit value is : {digit}')
print(f'{digit} binary number is : {binary.convert()}')