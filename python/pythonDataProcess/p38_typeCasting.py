str1 = '100' # 문자열
str2 = '200' # 문자열
str3 = '12.345' # 문자열

int1 = int(str1) # 정수변환
int2 = int(str2) # 정수변환
float1 = float(str3) # 실수변환

print(int1 == str1) #정수 != 문자열
print(type(int1)) #정수변환한 int1은 정수
print(type(int2)) #정수변환한 int2은 정수
print(type(float1)) #실수변환한 float1은 실수

sum = int1 + int2 # 정수 + 정수 = 정수=> sum은 정수
print('result1 : ', sum)

float2 = float1 + 35.2 #35.2도 float이기에 산수연산자
print('result2 : ', float2)
