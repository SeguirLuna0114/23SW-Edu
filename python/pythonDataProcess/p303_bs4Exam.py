from bs4 import BeautifulSoup

html = open('fruits.html', 'r', encoding="utf-8")
soup = BeautifulSoup(html, 'html.parser')
body = soup.select_one("body")
ptag = body.find('p')
print('1번째 p 태그 : ', ptag['class'])
# 1번째 p 태그 :  ['ptag', 'red']

ptag['class'][1] = 'white'
print('1번째 p 태그 : ', ptag['class'])
# 1번째 p 태그 :  ['ptag', 'white']

ptag['id'] = 'apple'
print('-' * 50)
print('1번째 p 태그의 id 속성 : ', ptag['id'])
# 1번째 p 태그의 id 속성 :  apple
print('-' * 50)

body_tag = soup.find('body')
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

idx = 0
print('children 속성으로 하위 항목 보기')
for child in body_tag.children:
    idx += 1
    print(str(idx) + '번째 요소 : ', child)
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
mydiv = soup.find('div')
print(mydiv)
# <div id="container">
# <p class="hard">과일</p>
# </div>
print('-' * 50)

print('div의 부모 태그')
print(mydiv.parent)
# <body>
# <p align="center" class="ptag white" id="apple">사과</p>
# <p align="center" class="ptag yellow">참외</p>
# <p align="center" class="ptag blue">블루베리</p>
# <div id="container">
# <p class="hard">과일</p>
# </div>
# </body>
print('-' * 50)

mytag = soup.find("p", attrs={'class' : 'hard'})
print(mytag)
# <p class="hard">과일</p>
print('-' * 50)

print('mytag의 부모 태그는? ')
print(mytag.parent)
# <div id="container">
# <p class="hard">과일</p>
# </div>
print('-' * 50)

print('mytag의 모든 상위 부모 태그들의 이름')
parents = mytag.find_parents()
for p in parents:
    print(p.name)
    # div
    # body
    # html
    # [document]
print('-' * 50)