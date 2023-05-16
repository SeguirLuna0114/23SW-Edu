import matplotlib.pyplot as plt
from wordcloud import WordCloud

plt.rcParams['font.family'] = 'Malgun Gothic'

#steve.txt파일을 rt모드(텍스트파일 읽기모드)로 열기
filename = 'steve.txt'
myfile = open(filename, 'rt', encoding='utf-8')

text = myfile.read() #파일의 내용을 text변수에 저장

wordcloud = WordCloud() #객체를 생성
wordcloud = wordcloud.generate(text) #generate() 메서드 사용 => text를 기반으로 워드 클라우드를 생성
print(type(wordcloud))
# <class 'wordcloud.wordcloud.WordCloud'>
print('-' * 40)

#wordcloud.words_: 워드 클라우드 객체에서 추출된 단어와 그에 대한 상대적인 빈도를 나타내는 딕셔너리. 단어를 키(key)로 가지고 해당 단어의 상대적인 빈도를 값(value)로 가지며, 단어의 크기를 결정하는 데 사용
bindo = wordcloud.words_
print(type(bindo)) #bindo변수 타입이 딕셔너리임
# <class 'dict'>
print('-' * 40)

#bindo.items()에서 반환된 딕셔너리 아이템을 빈도(x[1])를 기준으로 내림차순으로 정렬
sortedData = sorted(bindo.items(), key=lambda x : x[1], reverse=True) #bindo.items(): 딕셔너리 bindo의 키-값 쌍을 (key, value) 형태의 튜플로 반환하는 메서드
#key: 정렬기준 설정하는 매개변수(여기선, 빈도(x[1])로 지정하는 람다 함수를 의미)
print(sortedData)
print('-' * 40)

#sortedData 리스트에서 인덱스 0부터 9까지의 요소를 슬라이싱
charData = sortedData[0:10]
print(charData)
print('-' * 40)

xtick = []
chart = []
for item in charData:
    xtick.append(item[0]) #xtick 리스트에는 항목의 첫 번째 요소인 단어를 추가
    chart.append(item[1]) #chart 리스트에는 두 번째 요소인 빈도수를 추가
    # chart 리스트에는 해당 단어들의 빈도수가 저장됨 => 빈도수를 차트로 나타낼 수 있음

mycolor = ['r', 'g', 'b', 'y', 'm', 'c', '#FFF0F0', '#CCFFBB', '#05CCFF', '#11CCFF']
plt.bar(xtick, chart, color=mycolor)
plt.title('상위 빈도 Top 10')
filename = 'wordCloudEx01_01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' file saved...')

plt.figure(figsize=(12, 12))
plt.imshow(wordcloud)
plt.axis('off')

filename = 'wordCloudEx01_02.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' file saved...')
plt.show()