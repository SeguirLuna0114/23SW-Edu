class SmarPhone:
    def __init__(self, brand, maker, price):
        self.brand = brand
        self.maker = maker
        self.price = price
    def __str__(self): #str메소드 : string의 약자. 문자열을 그대로 반환
        return f'str : {self.brand} - {self.maker} - {self.price}' #str소스에 표현하기 위해서 넣어둠(정의함). 구조를 보여주는 느낌. print기법

class Galaxy(SmarPhone):
    def __init__(self, brand, maker, price, country):
        self.brand = brand
        self.maker = maker
        self.price = price
        self.country = country
    def __str__(self):
        return f'str : {self.__class__.__name__} ' \
            f'스마트폰은 {self.maker}에서 출시되었고, ' \
            f'{self.country}에서 생산되었습니다. ' \
            f'가격은 {self.price}입니다. '

iphone = SmarPhone('IPhone', 'Apple', 10000)
print(iphone)
galaxy = Galaxy('Galaxy', 'Samsung', 8000, 'South Korea')
print(galaxy)