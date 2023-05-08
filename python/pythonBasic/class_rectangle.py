class Rectangle(object):
    count = 0 # Rectangle.count를 사용하기 위해 count=0 정의(class변수)
    def __init__(self, width, height): #initializer(초기자)
        self.width = width
        self.height = height
        Rectangle.count += 1 # Rectangle.count값을 1씩 늘려줌
    def printCount(cls): #class 메서드
        print(cls.count)
    def calcArea(self): #인스턴스 메서드
        return self.width * self.height
    def isSquare(recWidth, recHeight): #정적 메서드
        return recWidth == recHeight
    def __add__(self, other): #__add__메서드: 두개의 객체를 +기호로 더하는 메서드
        return Rectangle(self.width + other.width, self.height + other.height)

