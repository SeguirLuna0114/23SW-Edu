import pandas as pd
import matplotlib.pyplot as plt

#Matplotlib의 기본 글꼴을 'Malgun Gothic'으로 설정
plt.rc('font', family='Malgun Gothic')
#plt.rcParams['font.family'] = 'Malgun Gothic'와 같은 결과를 출력

filename = 'mygraph.csv'
myframe = pd.read_csv(filename, index_col='이름', encoding='utf-8')
myframe.index.name = '이름'
myframe.columns.name = '시험 과목'

myframe.plot(kind='bar', rot=0, stacked=True, title='학생별 누적 시험 점수', legend=True)
print(myframe)
# 시험 과목  국어  영어
# 이름
# 강감찬    30  35
# 이순신    40  45
# 김유신    50  50
# 을지문덕   30  60
# 김춘추    30  40
# 선덕여왕   30  50
print('-' * 40)

filename = 'dataframeGraph02_04.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' Saved…')
print('-' * 40)
plt.show()
# plt.show(): 이미지 파일로 저장한 후에 불필요한 그래프를 다시 한번 출력하는 것을 방지