import pandas as pd
import matplotlib.pyplot as plt

#Matplotlib의 기본 글꼴을 'Malgun Gothic'으로 설정
plt.rc('font', family='Malgun Gothic')
#plt.rcParams['font.family'] = 'Malgun Gothic'와 같은 결과를 출력

filename = 'tips.csv'
myframe = pd.read_csv(filename, encoding='utf-8', index_col=0)

print('head() 메소드 결과')
print(myframe.head()) #myframe 데이터프레임의 상위 5개 행을 출력
print('-' * 40)

mycolors = ['r', 'b']
labels = myframe['sex'].unique()
print(labels)

#변수 생성
cnt = 0

for finditem in labels:
    #해당 팀명의 행만 추출하고, 추출한 행에서 '안타'와 '타점' 열을 각각 x, y 데이터로 설정
    xdata = myframe.loc[myframe['sex'] == finditem, 'total_bill']
    ydata = myframe.loc[myframe['sex'] == finditem, 'tip']
    #scatter plot을 그리는 코드
    plt.plot(xdata, ydata, color=mycolors[cnt], marker='o', linestyle='None', label=finditem)
    # marker는 점의 모양
    # linestyle은 라인의 스타일을 설정<-None: 선 없이 출력
    # label은 각 팀명에 대한 범례를 설정
    cnt += 1 #cnt는 mycolors 리스트의 인덱스로 사용

plt.legend()
plt.xlabel("결제 총액") #x축 레이블
plt.ylabel("팁 비용") #y축 레이블
plt.title("결제 총액과 팁 비용의 산점도") #그래프 제목 설정
plt.grid(True) #plt.grid(True): 그리드 출력

plt.show()
# plt.show(): 이미지 파일로 저장한 후에 불필요한 그래프를 다시 한번 출력하는 것을 방지