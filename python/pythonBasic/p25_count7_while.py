import p25_timer

timer = p25_timer.counter2()
counter = 0
sum = 0

while True: #while loop 안에서
    sum += 7
    if sum > 100: # 100초과면 break
        break
    counter = timer()
print(f'result : {counter}')