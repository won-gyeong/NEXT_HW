from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup
import requests as req

# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = "C:/Users/wgjo0/OneDrive/문서/조원경/고려대학교/NEXT/NEXT_HW/Session5/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

# 영화차트 사이트 접속 - selenium
driver.get("https://movie.naver.com/")

# csv 저장
import csv
file = open('movie.csv',mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["title","outline", "director", "rate"])

# 영화랭킹 카테고리 클릭 - selenium
chartbtn = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
chartbtn.click()
time.sleep(1)

# 1-20위 가져오기 - bs4
res1 = driver.page_source

soup1 = BeautifulSoup(res1, "html.parser")

for i in range(2, 12):
      rank = soup1.select_one(f"#old_content > table > tbody > tr:nth-child({i}) > td.title > div > a").text
      print(rank)
      time.sleep(1)

for i in range(13,23):
      rank = soup1.select_one(f"#old_content > table > tbody > tr:nth-child({i}) > td.title > div > a").text
      print(rank)
      time.sleep(1)

# 1-20위 정보 가져오기 bs4+selenium
res1 = driver.page_source
soup1 = BeautifulSoup(res1, "html.parser")

change = driver.find_element(By.XPATH, f'//*[@id="old_content"]/div[1]/ul/li[2]/a/img')
change.click()

for i in range(2,12):

            title = driver.find_element(By.XPATH, f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a')
            title.click()
      
            res2=driver.page_source
            soup2 = BeautifulSoup(res2, "html.parser")

            title1 = soup2.select_one('#content > div.article > div.mv_info_area > div.mv_info > h3 > a:nth-child(1)').text
            outline = soup2.select_one("#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a").text
            director = soup2.select_one("#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p > a").text
            rate = soup2.select_one('#actualPointPersentBasic > div > span').text
    
            print('제목:', title1, '개요:', outline, '감독:', director, rate)
      
      
            writer.writerow([title1, outline, director, rate])
            driver.back()
            time.sleep(1)

for i in range(13,23):

            title = driver.find_element(By.XPATH, f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a')
            title.click()
      
            res2=driver.page_source
            soup2 = BeautifulSoup(res2, "html.parser")

            title1 = soup2.select_one('#content > div.article > div.mv_info_area > div.mv_info > h3 > a:nth-child(1)').text
            outline = soup2.select_one("#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a").text
            director = soup2.select_one("#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p > a").text
            rate = soup2.select_one('#actualPointPersentBasic > div > span').text
    
            print('제목:', title1, '개요:', outline, '감독:', director, rate)
      
      
            writer.writerow([title1, outline, director, rate])
            driver.back()
            time.sleep(1)


file.close()

file = open('fav_movie.csv',mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["fav_title","fav_dir", "rate", "coun"])

# 좋아하는 영화 검색하고(selenium) 제목, 감독, 스크롤 내려서 평점과 리뷰 개수 가져오기(bs4)
search_box = driver.find_element(By.XPATH, '//*[@id="ipt_tx_srch"]')
search_box.send_keys("Bolt")
search_box.send_keys(Keys.ENTER)
time.sleep(1)


ff = driver.find_element(By.XPATH, '//*[@id="old_content"]/ul[2]/li[1]/dl/dt/a')
ff.click()


res1 = driver.page_source
soup1 = BeautifulSoup(res1, "html.parser")

fav_title = soup1.select_one('#content > div.article > div.mv_info_area > div.mv_info > h3 > a:nth-child(1)').text
fav_dir = soup1.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4) p > a').text
print('제목:', fav_title, '감독:', fav_dir )

scroll = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]')
ActionChains(driver).move_to_element(scroll).perform()

res2 = driver.page_source
soup2 = BeautifulSoup(res2, "html.parser")

rate = soup2.select_one("#content > div.article > div.section_group.section_group_frst > div:nth-child(5) > div:nth-child(2) > div.score_area > div.netizen_score > div > div > em").text
coun = soup2.select_one('#content > div.article > div.section_group.section_group_frst > div:nth-child(5) > div:nth-child(2) > div.score_total > strong > em').text.strip()
print('평점:', rate, '개수: ', coun, '건')
writer.writerow([fav_title, fav_dir, rate, coun])
file.close()


