import numpy as np #numpy as np는 NumPy라이브러리를 가져올 때 일반적으로 사용되는 축약어

a = np.array([-1, 3, 2, -6]) #NumPy를 이용하여 a=[-1, 3, 2, -6] 배열 생성
b = np.array([3, 6, 1, 2]) #NumPy를 이용하여 b=[3, 6, 1, 2] 배열 생성

#생성한 A, B배열의 형식 변경 with 'reshape함수'
A = np.reshape(a, [2,2]) #배열 a를 2*2형식으로 변환한 배열 A
B = np.reshape(b, [2,2]) #배열 b를 2*2형식으로 변환한 배열 B
print("\nsol1")
print(A) # [[-1  3] \
          # [ 2 -6]]
print("\nsol2")
print(B) # [[3 6] \
          # [1 2]]

result3_1 = np.matmul(A, B) #NumPy의 matmul함수를 사용해 행렬A와 행렬B를 곱함 => 결과값을 result3_1변수에 할당
result3_2 = np.matmul(B, A) #NumPy의 matmul함수를 사용해 행렬B와 행렬A를 곱함 => 결과값을 result3_2변수에 할당
print("\nsol3-1")
print(result3_1) #[[0 0] \
                 # [0 0]]
print("\nsol3-2")
print(result3_2) #[[  9 -27] \
                 # [  3  -9]]

#생성한 a, b배열의 형식 변경 with 'reshape함수'
a = np.reshape(a, [1,4]) #배열 a를 1*4형식으로 변환한 배열 a : [[-1  3  2 -6]] #1차원 배열은 행렬이 아니기 때문에 reshape으로 행렬로 설정
b = np.reshape(b, [1,4]) #배열 b를 1*4형식으로 변환한 배열 b : [[3 6 1 2]] #1차원 배열은 행렬이 아니기 때문에 reshape으로 행렬로 설정

#transpose함수를 사용하여 전치
b2 = np.transpose(b) #NumPy의 transpose함수를 사용하여 배열b를 전치(transpose)하는 코드
print("\nsol4-1")
print(b2) #[[3]\
          # [6]\
          # [1]\
          # [2]]

result4 = np.matmul(a, b2) #NumPy의 matmul함수를 사용하여 배열a와 b2의 곱 계산
print("\nsol4-2")
print(result4) #[[5]]