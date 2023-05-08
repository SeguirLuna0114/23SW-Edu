import p25_timer

timer = p25_timer.counter2()
cnt = 0 #count값을 하나씩 증가시킬 것

while True:
    print(f'-----{timer()}-----')
    if timer() > 100: # timer가 불려질때마다 증가
        break
    if timer() % 7 == 0:
        cnt += 1

print(cnt)