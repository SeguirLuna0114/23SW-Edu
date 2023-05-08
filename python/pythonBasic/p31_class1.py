class Person(object): #객체의 설계도인 클래스 정의
    total = 10
    def __init__(self, name, age): #클래스 내 변수 및 메소드 정의: 메소드 정의 시 매개변수의 첫번째는 반드시 self 입력, self는 현재의 객체를 가리키는 변수
        self.name = name
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
#클래스는 상속이 가능 => 여러번 사용(re-using)이 가능함.
my = Person("Moon", 22) #정의된 클래스를 이용하여 객체 생성 (name, age)
print(my.name) #만든 객체의 속성과 메소드 사용
print(my.age)
print(my.getName())
print(my.getAge())
print(my.total)

you = Person("Kim", 20)
print(you.getName())
print(you.getAge())
print(you.total)