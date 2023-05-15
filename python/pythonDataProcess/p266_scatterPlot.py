import pandas as pd
import matplotlib.pyplot as plt

#Matplotlib의 기본 글꼴을 'Malgun Gothic'으로 설정
plt.rc('font', family='Malgun Gothic')
#plt.rcParams['font.family'] = 'Malgun Gothic'와 같은 결과를 출력

filename = '프로야구타자순위2021년.csv'

#.head(): 데이터프레임의 상위 5개 행 출력
myframe = pd.read_csv(filename, encoding='utf-8')
print('head() 메소드 결과')
print(myframe.head()) #myframe 데이터프레임의 상위 5개 행을 출력
#    순위    선수명   팀명     타율   경기   타석   타수  ...  도루  도루실패  볼넷  사구   삼진  병살타  실책
# 0   1    최형우  KIA  0.354  140  600  522  ...   0     0  70   5  101    9   0
# 1   2    손아섭   롯데  0.352  141  611  540  ...   5     0  61   2   56    9   1
# 2   3    로하스   KT  0.349  142  628  550  ...   0     1  65   5  132   11   4
# 3   4    박민우   NC  0.345  126  530  467  ...  13     6  36  15   48   12  10
# 4   5  페르난데스   두산  0.340  144  668  586  ...   0     1  58  13   42   26   1
print('-' * 40)

#.info(): 데이터프레임의 요약정보 출력
# 데이터프레임의 전체 크기 (행과 열의 개수)
# 각 열(column)의 이름, 데이터 타입, 비어있지 않은(non-null) 값의 개수
# 데이터프레임이 차지하는 메모리 용량 등
print('info() 메소드 결과')
print(myframe.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 53 entries, 0 to 52
# Data columns (total 19 columns):
#  #   Column  Non-Null Count  Dtype
print('-' * 40)

mycolors = ['r', 'g', 'b']
labels = ['두산', 'LG', '키움']
print(labels)

#각 팀에 대응하는 색상을 지정하기 위한 변수
cnt = 0

for finditem in labels:
    #해당 팀명의 행만 추출하고, 추출한 행에서 '안타'와 '타점' 열을 각각 x, y 데이터로 설정
    xdata = myframe.loc[myframe['팀명'] == finditem, '안타']
    ydata = myframe.loc[myframe['팀명'] == finditem, '타점']
    #scatter plot을 그리는 코드
    plt.plot(xdata, ydata, color=mycolors[cnt], marker='o', linestyle='None', label=finditem)
    # marker는 점의 모양
    # linestyle은 라인의 스타일을 설정<-None: 선 없이 출력
    # label은 각 팀명에 대한 범례를 설정
    cnt += 1 #cnt는 mycolors 리스트의 인덱스로 사용

plt.legend(loc=4) #loc=4: 우측 하단에 출력
plt.xlabel("안타 개수") #x축 레이블
plt.ylabel("타점") #y축 레이블
plt.title("안타와 타점에 대한 산점도") #그래프 제목 설정
plt.grid(True) #plt.grid(True): 그리드 출력

plt.show()
# plt.show(): 이미지 파일로 저장한 후에 불필요한 그래프를 다시 한번 출력하는 것을 방지