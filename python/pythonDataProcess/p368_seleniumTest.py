import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome 웹드라이버를 사용하여 WebDriver 객체 생성
driver = webdriver.Chrome()
print(type(driver)) # WebDriver 객체의 타입 출력
# <class 'selenium.webdriver.chrome.webdriver.WebDriver'> #(Selenium 라이브러리에서 Chrome 웹드라이버를 사용하기 위해 제공되는 클래스)
print('-' * 50)

print('Go Google~!!')
url = 'http://www.google.com'
driver.get(url) # Google로 이동

search_textbox = driver.find_element(By.NAME, 'q') # 검색 텍스트 상자를 찾아서 검색어 입력

word = '북미정상회담'
search_textbox.send_keys(word)

search_textbox.submit() # 검색 텍스트 상자에서 엔터 키를 눌러 검색 수행

wait = 3
print(str(wait) + '초 동안 기다립니다.')
# 3초 동안 기다립니다.
time.sleep(wait)

imagefile = 'xx_capture.png'
driver.save_screenshot(imagefile) # 화면 스크린샷을 저장
print(imagefile + ' 이미지 저장')
# xx_capture.png 이미지 저장

wait = 3
driver.implicitly_wait(wait) # 3초 동안 암묵적 대기

driver.quit() # WebDriver 종료
print('Browser Exit~!!')
