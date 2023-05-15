import numpy as np

array = np.array([1.57, 2.48, 3.93, 4.33]) #1차원 배열 생성
print('\narray print') #1차원 배열의 경우에는 배열O, 행렬X
print(type(array)) #numpy.ndarray: ndarray는 다차원 배열을 나타내는 데이터 타입. 배열은 각 원소가 같은 데이터타입으로 이루어진 값들의 집합
print(array) #[1.57 2.48 3.93 4.33]

#np.ceil()함수는 인자로 전달된 배열의 각 요소에 대해 "올림 값"을 계산하는 함수
print('\nnp.ceil() function')
result = np.ceil(array) #np.ceil()함수를 통해 각 요소에 대하여 소수점 첫째자리에서 올림
print(result) #[2. 3. 4. 5.]

#np.floor() 함수는 인자로 전달된 배열의 각 요소에 대해 내림 값을 계산하는 함수
print('\nnp.floor() function')
result = np.floor(array) #np.floor()함수를 통해 각 요소에 대하여 소수점 첫째자리에서 버림
print(result) #[1. 2. 3. 4.]

#np.round()함수는 인자로 전달된 배열의 각 요소에 대해 반올림 값을 계산하는 함수
print('\nnp.round() function')
result = np.round(array) #np.round()함수를 통해 각 요소에 대하여 소수점 첫째자리에서 반올림
print(result) #[2. 2. 4. 4.]

#np.round(변수, n)함수는 소수점n번째 자리까지 반올림하여 나타낼지 계산
print('\n1 decimal place round')
result = np.round(array, 1) #array배열의 각 요소를 소수점 "첫번째 자리까지" 반올림한 값을 나타냄
print(result) #[1.6 2.5 3.9 4.3]

# np.sqrt() 함수를 사용하여 인자로 전달된 배열의 각 요소에 대해 제곱근 값을 계산
print('\nsqart() function')
result = np.sqrt(array) #sqrt함수로 array 배열의 각 요소의 제곱근 값 계산
print(result) #[1.25299641 1.57480157 1.98242276 2.0808652 ]

#arange(n)을 이용해 0~(n-1)까지 정수를 요소로 갖는 배열 생성
arr = np.arange(10) #np.arange() 함수를 사용하여 0부터 9까지의 정수를 요소로 가지는 배열 arr을 생성
print(arr) #[0 1 2 3 4 5 6 7 8 9]
print() #공백

# np.exp() 함수를 사용하여 배열의 각 요소에 대해 e의 지수값을 계산한 결과
print('\nexp() function')
result = np.exp(arr) #arr 배열의 각 요소에 대해 e의 지수값을 계산한 결과를 출력
print(result) #[1.00000000e+00 2.71828183e+00 7.38905610e+00 2.00855369e+01 5.45981500e+01 1.48413159e+02 4.03428793e+02 1.09663316e+03 2.98095799e+03 8.10308393e+03]

x = [5, 4] #list x생성
y = [6, 3] #list y생성

#np.maximum() 함수를 사용하여 배열(또는 리스트)을 인자로 받아서, 각 요소별로 큰 값을 반환
print('\nnp.maximum(x, y)')
result = np.maximum(x, y) #x와 y의 첫 번째 요소인 5와 6 중에서 큰 값인 6을 반환하고, 두 번째 요소인 4와 3 중에서 큰 값인 4를 반환
print(result) #[6 4]

print('-' * 30) #------------------------------

array1 = np.array([-1.1, 2.2, 3.3, 4.4]) #1차원 배열
print('\narray1')
print(array1) #[-1.1  2.2  3.3  4.4]

array2 = np.array([1.1, 2.2, 3.3, 4.4])
print('\narray2')
print(array2) #[1.1 2.2 3.3 4.4]

#np.abs() 함수는 인자로 받은 배열의 각 요소의 절대값을 반환
print('\nabs() function')
result = np.abs(array1) #배열 array1의 각 요소의 절대값을 구한 결과를 반환하는 코드
print(result) #[1.1 2.2 3.3 4.4]

#np.sum() 함수는 인자로 받은 배열의 모든 요소의 합을 반환
print('\nsum() function')
result = np.sum(array1) #배열 array1의 모든 요소의 합을 구한 결과를 반환
print(result) # -1.1 + 2.2 + 3.3 + 4.4 = 8.8

#np.equal() 함수는 인자로 받은 두 배열의 각 요소를 비교하여, 요소가 같으면 True, 다르면 False로 이루어진 배열을 반환
print('\ncompare')
result = np.equal(array1, array2) #np.equal() 함수를 사용하여 배열 array1과 array2의 각 요소를 비교한 결과를 반환
print(result) #[False  True  True  True]

print('\nnp.sum() and np.equal')
print('\nTrue is 1, False is 0 counting.')
result = np.sum(np.equal(array1, array2)) #np.equal(array1, array2)의 값을 [0 1 1 1]로 계산하여 모든 요소의 합을 반환
print(result) #0+1+1+1=3

#np.mean()함수는 모든 요소의 평균을 계산
print('\naverage')
result = np.mean(array2) #array2의 모든 요소의 평균을 계산
print(result) #(1.1 + 2.2 + 3.3 + 4.4)/4 = 2.75

arrX = np.array([[1,2], [3,4]], dtype=np.float64) #arrX는 2*2 크기의 2차원 배열. dtype=np.float64: 배열 내부의 원소들이 64비트 부동소수점형(float64)로 구성됨(데이터타입 지정하지 않을 경우 기본적으로 64비트 floating point number로 데이터타입 지정)
arrY = np.array([[5,6], [7,8]], dtype=np.float64) #arrY는 2*2 크기의 2차원 배열. dtype=np.float64: 배열 내부의 원소들이 64비트 부동소수점형(float64)로 구성됨

#element-wise: 배열의 원소/요소 간의 연산이 수행됨을 의미
#요소별 덧셈으로 더한 결과 출력(numpy는 기본적으로 element-wise 연산에 대해 교환법칙과 결합법칙을 따르기 때문)
print('\nadd of element by element')
#arrX + arrY와 np.add(arrX, arrY) 모두 같은 결과를 출력
print(arrX + arrY) #[[ 6.  8.] \
                   # [10. 12.]]
print(np.add(arrX, arrY)) #np.add(배열1, 배열2): numpy에서 제공하는 요소별 덧셈 함수

#요소별 뺄셈으로 뺀 결과 출력(numpy는 기본적으로 element-wise 연산에 대해 교환법칙과 결합법칙을 따르기 때문)
print('\nsub of element by element')
#arrX - arrY와 np.substract(arrX, arrY) 모두 같은 결과를 출력
print(arrX - arrY) #[[-4. -4.] \
                   # [-4. -4.]]
print(np.subtract(arrX, arrY)) #np.substract(배열1, 배열2): numpy에서 제공하는 요소별 뺄셈 함수

#요소별 곱셈으로 곱한 결과 출력
print('\nmul of element by element')
print(arrX * arrY) #[[ 5. 12.] \
                   # [21. 32.]]
print(np.multiply(arrX, arrY)) #np.multiply(배열1, 배열2): 두 배열을 element-wise 곱셈하는 함수

#요소별 나눗셈으로 나눈 결과 출력
print('\ndiv of element by element')
print(arrX / arrY) # [[0.2        0.33333333] \
                    # [0.42857143 0.5       ]]
print(np.divide(arrX, arrY)) #np.divide(배열1, 배열2): 두 배열을 요소별로 나누는 함수

# np.sqrt 함수는 인자로 받은 배열의 원소들에 대한 제곱근을 계산한 결과를 반환
print('\nsqrt of element by element') # arrX 행렬의 각 원소들에 대한 제곱근을 계산하는 코드
print(np.sqrt(arrX)) #[[1.         1.41421356] \
                     # [1.73205081 2.        ]]