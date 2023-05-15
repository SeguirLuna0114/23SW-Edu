import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic' #Matplotlib의 기본 글꼴을 'Malgun Gothic'으로 설정

myindex = ['이상화', '한용운','노천명','윤동주', '이육사'] #이름 list 정의
mylist = [30, 20, 40, 60, 50] #점수 list 정의
mycolors = ['blue', '#6AFF00', 'yellow', '#FF003C', 'green'] #색상 list 정의

#plt.pie(): 파이차트 생성 함수
plt.pie(x=mylist, labels=myindex, shadow=True, explode=(0, 0.1, 0, 0, 0), colors=mycolors, autopct='%1.2f%%', startangle=90, counterclock=False)
# x: 데이터를 의미. 이 경우 mylist
# labels: 각 파이 슬라이스에 사용할 레이블을 나타내는 목록입니다. 이 경우 myindex
# shadow: 차트가 그림자 효과를 갖는지 여부를 결정하는 부울 값으로, True로 설정시 그림자효과O
# explode: 파이 슬라이스 간의 간격을 나타내는 값의 튜플입니다. 이 경우 (0, 0.1, 0, 0, 0)으로 설정됩니다. 두 번째 값 0.1은 '한용운'에 해당하는 두 번째 슬라이스가 차트의 나머지 부분과 '반지름의 10%'로 '분리'됨을 의미합니다.
# colors: 각 파이 슬라이스에 사용할 색상 목록입니다. 이 경우 mycolors.
# autopct: 퍼센트를 표시하는 방법을 지정하는 '문자열 형식 지정자'입니다. 이 경우 '%1.2f%%'로 설정되어 있으므로 소수점 두 자리까지 표시합니다.
# startangle: 시작 각도를 결정하는 정수 값입니다. 이 경우 90으로 설정되어 있습니다.

plt.legend(loc=4) #legend: 범례를 추가하는데 사용됨. loc은 location의 약자로, 1부터 10까지의 숫자를 받아 각각 다른 위치에 범례를 배치(loc=4는 범례를 그래프의 오른쪽 하단에 배치)

filename = 'pieGraph02.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' Saved...')
plt.show()