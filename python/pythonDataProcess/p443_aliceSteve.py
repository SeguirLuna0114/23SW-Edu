import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from wordcloud import WordCloud
from wordcloud import STOPWORDS
from wordcloud import ImageColorGenerator

#Python의 PIL(Pillow) 라이브러리를 사용하여 이미지 파일을 열고, 이미지 파일의 형식 및 속성을 확인
image_file = 'alice.png' # 해당 이미지 파일이 저장된 디렉토리와 파일 이름을 포함

#Image.open() 함수: 이미지 파일을 연다
img_file = Image.open(image_file)
print(type(img_file)) #PNG 형식의 이미지 파일을 나타내는 PIL(Pillow)의 PngImageFile 클래스의 객체
# <class 'PIL.PngImagePlugin.PngImageFile'>
print('-' * 40)

# 이미지 데이터를 NumPy 배열로 변환
alice_mask = np.array(img_file) #변수에 저장된 이미지를 NumPy 배열로 변환
print(type(alice_mask)) #NumPy 배열을 나타내는 클래스인 numpy.ndarray의 객체
# <class 'numpy.ndarray'>
print('-' * 40)

plt.figure(figsize=(8, 8))
plt.imshow(alice_mask, interpolation='bilinear')
plt.axis('off') #graph의 축을 없앰

filename = 'alice_graph01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' file saved...')


#stopwords 세트 생성: 텍스트 처리 작업에서 제거해야 하는 일련의 단어들을 포함하는 사전(set)
mystopwords = set(STOPWORDS) # STOPWORDS를 사용하여 불용어(stopwords) 세트
mystopwords.add('said') #'said'라는 단어를 mystopwords 세트에 추가
mystopwords.update(['hohoho', 'hahaha']) #update() 메서드를 사용 => ['hohoho', 'hahaha']라는 리스트의 요소들을 mystopwords 세트에 추가

#len() 함수: 세트의 요소 개수를 반환
print(len(mystopwords)) #세트의 길이 출력=해당세트의 총 길이
# 195
print(mystopwords)

#WordCloud() 함수=> WordCloud 객체를 생성
wc = WordCloud(background_color='white', max_words=2000, mask=alice_mask, stopwords=mystopwords)
#max_words=2000: 워드 클라우드에 표시할 최대 단어 수를 2000개로 설정
#mask=alice_mask: 워드 클라우드의 모양을 지정
#stopwords=mystopwords: 워드 클라우드에서 제외할 불용어(stopwords) 세트를 mystopwords 변수로 지정

stevefile = 'steve.txt' #텍스트파일의 경로를 할당
text = open(stevefile, 'rt', encoding='utf-8')
text = text.read()

wc = wc.generate(text) #WordCloud 객체(wc)를 기반으로 텍스트 데이터(text)를 처리
print(wc.words_) #wc.words_는 딕셔너리 형태로 단어와 빈도수의 쌍으로 구성

#plt.figure(): Matplotlib figure를 생성.
# figsize=(n1,n2): figure의 크기를 (n1, n2)로 설정
plt.figure(figsize=(12, 12))
#mshow() 함수: 이미지를 플롯(plot)으로 표시
plt.imshow(wc, interpolation='bilinear')
#interpolation: 이미지의 보간(interpolation) 방법을 설정. 'bilinear'는 양선형 보간법을 의미하며, 부드러운 이미지 출력을 위해 사용
plt.axis('off') #플롯의 축(axis)을 제거

filename = 'alice_graph02.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' file saved...')

#steve.txt' 파일의 내용을 기반으로 WordCloud를 생성->생성된 워드 클라우드를 'alice_color.png' 이미지 모양에 맞춰서 출력
#이미지 파일 열기 -> 이미지를 NumPy 배열로 변환
alice_color_file = 'alice_color.png'
alice_color_mask = np.array((Image.open(alice_color_file)))

wc = WordCloud(background_color='white', max_words=2000, mask=alice_color_mask, stopwords=mystopwords, max_font_size=40, random_state=42)
#mask=alice_color_mask: 워드 클라우드의 모양을 'alice_color.png' 이미지로 지정
wc = wc.generate(text)

plt.figure(figsize=(12, 12))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')

filename = 'alice_graph03.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' file saved...')

plt.figure(figsize=(12, 12))
plt.imshow(alice_color_mask, interpolation='bilinear')
plt.axis('off')

filename = 'alice_graph04.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' file saved...')

image_colors = ImageColorGenerator(alice_color_mask)

plt.figure(figsize=(12, 12))
#wc.recolor() 함수: 워드 클라우드 객체 wc의 색상을 재설정
newwc = wc.recolor(color_func=image_colors, random_state=42)
#color_func 매개변수: 이미지의 색상을 추출하여 워드 클라우드에 적용하는 image_colors 함수를 지정함
plt.imshow(newwc, interpolation='bilinear')
plt.axis('off')

filename = 'alice_graph05.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' file saved...')

print('finished...')