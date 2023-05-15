somelist = ['김의찬', '유만식', '이영철', '심수련', '윤기석', '노윤희', '황우철'] #class type = 'list'
print(somelist) #somelist 전체 출력
print(somelist[4]) #somelist의 4번째 데이터 출력 => 윤기석
print(somelist[-2]) #뒤에서 2번째 데이터 출력
print(somelist[1:4]) #1~3번째 데이터 출력
print(somelist[4:]) #4~마지막번째 데이터 출력
length = len(somelist) #list 데이터 길이=7
print(somelist[:length:2]) #0,2,4... 와 같이 짝수번째 데이터만 출력
print(somelist[1:length:2]) #1,3,5... 와 같이 홀수번째 데이터만 출력
