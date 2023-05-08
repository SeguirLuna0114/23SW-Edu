class Gcd(object): #최대공약수와 최소공배수 class 구현
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def gcd(self):
        print("gcd", (self.a, self.b))
        while self.b != 0:
            self.r = self.a % self.b
            self.a = self.b
            self.b = self.r #self.b = self.a % self.b와 같은 명령
            print("gcd", (self.a, self.b))
        return self.a

a = int(input("Input First number : ")) #첫번째 입력 = a
b = int(input("Input Second number : ")) #두번째 입력 = b

gcd1 = Gcd(a, b) #class Gcd에 a와 b 적용 => gcd1
print(f'gcd({a}, {b}) of {a}, {b} : {gcd1.gcd()}')
