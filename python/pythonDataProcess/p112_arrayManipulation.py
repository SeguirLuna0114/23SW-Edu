import numpy as np

# repeat함수를 사용하여 특정변수의 값을 반복하여 배열 생성
print('\nnp.repeat function')
su1 = 2
rep_cnt1 = 5
result = np.repeat(su1, rep_cnt1) # repeat함수를 사용하여 su1(2)변수의 값을 rep_cnt1(5)만큼 반복하여 배열 생성
print(type(result)) #np repeat로 인해 생성된 배열의 데이터 타입(자료형)은 'numpy.ndarray'(NumPy 배열)
print(result) #[2 2 2 2 2] : 2를 5번 반복하여 생성된 1차원 NumPy 배열

array1 = np.array([1, 2]) #[1, 2] 행렬 생성 => 자료형은 NumPy배열
array2 = np.array([3, 4]) #[3, 4] 행렬 생성 => 자료형은 NumPy배열
print('\narray1')
print(array1) #[1,2]가 할당된 1차원 NumPy배열
print('\narray2')
print(array2) #[3,4]가 할당된 1차원 NumPy배열

#concatenate 함수를 사용하여 변수 연결하여 하나의 배열로 합치기
print('\nnp.concatenate function')
result = np.concatenate((array1, array2)) #concatenate 함수를 활용하여 array1변수와 array2변수를 연결하여 하나의 배열로 합치는 코드
print(result) #[1 2 3 4]

su2 = 3
rep_cnt2 = 4
print('\nfunction repeat')
abcd = np.repeat(su1, rep_cnt1) # repeat함수를 사용하여 su1(2)변수의 값을 rep_cnt1(5)만큼 반복하여 배열 생성: [2 2 2 2 2]
defg = np.repeat(su2, rep_cnt2) # repeat함수를 사용하여 su2(3)변수의 값을 rep_cnt2(4)만큼 반복하여 배열 생성: [3 3 3 3]
result = np.concatenate((abcd, defg)) #concatenate 함수를 활용하여 abcd변수와 defg변수를 연결하여 하나의 배열로 합치는 코드
print(result) #[2 2 2 2 2 3 3 3 3]

array3 = np.array([1, 2, 3, 4, 5, 6]) #array3의 데이터타입은 numpy.ndarray(NumPy 배열)

#reshape function을 이용하여 배열의 형태 변경
print('\nreshape function')
print('2row 3col') #2행 3열 배열
result = np.reshape(array3, [2,3]) # reshape함수를 사용하여 array3 배열의 형태를 [2,3]으로 변경
print(result) #[[1 2 3] \
              # [4 5 6]] : 2행 3열 행렬

print('3row 2col') #3행 2열 배열
result = np.reshape(array3, [3,2]) # reshape함수를 사용하여 array3 배열의 형태를 [3,2]으로 변경
print(result) #[[1 2] \
              # [3 4] \
              # [5 6]] : 3행 2열 행렬('numpy.ndarray'(NumPy 배열))

array4 = np.array([[3, 6, 2], [4, 1, 5]]) #2행 3열의 배열 형성
print('\narray4')
print(array4) # [[3 6 2] \
               # [4 1 5]]

#transpose함수를 사용하여 배열 전치
print('\ntransposed array')
result = np.transpose(array4) # NumPy의 transpose함수를 사용하여 array4 배열을 전치
print(result)