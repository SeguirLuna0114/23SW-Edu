mylist01 = list(onedata for onedata in range(1, 6))
print(mylist01) # 1~5까지 숫자를 이용하여 list 생성: [1, 2, 3, 4, 5]

print()

mylist02 = list(10 * onedata for onedata in range(1, 6))
print(mylist02) # 1~5까지 숫자에 10을 곱한 값을 이용하여list 생성: [10, 20, 30, 40, 50]

mylist03 = [3, 4, 6, 2] # []을 이용하여 list 생성
result = [idx ** 2 for idx in mylist03 if idx % 2 == 0] #mylist에서 짝수인 원소들을 뽑아서 해당 원소의 제곱값을 result라는 새로운 리스트에 추가
print(result) #[4^2, 6^2, 2^2] 출력됨