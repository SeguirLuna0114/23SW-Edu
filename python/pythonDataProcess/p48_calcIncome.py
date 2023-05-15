salary = int(input("월 급여 입력 : "))

income = 0 #초기 income값 설정
tax = 0

if salary >= 500:
    income = 12 * salary
else:
    income = 13 * salary

if income >= 10000:
    tax = 0.2 * income
elif income >= 7000:
    tax = 0.15 * income
elif income >= 5000:
    tax = 0.12 * income
elif income >= 1000:
    tax = 0.1 * income
else:
    tax = 0

print("월급 : %d" % (salary))
print("연봉 : %.2f" % (income)) #%.2f: 소수점 이하 2자리까지 실수(float)을 나타냄
print("세금 : %.2d" % (tax)) #%.2d: 2자리 정수를 나타내는 서식지정자=>최소 2자리를 사용하되, 자리수가 부족할 경우 앞을 0으로 채워줌.
# '%02d'와 '%.2d'의 차이점은 자릿수가 2자리를 넘어가는 경우
# %02d: 정수형 숫자를 2자리로 고정하여 표시(123 => 99를 반환.2자리수만 출력 가능)
# %.2d: 최대 2자리까지만 표시하므로, 자릿수가 3자리 이상인 경우에는 그대로 출력(123 => 23를 반환. 2번째 자리 수까지만 출력)