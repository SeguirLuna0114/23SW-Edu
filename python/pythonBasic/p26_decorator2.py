import datetime

def datetime_deco(func):
    def decorated():
        print(datetime.datetime.now())
        func() #정의되는 부분만 바꿔서 정의 가능
        print(datetime.datetime.now())
        print()
    return decorated

@datetime_deco #decorator는 대상함수를 wrapping하고 wrapping된 함수의 앞 뒤에 추가적으로 꾸며질 구문을 정의해 재사용 쉽게 함
def func1():
    print("Main Function1 start")

@datetime_deco
def func2():
    print("Main Function2 start")

@datetime_deco
def func3():
    print("Main Function3 start")

func1()
func2()
func3()