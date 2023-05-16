import nltk
import matplotlib.pyplot as plt
import numpy as np

from wordcloud import WordCloud
from PIL import Image
from konlpy.tag import Komoran

plt.rc('font', family="Malgun Gothic")

class Visualization: # 시각화에 사용되는 단어 리스트를 저장하고, 해당 단어 리스트를 딕셔너리 형태로 변환
    #__init__ 메서드: 클래스의 생성자로서, 객체가 생성될 때 자동으로 호출되는 메서드
    def __init__(self, wordList):
        self.wordList = wordList #wordList는 시각화에 사용되는 단어 리스트
        self.wordDict = dict(wordList) #wordList를 딕셔너리 형태로 변환하여 클래스의 인스턴스 변수 wordDict에 저장

    def makeWordCloud(self): #워드 클라우드를 생성하고 이미지 파일로 저장
        alice_color_file = 'alice_color.png' # 'alice_color.png' 파일의 경로를 저장
        alice_coloring = np.array(Image.open(alice_color_file)) #이미지 파일을 배열 형태로 변환

        fontpath = "C:/Windows/Fonts/malgun.ttf" #폰트 파일의 경로를 fontpath 변수에 저장
        wordcloud = WordCloud(font_path=fontpath, mask=alice_coloring, relative_scaling=0.2, background_color='lightyellow')
        #mask 매개변수: 앞서 생성한 마스크 이미지를 지정
        #relative_scaling 매개변수: 단어 크기의 상대적인 스케일링을 조정
        #background_color 매개변수: 워드 클라우드의 배경색을 지정
        print(self.wordList)
        wordcloud = wordcloud.generate_from_frequencies(self.wordDict) # 단어 빈도수에 기반하여 워드 클라우드를 생성

        plt.imshow(wordcloud) #워드 클라우드 이미지를 표시
        plt.axis('off') #축을 표시하지 않음

        filename = 'xx_myWordCloud.png'
        plt.savefig(filename, dpi=400, bbox_inches='tight')
        print(filename + ' file saved..')

        plt.figure(figsize=(16,8))

    def makeBarChart(self):
        barcount = 10 #barcount 변수에 10을 저장
        #x축의 범위를 지정
        xlow, xhigh = -0.5, barcount - 0.5

        result =  self.wordList[:barcount]
        chartdata = [] #바 차트를 생성할 데이터
        xdata = [] #x축 레이블을 저장할 변수
        mycolor = ['r', 'g', 'b', 'y', 'm', 'c', '#FFF0F0', '#CCFFBB', '#05CCFF', '#11CCFF']

        for idx in range(len(result)):
            chartdata.append(result[idx][1]) #chartdata 리스트에 result의 빈도수를 추가
            xdata.append(result[idx][0]) #xdata 리스트에 result의 단어를 추가

            value = str(chartdata[idx]) + '건'
            plt.text(x=idx, y=chartdata[idx] - 5, s=value, fontsize=8, horizontalalignment='center')
            #s 매개변수에는 value 변수의 값을 전달하여 막대 위에 표시할 텍스트를 지정
            #horizontalalignment 매개변수: 텍스트의 가로 정렬 방식을 지정

        #plt.xticks() 함수: x축 눈금을 설정하는데 사용되는
        plt.xticks(range(barcount), xdata, rotation=45)
        #range(barcount)를 통해 x축의 위치를 설정
        #xdata를 통해 x축의 레이블을 설정

        #plt.bar() 함수: 막대를 생성
        plt.bar(range(barcount), chartdata, align='center', color=mycolor)
        #range(barcount): 막대의 위치를 설정
        #chartdata: 막대의 높이(빈도수)를 설정

        plt.title('상위 ' + str(barcount) + '빈도수')
        plt.xlim([xlow, xhigh])
        plt.xlabel('주요 키워드')
        plt.ylabel('빈도수')

        filename = 'myBarChart.png'
        plt.savefig(filename, dpi=400, bbox_inches='tight')
        print(filename + ' file saved..')

filename = '문재인대통령신년사.txt'
ko_con_text = open(filename, encoding='utf-8').read()
print(type(ko_con_text))
print('-' * 40)

komo = Komoran(userdic='user_dic.txt') #사용자 정의 사전 파일인 'user_dic.txt'를 userdic 매개변수로 지정하여 객체를 초기화
token_ko = komo.nouns(ko_con_text) #명사(nouns)만 추출한 결과를 token_ko 변수에 저장
stop_word_file = 'stopword.txt'
stop_file = open(stop_word_file, 'rt', encoding='utf-8')
stop_words = [ word.strip() for word in stop_file.readlines()] #불용어(stop words) 파일인 'stopword.txt'을 읽어들임

#stop_words에 포함되지 않은 단어들만 추출하여 tokens_ko 리스트에 저장
tokens_ko = [each_word for each_word in token_ko if each_word not in stop_words]

ko = nltk.Text(tokens=tokens_ko) #nltk.Text()를 호출하여 tokens=tokens_ko를 통해 단어 리스트 tokens_ko를 전달하여 ko 객체를 생성

print(type(ko))
print(type(ko.vocab()))
print(type(ko.vocab().most_common(50)))

data = ko.vocab().most_common(500)
wordlist = list()

#(word, count) 형태의 데이터를 순회하면서 조건을 만족하는 단어와 빈도수를 wordlist에 추가
for word, count in data:
    if (count >= 1 and len(word) >= 2): #count가 1 이상이고, word의 길이가 2 이상인 경우
        wordlist.append((word, count)) #단어와 빈도수를 wordlist에 추가

print(wordlist)
visual = Visualization(wordlist)
visual.makeWordCloud()
visual.makeBarChart()

print('finished')