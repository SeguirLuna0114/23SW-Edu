def min(a, b): #min 함수를 정의
    if a > b:
        return b
    else:
        return a

a = input("Input first number : ")
b = input("Input Second number : ")

print("{} vs {} : Min number = {}".format(a, b, min(a,b)))