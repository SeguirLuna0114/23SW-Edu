mystring = "life is an egg" #데이터타입 string(문자열)
mylist = mystring.split() #데이터타입 list. split()을 이용해 띄어쓰기를 구분자로 문자열 split

print(mylist) #문자열로 이루어진 list

for idx in range(len(mylist)): #리스트에서 인덱스를 이용해 각 원소에 접근하는 반복문
    if idx % 2 == 0: #idx가 2로 나누면 나머지가 0인 경우 => 2의 배수인 경우(0,2,4,...)
        mylist[idx] = mylist[idx].upper() # 대문자로 출력
    else: #1,3,과 같이 홀수번째인 경우
        mylist[idx] = mylist[idx].lower() # 소문자로 출력

print(mylist)
#join 함수는 문자열을 이어붙이는데 사용됨: 'separator(구분자)'.join('문자열')
result = '#'.join(mylist) #구분자'#' => 빈칸에 '#'를 채워서 mylist문자열을 join
print('result : ', result)

result = ' '.join(mylist) #구분자 ' ' => 빈칸에 '공백'를 채워서 mylist문자열을 join
print('result : ', result)
