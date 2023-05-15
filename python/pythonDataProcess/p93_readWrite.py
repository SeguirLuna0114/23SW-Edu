myfile01 = open('sample.txt', 'rt', encoding='UTF-8') #'sample.txt' 파일을 text 읽기모드(rt)로 열어서
linelists = myfile01.readlines() #linelists에 파일을 한줄씩 읽어서 list형식으로 저장
myfile01.close() #파일 닫음
print(linelists) #sample.txt 값을 읽어줌: ['70\n', '60\n', '55\n', '75\n', '95\n', '90\n', '80\n', '80\n', '85\n', '100']

# sample.txt 파일에 있는 점수의 총합과 평균을 구함
total = 0
for one in linelists: #linelists에 저장된 각 점수에 대해
    score = int(one) #점수를 정수로 변환하여(text모드로 열었기에 string임)
    total += score #각 점수를 더하여 total에 저장
average = total / len(linelists) #total을 linelists의 길이로 나눠서 average에 저장

#result.txt파일에 총합과 평균을 씀
myfile02 = open('result.txt', 'wt', encoding='UTF-8') #result.txt파일을 text 쓰기모드(wt)로 열기
myfile02.write('총점 : ' + str(total) + '\n') #write함수를 이용해 total값을 문자열로 변환하여(text모드이기 때문) 파일에 씀
myfile02.write('평균 : ' + str(average)) #write함수를 이용해 average값을 문자열로 변환하여(text모드이기 때문) 파일에 씀
myfile02.close() #파일 닫기
print("done~!!")

#result.txt파일을 열어서 파일의 내용을 한줄씩 출력
myfile03 = open('result.txt', 'rt', encoding='UTF-8') #'result.txt'파일을 text 읽기모드(rt)로 열기
line = 1
while line:
    line = myfile03.readline() #readline함수를 이용하여 한 줄씩 파일 내용을 읽어서 line에 저장
    print(line) #line 출력(이때, line은 문자열)
myfile03.close() #파일 닫기