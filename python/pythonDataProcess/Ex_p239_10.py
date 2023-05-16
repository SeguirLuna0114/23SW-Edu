import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic' #Matplotlib의 기본 글꼴을 'Malgun Gothic'으로 설정

filename = 'mpg.csv'
myframe = pd.read_csv(filename, encoding='utf-8')

#.unique()메소드: 데이터프레임 객체에서 ['특정 열']의 고유한 값(중복을 제거한)을 가져옴
print(myframe['drv'].unique())#myframe 데이터프레임 객체에서 'drv'열의 고유 값을 가져와 출력함

frame01 = myframe.loc[myframe['drv'] == 'f', 'hwy']#myframe['drv'] == 'f': drv열의 값이 f인 행만 선택 -> 선택된 행들의 'hwy'열(column)값을 저장
frame01.index.name = '전륜 구동' #frame01객체의 인덱스 이름을 '전륜구동'으로 지정
print(frame01.head())#.head()명령어로 처음 5개의 행(row)을 출력함
print('-' * 40)

frame02 = myframe.loc[myframe['drv'] == '4', 'hwy']
frame02.index.name = '4륜 구동'
print(frame02.head())
print('-' * 40)

frame03 = myframe.loc[myframe['drv'] == 'r', 'hwy']
frame03.index.name = '후륜 구동'
print(frame03.head())
print('-' * 40)

#생성한 데이터프레임 객체를 합쳐서 새로운 객체로 저장
totalframe = pd.concat([frame01, frame02, frame03], axis=1, ignore_index=True) #데이터프레임 frame01, frame02, frame03을 수평 방향(axis=1)으로(concat) 합침. #ignore_index=True: 기존의 인덱스가 아닌, 새로운 인덱스를 생성
totalframe.columns = ['f', '4', 'r'] #.columns = [list]: 데이터프레임의 열이름 변경
print(totalframe.head())
print('-' * 40)

#데이터프레임에 대한 상자그림(box plot) 생성
totalframe.plot(kind='box') #kind='box'로 box plot 생성

plt.xlabel("구동 방식")
plt.ylabel("주행 마일수")
plt.grid(False)
plt.title("고속도로 주행 마일수의 상자 수염")
#totalframe.plot(xlabel='구동 방식',ylabel='주행 마일수', grid=False, title='고속도로 주행 마일수의 상자 수염')

filename = 'boxPlot02_image.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' Saved...')
plt.show()