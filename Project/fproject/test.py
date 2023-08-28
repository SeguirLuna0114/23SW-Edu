from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

options = Options()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

url = "https://prod.danawa.com/list/?cate=13237976&15main_13_02"
driver.get(url)
cnt = 0
while True:
    if cnt == 0:
        cnt = 2
        print("A")
        
    elif cnt == 1:
        print("B")
        driver.find_element(By.CSS_SELECTOR, '#productListArea > div.prod_num_nav > div > a').click()
        sleep(2)
        cnt = 2
    else:
        print("C")
        for v in range(cnt):
            driver.find_element(By.CSS_SELECTOR, '#productListArea > div.prod_num_nav > div > a.edge_nav.nav_next').click()
            sleep(2)
        cnt += 1
        
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    num = soup.select("#productListArea > div.prod_num_nav > div > div > a")
    print(num)
    
    for p in range(1, len(num) + 1):
        driver.find_element(By.CSS_SELECTOR,f"#productListArea > div.prod_num_nav > div > div > a:nth-child({p})").click()
        sleep(2)
        
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find_all("a" , attrs={'name': "productName"})
        print("good")
        # print(data[0])
        for u in data:
            driver.get(u["href"])
            
            sleep(2)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            # print(soup)
            test = soup.find('tbody', attrs={'class': "high_list"})
            # print(test)
            print("so good")
            # print(test)
            te = test.select("tbody.high_list > tr")
            tee = test.select("td.mall > div > a")
            
            print(u.text)
            print(len(tee))
            print(len(te))

            for i, v in zip(te, tee):
                basong = i.find('span', attrs={'class', "stxt deleveryBaseSection"})
                prc = i.find('em', attrs={'class': "prc_t"})  
                icon = v.find('img')
                sell_page = v["href"]
                if basong == None:
                    continue
                elif icon == None:
                    icon = v["title"]
                else:
                    icon = icon["alt"]
                    icom_img = icon["src"]
                    
                print(f"아이콘 이미지: {icom_img}, 구매 페이지 이동 URL: {sell_page}")
                # print(f"업체: {icon}, 가격: {prc.text}, 배송가격: {basong.text}")
                
                sleep(2)

            
            driver.back()
        
    if len(num) < 10:
        break
    
driver.quit() 

