class Calculate(object):
    def __init__(self, first, second):
        self.first = first #self 초기화
        self.second = second

    def add(self):
        result = self.first + self.second
        return 'add result : %d' % result
    def sub(self):
        result = self.first - self.second
        return 'sub result : %d' % result
    def mul(self):
        result = self.first * self.second
        return 'mul result : %d' % result
    def div(self):
        if self.second == 0: #second값이 0이면, 5로 대체
            self.second = 5
        result = self.first / self.second #result는 float
        return 'div result : %.3f' % result #float의 소수점3자리수까지 출력

calc = Calculate(14, 0) #first=14, second=0

print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())
