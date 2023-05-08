class Calc(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self): #self는 자기자신을 지칭
        return self.a + self.b
    def sub(self):
        return self.a - self.b
