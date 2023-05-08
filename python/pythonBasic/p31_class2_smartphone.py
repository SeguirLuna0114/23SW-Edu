class SmarPhone:
    def __init__(self, brand, details):
        self.brand = brand
        self.details = details
    def __str__(self): #str메소드 : string의 약자. 문자열을 그대로 반환
        return f'str : {self.brand} - {self.details}' #str소스에 표현하기 위해서 넣어둠(정의함). 구조를 보여주는 느낌. print기법
    def __repr__(self): #repr메소드 : representation. 문자열을 생성할 수 있는 방법을 정의함. 설명서와 같음. 객체를 선언하는 방법
        return f'repr : Instant_name = SmartPhone({self.brand}, {self.details})'
    def __doc__(self):
        return f'This class is Smart Phone Class. It is have a brand name and detail description.'

SmarPhone1 = SmarPhone('IPhone', {'color' :'White', 'price' : 10000})
SmarPhone2 = SmarPhone('Galaxy', {'color' :'Black', 'price' : 8000})
SmarPhone3 = SmarPhone('Blackberry', {'color' :'Silver', 'price' : 6000})

print(dir(SmarPhone)) #dir을 사용해서 지원하는 메서드 표현
print(SmarPhone1) #str이 default여서 print(str(SmartPhone1)) = Print(SmartPhone1)
print(SmarPhone1.__dict__)
print(SmarPhone2.__dict__)
print(SmarPhone3.__dict__)

print(id(SmarPhone1))
print(id(SmarPhone2))
print(id(SmarPhone3))

print(SmarPhone1.brand == SmarPhone2.brand)
print(SmarPhone1 is SmarPhone2)

print(SmarPhone.__str__(SmarPhone1))
print(SmarPhone.__repr__(SmarPhone2))
print(SmarPhone.__doc__)
