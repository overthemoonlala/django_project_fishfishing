'''
사진 크롤링
20220701
'''

###############################################################################
# ▶ 멸종위기어류 사진 크롤링


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request


# ▶ 1. 드라이브 열어서 url 가져오기
driver = webdriver.Chrome("c:/setup/chromedriver")
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl") #구글 이미지 검색



# ▶ 2. name 요소로 검색키 찾고 원하는 단어 입력 후 검색하기
elem = driver.find_element(By.NAME, "q") #구글 검색 find_element로 가져오기
elem.send_keys("수지") #원하는 값 입력
elem.send_keys(Keys.RETURN) #값 엔터
time.sleep(2) #2초간 웨이팅



# ▶ 3. 사진 저장하기
images = driver.find_elements(By.CSS_SELECTOR  , '.rg_i.Q4LuWd') #작은 이미지를 클릭
count = 300
#img_url=[]
try:
    for image in images:
        image.click()
        time.sleep(2)
        imgurl = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img").get_attribute("src")
        count = count + 1
        urllib.request.urlretrieve(imgurl, 'img/수지/'+ str(count) +'.jpg')
        if count == 50:
            driver.quit() #브라우저 닫기
except urllib.error.URLError:
    pass        
      
        
#####################################################################################################################################################
# ▶ 크롤링한 이미지 이름 변경하기       
import os      
        
# 디렉토리에 있는 항목들의 이름을 담고 있는 리스트를 반환
file_path = 'img/농어' # 파일경로
file_names = os.listdir(file_path)
file_names #파일이름확인

i = 0
for name in file_names:
    src = os.path.join(file_path, name)
    dst = str(i) + '.jpg'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1
      
