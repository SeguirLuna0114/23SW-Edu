import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic' #Matplotlib의 기본 글꼴을 'Malgun Gothic'으로 설정

#주어진 파일을 euc-kr로 인코딩하여 데이터프레임을 읽어들임
filename = 'ex802.csv'
myframe = pd.read_csv(filename, index_col='type', encoding='utf-8')

myframe.plot(title= '지역별 차종 교통량', kind='line', legend=True, rot=0)
print(myframe)
#       seoul  pusan  ulsan  daejon  daegu
# type
# 대형차      60     40     70      50     60
# 중형차      55     50     55      40     60
# 소형차      65     60     75      30     56

filename = 'dataframeGraph02_04.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
# dpi(dots per inch): 저장될 이미지의 해상도
# bbox_inches(Bounding Box Inches)='tight' : 시각화된 그림의 외곽 경계 상자를 그림의 크기에 맞게 조정하여 트리밍
print(filename + 'Saved...')
plt.show()
# plt.show(): 이미지 파일로 저장한 후에 불필요한 그래프를 다시 한번 출력하는 것을 방지