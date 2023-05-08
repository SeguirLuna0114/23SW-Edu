sum = 0

for i in range(10):
    if i % 2 == 0:
        pass # 2의배수이면 pass
    sum += i #2의 배수 이외의 값들을 더함
    print(f'sum += {i}')
print()
print(f"sum = {sum}")