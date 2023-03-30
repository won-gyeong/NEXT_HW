#크롤링 selenium으로 했다가 잘못된 걸 뒤늦게 알아차린..


# # 영화랭킹 1-20위 가져오기 
# for i in range(2,12):
#     rank = driver.find_element(By.XPATH, f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a').text
#     print(rank)
#     time.sleep(1)

# for i in range(13,23):
#     rank = driver.find_element(By.XPATH, f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a').text
#     print(rank)
#     time.sleep(1)

# # 각 영화 클릭하고 개요, 감독, 평점 가져오기
# for i in range(2,12):
#     title = driver.find_element(By.XPATH, f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a')
#     title.click()
#     title1 = driver.find_element(By.XPATH, f'//*[@id="content"]/div[1]/div[2]/div[1]/h3/a[1]').text
#     outline = driver.find_element(By.XPATH, f'//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
#     director = driver.find_element(By.XPATH, f'//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
#     rate = driver.find_element(By.XPATH, f'//*[@id="actualPointPersentBasic"]/div/span').text
    
#     print('제목:', title1, '개요:', outline, '감독:', director, rate)
    
#     chartbtn = driver.find_element(By.XPATH, f'//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
#     chartbtn.click()
#     time.sleep(1)


# for i in range(13,23):
#     title = driver.find_element(By.XPATH, f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a')
#     title.click()
#     title1 = driver.find_element(By.XPATH, f'//*[@id="content"]/div[1]/div[2]/div[1]/h3/a[1]').text
#     outline = driver.find_element(By.XPATH, f'//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
#     director = driver.find_element(By.XPATH, f'//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
#     rate = driver.find_element(By.XPATH, f'//*[@id="actualPointPersentBasic"]/div/span').text
    
#     print('제목:', title1, '개요:', outline, '감독:', director, rate)
    
#     chartbtn = driver.find_element(By.XPATH, f'//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
#     chartbtn.click()
#     time.sleep(1)

# # 좋아하는 영화 검색하고 제목, 감독, 스크롤 내려서 평점과 리뷰 개수 가져오기
# search_box = driver.find_element(By.XPATH, '//*[@id="ipt_tx_srch"]')
# search_box.send_keys("Bolt")
# search_box.send_keys(Keys.ENTER)
# time.sleep(1)

# ff = driver.find_element(By.XPATH, '/html/body/div/div[4]/div/div/div/div/div[1]/ul[2]/li[1]/dl/dt/a')
# ff.click()
# time.sleep(1)

# fav_title = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/h3/a').text
# fav_dir = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]').text
# print('제목:', fav_title, '감독:', fav_dir )
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(1)