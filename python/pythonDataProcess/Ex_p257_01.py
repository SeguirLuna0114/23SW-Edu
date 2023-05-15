import urllib.request
import matplotlib.pyplot as plt

url = "https://shared-comic.pstatic.net/thumb/webtoon/648419/thumbnail/thumbnail_IMAG10_1421195d-13be-4cde-bcf9-0c78d51c5ea3.jpg"
savename = input('저장할 파일 이름 입력 : ')
result = urllib.request.urlopen(url)
# urllib.request.urlopen(url, result)

dataread = result.read()
print('# type(data) : ', type(dataread))

with open(savename, mode='wb') as f:
    f.write(dataread)
    print(savename + ' saved...')
