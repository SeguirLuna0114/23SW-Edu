from bs4 import BeautifulSoup #bs4 라이브러리에서 BeautifulSoup 클래스를 불러오는 코드
#BeautifulSoup: HTML/XML 등의 마크업 언어로 작성된 문자열을 파싱하여 파이썬에서 다루기 쉬운 트리구조 형태로 변환하는 파이썬 패키지

#html 파일을 열어 BeautifulSoup을 사용하여 파싱
html = open('fruits.html', 'r', encoding="utf-8") # 'fruits.html' 파일을 읽기 모드('r')로 열어서 변수 html에 저장
# r 모드: 일반적인 텍스트 파일을 읽을 때 사용
# (rb 모드: 이진(binary) 파일을 읽을 때 사용.  이미지, 동영상, 음악 파일 등의 텍스트파일 아닌 다른형태의 파일을 의미)
soup = BeautifulSoup(html, 'html.parser') #html문서 파싱하여 파이썬에서 사용하기 쉬운 형태로 만들어주는 라이브러리
#'html.parser': BeautifulSoup이 HTML 문서를 파싱하는 데 사용하는 파서의 종류를 지정(파이썬의 표준 라이브러리 html.parser를 사용하겠다는 의미)
body = soup.select_one("body") #BeautifulSoup 객체 soup에서 body 태그를 선택
ptag = body.find('p') #body 태그에서 첫 번째 p 태그를 찾음
# <p align="center" class="ptag red">사과</p>
print('\n 1번째 p 태그 : ', ptag['class']) #ptag['class']는 ptag의 class 속성값을 리스트 형태로 반환
# 1번째 p 태그 :  ['ptag', 'red']

# HTML 태그 - id 속성과 class 속성이 존재
# id 속성: 해당 요소의 고유한 식별자를 나타냄
# class 속성: 여러 요소들을 그룹으로 묶어 스타일을 적용하거나, 자바스크립트로 조작할 때 유용하게 사용

#파싱된 HTML 문서에서 ptag의 속성값중 인덱스값에 해당하는 항목을 변경
ptag['class'][1] = 'white' #ptag['class']의 인덱스1(2번째 항목)를 white로 바꿈
# class 속성: 여러 요소들을 그룹으로 묶어 스타일을 적용하거나, 자바스크립트로 조작할 때 유용하게 사용
print('\n 1번째 p 태그 : ', ptag['class'])
# 1번째 p 태그 :  ['ptag', 'white'] #red -> white로 변경됨
print('-' * 50)

#파싱된 HTML 문서에서 ptag에 해당하는 태그의 속성값 변경
ptag['id'] = 'apple' #ptag에 해당하는 첫 번째 p 태그의 id 속성값을 'apple'로 변경
print('1번째 p 태그의 id 속성 : ', ptag['id'])
# 1번째 p 태그의 id 속성 :  apple
# id 속성: 해당 요소의 고유한 식별자를 나타냄
print('-' * 50)

# soup.find() 메소드: soup 객체 안에서 찾고자 하는 태그나 속성을 검색할 때 사용. 찾고자하는 태그나 속성의 이름을 문자열 형태로 전달. 여러 태그 존재시, 첫번째 태그만 반환
body_tag = soup.find('body') #soup에서 첫 번째 'body 태그'를 찾아 그 결과를 body_tag 변수에 저장
print(body_tag)
# <body>
# <p align="center" class="ptag white" id="apple">사과</p>
# <p align="center" class="ptag yellow">참외</p>
# <p align="center" class="ptag blue">블루베리</p>
# <div id="container">
# <p class="hard">과일</p>
# </div>
# </body>
print('-' * 50)

#.children()메소드: 하위 요소(항목)을 가져옴. 이들은 NavigableString과 Tag 객체들로 구성됨
idx = 0
print('children 속성으로 하위 항목 보기')
for child in body_tag.children: #idx 변수를 이용하여 몇 번째 요소인지 출력하고, 해당 요소를 child 변수에 저장하여 출력
    idx += 1
    print(str(idx) + '번째 요소 : ', child) #'fruits.html' 파일의 'body' 태그의 하위 요소들이 순서대로 출력
    # 1번째 요소 :
    #
    # 2번째 요소 :  <p align="center" class="ptag white" id="apple">사과</p>
    # 3번째 요소 :
    #
    # 4번째 요소 :  <p align="center" class="ptag yellow">참외</p>
    # 5번째 요소 :
    #
    # 6번째 요소 :  <p align="center" class="ptag blue">블루베리</p>
    # 7번째 요소 :
    #
    # 8번째 요소 :  <div id="container">
    # <p class="hard">과일</p>
    # </div>
    # 9번째 요소 :
print('-' * 50)

# soup에서 첫 번째 'div 태그'를 찾아 그 결과를 mydiv 변수에 저장
mydiv = soup.find('div')
print(mydiv)
# <div id="container">
# <p class="hard">과일</p>
# </div>
print('-' * 50)

#.parent()메소드: 부모태그 반환
print('div의 부모 태그')
print(mydiv.parent) #body 태그를 반환
# <body>
# <p align="center" class="ptag white" id="apple">사과</p>
# <p align="center" class="ptag yellow">참외</p>
# <p align="center" class="ptag blue">블루베리</p>
# <div id="container">
# <p class="hard">과일</p>
# </div>
# </body>
print('-' * 50)

#.find()메소드: 해당태그를 찾아주는 역할
# .find(name, attrs, recursive, string, **kwargs)의 구조를 사용
# name: 찾고자 하는 태그의 이름(반드시 입력되어야 함). name 값이 True이면, 현재 문서에서 사용된 모든 태그를 반환
# attrs: 찾고자 하는 태그의 속성. dictionary 형태{'key':'value'}로 지정.
# recursive: 탐색 범위를 결정하는 값. 기본값은 True => 자식 태그에 대해서도 재귀적으로 탐색을 수행.
# string: 태그 안에 있는 문자열을 검색.
# **kwargs: 속성값을 직접 지정해주는 방식으로 사용.
mytag = soup.find("p", attrs={'class' : 'hard'}) #'p'태그 중에서, class속성이 hard인 요소를 찾아 mytag 변수에 할당 -> 출력
print(mytag)
# <p class="hard">과일</p>
print('-' * 50)

#.parent(): mytag 요소를 감싸는 바로 위의 요소 반환
print('mytag의 부모 태그는? ') #=> <p class="hard">Hard Text</p> 요소의 부모는 <div> 요소
print(mytag.parent) # <div> 요소를 나타내는 Beautiful Soup 객체가 반환
# <div id="container">
# <p class="hard">과일</p>
# </div>
print('-' * 50)

#.find_parents() 메서드: mytag 요소의 조상 요소들을 반환
print('mytag의 모든 상위 부모 태그들의 이름')
parents = mytag.find_parents()
#for문을 이용하여 각 조상 요소들의 이름을 출력
for p in parents: #출력 결과는 mytag 요소의 부모 요소부터 최상위 요소까지의 이름이 순서대로 나열됨
    print(p.name)
    # div
    # body
    # html
    # [document]
print('-' * 50)