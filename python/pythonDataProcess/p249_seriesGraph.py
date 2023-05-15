from pandas import Series
import matplotlib.pyplot as plt
#matplotlib: 파이썬에서 데이터를 시각화하기 위한 라이브러리.  다양한 스타일의 플롯을 만들고, 레이블, 제목 등을 추가하고, 축 범위와 눈금 표시 등을 제어 가능
#pyplot 모듈: 그래프를 그리기 위한 여러 유용한 함수들을 제공하며, 그래프를 생성하고 커스터마이즈하기 위한 다양한 옵션도 제공
plt.rcParams['font.family'] = 'Malgun Gothic' #Matplotlib의 기본 글꼴을 'Malgun Gothic'으로 설정

mylist = [30, 20, 40, 30, 60, 50]
myindex = ['강감찬', '김유신', '이순신', '안익태', '윤동주', '홍길동']

print(myindex)
# ['강감찬', '김유신', '이순신', '안익태', '윤동주', '홍길동']
print(mylist)
# [30, 20, 40, 30, 60, 50]
print('-' * 50)

# pandas의 Series를 이용하여 Series 객체를 생성
myseries = Series(data=mylist, index=myindex)
myylim = [0, myseries.max() +10] #y축 범위를 설정. 이때 범위는 0~최대값+10으로 설정됨 => myylim = [0, 60+10=70]

#myseries를 이용하여 선 그래프 작성(kind='line')
myseries.plot(title= '시험점수', kind='line', ylim=myylim, grid=True, rot=10, use_index=True)
# title: 그래프의 제목을 지정하는 옵션
# kind: 그래프의 종류를 지정하는 옵션 <- 여기서는 line을 지정하여 선 그래프
# ylim: y축의 범위를 지정
# grid: 그래프에 격자를 표시할지 여부를 지정
# rot: x축 라벨의 각도를 지정
# use_index: x축 라벨로 인덱스를 사용할지(True), 아니면 데이터의 값 자체를 사용할지(False) 여부를 지정

#시각화된 그래프를 이미지 파일로 저장
filename = 'seriesGraph01.png' #저장할 이미지 파일 이름 설정
plt.savefig(filename, dpi=400, bbox_inches='tight')
# dpi(dots per inch): 저장될 이미지의 해상도
# bbox_inches(Bounding Box Inches)='tight' : 시각화된 그림의 외곽 경계 상자를 그림의 크기에 맞게 조정하여 트리밍
print(filename + 'Saved...')
plt.show()
# plt.show(): 이미지 파일로 저장한 후에 불필요한 그래프를 다시 한번 출력하는 것을 방지