from pandas import Series
import matplotlib.pyplot as plt
#matplotlib: 파이썬에서 데이터를 시각화하기 위한 라이브러리.  다양한 스타일의 플롯을 만들고, 레이블, 제목 등을 추가하고, 축 범위와 눈금 표시 등을 제어 가능
plt.rcParams['font.family'] = 'Malgun Gothic'

mylist = [30, 20, 40, 60, 50]
myindex = ['이상화', '한용운', '노천명', '윤동주', '이육사']

print(myindex)
# ['이상화', '한용운', '노천명', '윤동주', '이육사']
print(mylist)
# [30, 20, 40, 60, 50]
print('-' * 50)

myseries = Series(data=mylist, index=myindex)
myylim = [0, myseries.max() +10]
myseries.plot(title= '금월실적', kind='line', ylim=myylim, grid=False, rot=10, use_index=True, color=['b'])
# grid: 그래프에 격자를 표시할지 여부를 지정
# color: 그래프 색상을 '리스트 형태로' 설정하는 옵션. <-b(blue)

filename = 'seriesGraph02.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + 'Saved...')
plt.show()