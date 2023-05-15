import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic' #Matplotlib의 기본 글꼴을 'Malgun Gothic'으로 설정

#주어진 파일을 euc-kr로 인코딩하여 데이터프레임을 읽어들임
filename = 'dataframeGraph.csv'
myframe = pd.read_csv(filename, encoding='euc-kr') # encoding='euc-kr': 파일이 한국어로 작성됨=>한글 인코딩 방식

#.set_index(keys='데이터'): 데이터를 인덱스로 설정
myframe = myframe.set_index(keys='name') #name을 인덱스로 설정
print(myframe)
#       seoul  pusan  inchon  daejon
# name
# 강감찬      76     54      50      83
# 이순신      77     86      67      43
# 김유신      70     56      88      81
# 신사임당     93     63      71      78
# 유관순      44     79      54      97
# 이봉창      52     80      59      58
# 윤봉길      82     57      59      84
# 안중근      62     60      59      67
# 김구       76     69      52      45
# 김원봉      97     55      62      63

#myframe를 이용하여 선 그래프 작성(kind='line')
myframe.plot(title= 'Sometitle', kind='line', figsize=(10, 6), legend=True)
# figsize: 그래프의 크기를 지정
# legend: 범례를 표시할지 여부를 지정

filename = 'dataframeGraph01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + 'Saved...')
plt.show()
# plt.show(): 이미지 파일로 저장한 후에 불필요한 그래프를 다시 한번 출력하는 것을 방지