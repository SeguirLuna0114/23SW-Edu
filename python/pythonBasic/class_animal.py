class Animal(object):
    def __init__(self, name):
        self.name = name
    def move(self):
        print('move~')
    def speak(self):
        pass #재정의를 하기위해서 pass-내용이 없는 빈 클래스를 만듦

class Dog(Animal):
    def speak(self):
        print('woof-woof')

class Duck(Animal):
    def speak(self):
        print('quack-quack')

