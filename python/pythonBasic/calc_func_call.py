import calc_func

a = int(input("Input first number : "))
b = int(input("Input Second number : "))

print('{} + {} = {}'.format(a, b, calc_func.add(a, b))) #calc_func()내의 함수 중 add만 호출
print('{} - {} = {}'.format(a, b, calc_func.sub(a, b))) #calc_func()내의 함수 중 sub만 호출
