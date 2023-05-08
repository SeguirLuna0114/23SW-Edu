sum = 0

for i in range(10): # 0~9까지
    if i % 2 == 0: #i가 2의배수이면
        continue #skip
    sum += i # sum = sum + i #2의배수가 아닌 i에 인해 sum
    print(f'sum += {i}') #sum에서 i만큼 더해짐

print() # 공백 출력
print(f"sum = {sum}")  # sum의 값들을 모두 더함