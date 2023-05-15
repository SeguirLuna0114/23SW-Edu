def nolamda(x, y): #nolamda는 데이터타입 function(함수)
    return 3 * x + 2 * y

x, y = 3, 5

result = nolamda(x, y) #result는 정수 x와 y로 이루어진 정수
print('일반 함수 방식 : %d' % (result))

#lambda(람다) 함수 정의
#lambda함수는 이름이 없는 함수(anonymous)로서, 일회성으로 사용되거나 간단한 함수를 정의할 때 주로 사용
yeslamda = lambda x, y : 3 * x + 2 * y #x와 y를 매개변수로 받고, 3 * x + 2 * y를 반환. #yeslambda는 데이터타입이 funciton(함수)

result = yeslamda(x, y) # x=3, y=5일때 yeslamda 결과값
print("람다 방식 1 : %d" % (result))

result = yeslamda(5, 7) # x=5, y=7일때 yeslamda 결과값
print("람다 방식 2 : %d" % (result))