import urllib.request
import matplotlib.pyplot as plt

# 다운로드할 이미지 파일의 URL을 지정 -> urllib.request.urlopen() 함수를 이용해 데이터 가져옴
url = "https://shared-comic.pstatic.net/thumb/webtoon/648419/thumbnail/thumbnail_IMAG10_1421195d-13be-4cde-bcf9-0c78d51c5ea3.jpg"
savename = input('저장할 파일 이름 입력 : ') #저장할 이미지 파일의 이름을 입력
result = urllib.request.urlopen(url) #urllib.request.urlopen() 함수를 이용하여 URL에 접속하여 데이터를 가져옴
# urllib.request.urlopen(url, result)

dataread = result.read() #가져온 데이터를 read메서드를 사용하여 읽어옴
print('# type(data) : ', type(dataread))

# 지정한 이름의 파일을 wb(바이너리 쓰기) 모드로 열고, 파일 객체를 f에 할당
with open(savename, mode='wb') as f:
    f.write(dataread) #파일 객체 f를 이용하여 가져온 데이터를 해당 파일에 쓰기
    print(savename + ' saved...')
