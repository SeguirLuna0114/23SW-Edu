from itertools import count

# 0부터 4까지의 숫자를 출력하는 반복문
for page_idx in count():
    # count() 함수를 사용 => (0부터 시작하여 1씩 증가하는 값으로 이루어진)무한한 숫자 시퀀스 생성
    # for 반복문 => 해당 숫자를 처리
    if page_idx >= 5: #page_idx가 5보다 크거나 같으면
        break #반복문을 종료(반복문이 5회를 실행하게 되면 if 문의 조건이 만족되어 break 문이 실행되어 반복문을 종료)
    print(page_idx)
    # 0
    # 1
    # 2
    # 3
    # 4
print('finished')
