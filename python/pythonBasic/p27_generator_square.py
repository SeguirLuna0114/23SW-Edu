def square_number(nums): #변수를 nums라고 하는 경우
    for i in nums: #i가 nums안에 속하는 동안 i*i를 순차적으로 실행
        yield i * i #yield키워드는 해당 라인을 실행하고, 함수를 호출한 쪽으로 프로그램 제어

mynum = [1, 2, 3, 4, 5] #mynum list 선언
result = square_number(mynum) #square_number함수의 결과값을 result라는 변수 선언

for i in range(len(mynum)): # len(mynum)=5이기에, range(5): 0~4까지
    print(f'Square value of mynum[{i}] = {mynum[i]} : {next(result)}')
# next함수가 실행되면 yield키워드의 i인 0을 넘겨주고 멈춤 ->다시 next가 실행되면 그 다음 i를 반환