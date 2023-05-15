from pandas import Series
import matplotlib.pyplot as plt

#Matplotlib의 기본 글꼴을 'Malgun Gothic'으로 설정
plt.rc('font', family='Malgun Gothic')
#plt.rcParams['font.family'] = 'Malgun Gothic'와 같은 결과를 출력

#member라는 Series 생성
myindex = ['강감찬', '홍길동', '이순신', '최영']
member = Series(data=[20, 60, 80, 40], index=myindex)
print(member)
# 강감찬    20
# 홍길동    60
# 이순신    80
# 최영     40
# dtype: int64
print('-' * 50)

print('# values 속성을 이용 요소들의 값 확인')
print(member.values)
print('-' * 50)

print('# index 속성을 이용 색인 객체를 확인')
print(member.index)
print('-' * 50)

member.plot(kind='bar', rot=40, ylim=[0, member.max() + 20], use_index=True, grid=False, table=False, color=['r', 'g', 'b', 'y'])
#table: 그래프 아래에 테이블을 표시할 것인지 여부

plt.xlabel('학생 이름') # .xlabel(): x축 라벨 설정
plt.ylabel('점수') # .ylabel(): y축 라벨 설정
plt.title('학생별 시험 점수') #.title(): 그래프 제목 설정
#member.plot(title='학생별 시험점수', xlabel='학생 이름', ylabel='점수')라고 적을 수 있음

#member 시리즈에서 전체 합을 구한 후 각 학생이 차지하는 비율을 계산
ratio = 100 * member / member.sum()
print(ratio)
# 강감찬    16.666667
# 김유신    11.111111
# 이순신    22.222222
# 안익태    16.666667
# 윤동주    33.333333
# dtype: float64
print('-' * 50)

for idx in range(member.size): #member시리즈의 크기만큼 반복
    value = str(member[idx]) + '건' #member시리즈 항목의 값을 문자로 출력
    #ratio[idx]값을 백분율(%) 형태의 문자열로 표현
    ratioval = '%.1f%%' % (ratio[idx]) # ratio[idx] 값을 소수점 아래 첫번째 자리까지만 표시(%.1f)하고, 그 뒤에 퍼센트 기호(%)를 붙여서(%%) 문자열 형태('')로 만드는 것

    plt.text(x=idx, y=member[idx] + 1, s=value, horizontalalignment='center')
    plt.text(x=idx, y=member[idx] / 2, s=ratioval, horizontalalignment='center')

meanval = member.mean()
print(meanval)
# 36.0
print('-' * 50)

average = '평균 : %d건' % meanval
plt.axhline(y=meanval, color='r', linewidth=1, linestyle='dashed')
plt.text(x=0, y=meanval + 1, s=average, horizontalalignment='center')

filename = 'graph01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + 'Saved...')
plt.show()
# plt.show(): 이미지 파일로 저장한 후에 불필요한 그래프를 다시 한번 출력하는 것을 방지