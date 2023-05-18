from xml.etree.ElementTree import parse #parser 함수를 사용하여 XML 파일을 파싱

# XML 파일을 파싱하여 데이터를 추출

tree = parse('xmlEx_03.xml') #parse 함수를 사용하여 'xmlEx_03.xml' 파일을 파싱하여 트리 구조로 만듦
myroot = tree.getroot() #tree에서 최상위 요소(루트 요소)를 가져와서 myroot 변수에 저장
print(type(myroot))
#xml.etree.ElementTree.Element 클래스
print('-' * 40)

#.findall()메서드: 지정된 요소 이름과 일치하는 모든 요소를 반환
families = myroot.findall('가족') #myroot에서 '가족' 요소를 찾아서 families 변수에 저장
print(type(families))
#list 클래스
print('-' * 40)

for onefamily in families: #families 리스트의 각 요소를 순회
    for onesaram in onefamily: #자식 요소들을 순회
        if len(onesaram) >= 1: #onesaram의 자식 요소의 개수가 1개 이상
            print(onesaram[0].text) #첫 번째 자식 요소의 텍스트를 출력
        else:
            print(onesaram.attrib['이름']) #onesaram 요소의 '이름' 속성의 값을 출력
    print('-' * 40)
print('finished')
