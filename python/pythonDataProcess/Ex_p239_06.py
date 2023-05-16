from pandas import Series
import matplotlib.pyplot as plt

#Matplotlib의 기본 글꼴을 'Malgun Gothic'으로 설정
plt.rc('font', family='Malgun Gothic')
#plt.rcParams['font.family'] = 'Malgun Gothic'와 같은 결과를 출력

#member라는 Series 생성
myindex = ['강감찬', '김유신', '이순신', '안익태', '윤동주']
mylist = [30, 20, 40, 30, 60]
member = Series(data=mylist, index=myindex)
print(member)
# 강감찬    30
# 김유신    20
# 이순신    40
# 안익태    30
# 윤동주    60
# dtype: int64
print('-' * 50)

print('# values 속성을 이용 요소들의 값 확인')
print(member.values)
# [30 20 40 30 60]
print('-' * 50)

print('# index 속성을 이용 색인 객체를 확인')
print(member.index)
# Index(['강감찬', '김유신', '이순신', '안익태', '윤동주'], dtype='object')
print('-' * 50)

member.plot(kind='bar', rot=0, use_index=True, grid=False, table=False, color=['r', 'g', 'b', 'y', 'm'])
plt.xlabel('학생 이름')
plt.ylabel('점수')
plt.title('학생별 시험 점수')

ratio = 100 * member / member.sum()
print(ratio)
# 강감찬    16.666667
# 김유신    11.111111
# 이순신    22.222222
# 안익태    16.666667
# 윤동주    33.333333
# dtype: float64
print('-' * 50)

for idx in range(member.size):
    value = str(member[idx]) + '건'
    ratioval = '%.1f%%' % (ratio[idx])

    plt.text(x=idx, y=member[idx] + 1, s=value, horizontalalignment='center')
    plt.text(x=idx, y=member[idx] / 2, s=ratioval, horizontalalignment='center')

meanval = member.mean()
print(meanval)
# 36.0
print('-' * 50)

average = '평균 : %d건' % meanval
plt.axhline(y=meanval, color='r', linewidth=1, linestyle='dashed')
plt.text(x=0, y=meanval + 1, s=average, horizontalalignment='center')

filename = 'graph02.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + 'Saved...')
plt.show()
# plt.show(): 이미지 파일로 저장한 후에 불필요한 그래프를 다시 한번 출력하는 것을 방지