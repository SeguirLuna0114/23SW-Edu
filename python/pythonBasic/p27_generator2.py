import datetime #class형태로 decorator 사용
#class형태로 decorator사용하려면 __call__함수로 decorator 형식을 정의
class DatetimeDecorator:
    def __init__(self, f): #호출할 함수를 인스턴스의 초기값으로 받음
        self.func = f #호출할 함수를 속성 func에 저장
    def __call__(self, *args, **kwargs): #호출할 함수의 매개변수를 처리
        print(datetime.datetime.now())
        self.func(*args, **kwargs) #self.func에 매개변수를 넣어서 호출
        print(datetime.datetime.now())
        print()

class MainClass:
    @DatetimeDecorator #@데코레이터
    def func1():
        print("Main Function1 start")
    @DatetimeDecorator
    def func2():
        print("Main Function2 start")
    @DatetimeDecorator
    def func3():
        print("Main Function3 start")

my = MainClass()
my.func1()
my.func2()
my.func3()