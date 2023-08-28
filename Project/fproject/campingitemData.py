from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument('--no-sandbox')
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

def get_url():
    url = "https://prod.danawa.com/list/?cate=13237976&15main_13_02"
    driver.get(url)
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup.select("#danawa_content > div.category_wrap > div.category_nav > div.cat_list_box > ul > li > a")
    cnt = 1
    url_list = []
    for a in tag:
        if a == None:
            pass
        else:
            url_list.append(f"https://prod.danawa.com{a['href']}")
            
    return {"MainURL" : url_list}


urls = get_url()["MainURL"]
cnt = 1
for url in urls:
    driver.get(url)
    sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    datas = soup.find_all("a" , attrs={'name': "productName"})
    for data in datas:
        try:
            print(url)
            driver.get(data["href"])
            sleep(3)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            main_img = soup.select("#productItem13375676 > div > div.thumb_image > a.thumb_link > img")["src"]
            test = soup.find('tbody', attrs={'class': "high_list"})
            te = test.select("tbody.high_list > tr")
            tee = test.select("td.mall > div > a")
            print(f"상품명: {data.text}, 상품이미지 URL : {main_img}")
            sleep(3)
        except:
            print(f"상품명: {data.text}")
            continue
        for i, v in zip(te, tee):
            basong = i.find('span', attrs={'class', "stxt deleveryBaseSection"})
            prc = i.find('em', attrs={'class': "prc_t"})  
            icon = v.find('img')
            sell_page = v["href"]
            if basong == None:
                continue
            elif icon == None:
                icon1 = v["title"]
            else:
                icon1 = icon["alt"]
                icom_img = icon['src']
            
            print(f"업체: {icon1}, 가격: {prc.text}, 배송가격: {basong.text}")
            print(f"아이콘 이미지: {icom_img}, 구매 페이지 이동 URL: {sell_page}")
    driver.close()  
    sleep(3)        
driver.quit() 