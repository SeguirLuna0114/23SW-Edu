myfile1 = open('sample02.txt', 'rt', encoding='UTF-8') #'sample02.txt' 파일을 text 읽기모드(rt)로 열어서
linelists = myfile1.readlines() #linelists에 파일을 한줄씩 읽어서 list형식으로 저장
myfile1.close()

myfile2 = open('result02.txt', 'wt', encoding='UTF-8') #result02.txt파일을 text 쓰기모드(wt)로 열기
total = 0 #총점
for one in linelists: #linelists에 저장된 각 점수에 대해
    mylist = one.split(',') #구분자','으로 linelist 한줄의 데이터를 나눔
    if (int)(mylist[1]) >= 19: #(int): ()안의 값을 정수로 변환. (int)(mylist[1]): mylist의 두번째요소(index 1)를 정수형으로 변환
        adult = '성인'
    else:
        adult = '미성년'
    text = mylist[0] + '/' + mylist[1].strip() + '/' + adult #strip(): 문자열 앞뒤의 공백을 제거: " 19 " => "19"
    myfile2.write(text + '\n')
myfile2.close()

myfile3 = open('result02.txt', 'rt', encoding='UTF-8')
line = 1
while line:
    line = myfile3.readline()
    print(line)
myfile3.close()