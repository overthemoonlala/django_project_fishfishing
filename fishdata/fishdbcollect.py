
'''
1. 멸종위기종 웹 크롤링
Beatifulsoup- 20220701


'''
'''
url
"https://www.nie.re.kr/endangered_species/home/enspc/enspc06003v.do?species_sn=99",  #좀수수치
"https://www.nie.re.kr/endangered_species/home/enspc/enspc06003v.do?species_sn=100", #모래주사
"https://www.nie.re.kr/endangered_species/home/enspc/enspc06003v.do?species_sn=101", #퉁사리
"https://www.nie.re.kr/endangered_species/home/enspc/enspc06003v.do?species_sn=102" #입실납자루
"https://www.nie.re.kr/endangered_species/home/enspc/enspc06003v.do?species_sn=108" #돌상어
'''


# ▶ 멸종위기종 크롤링
import urllib.request as req
from bs4 import BeautifulSoup

base_url= "https://www.nie.re.kr/endangered_species/home/enspc/enspc06003v.do?species_sn={}"

idurl=[99, 100, 101, 102, 108]
name = []     #어류종
reason = []   #멸종원인
shape = []    #형태
ecology = []  #생태
place = []    #서식지

for i in idurl:
    url = base_url.format(i)
    res = req.urlopen(url)
    print(url)
    soup = BeautifulSoup(res, 'html.parser')
    names = soup.select_one('#container > div.layout > div.jongview > div.jonginfo > h3').get_text() #어류종
    reasons = soup.select_one("#container > div.layout > div:nth-child(22) > div > p").get_text() #멸종원인
    shapes = soup.select_one("#container > div.layout > p:nth-child(14)").get_text() #형태
    ecologies = soup.select_one("#container > div.layout > ul > li:nth-child(1)").get_text() #생태
    places = soup.select_one("#container > div.layout > div:nth-child(18) > div:nth-child(1) > p").get_text() #서식지
    name.append(names)
    reason.append(reasons)
    shape.append(shapes)
    ecology.append(ecologies)
    place.append(places)

    
print(name)    #전처리 필요x
print(reason)  #전처리 필요o => 앞,뒤 공백 및 문자열 제거
print(shape)   #전처리 필요o => 앞,뒤 공백 및 문자열 제거
print(ecology) #전처리 필요o => 뒷 공백 제거
print(place)   #전처리 필요o => 앞,뒤 공백 및 문자열 제거



# ▶ 데이터 전처리

for i in range(5):
    reason[i]=reason[i].strip("'\r\n             ")
    reason[i]=reason[i].strip("  \r\n          \t\r\n\t\t\t")
    shape[i]=shape[i].strip("'\r\n          ")
    shape[i]=shape[i].strip("  \r\n          \r\n")
    ecology[i]=ecology[i].rstrip()
    place[i]=place[i].strip("\r\n             ")
    place[i]=place[i].strip(" \r\n             \r\n              \r\n          \t\r\n\t\t\t")

    

print(reason)
print(shape)
print(ecology)
print(place)



#▶ 데이터프레임 변환 후 엑셀 저장

import pandas as pd
import openpyxl

extinct_fish = pd.DataFrame(zip(name, reason, shape, ecology, place),\
                            columns=['name', 'reason', 'shape', 'ecology', 'place'])
extinct_fish

extinct_fish.to_excel("data/멸종위기어류.xlsx")
extinct_fish = pd.read_excel("data/멸종위기어류.xlsx")
extinct_fish



################################################################################
'''
2. 독성어류 크롤링

url
"https://www.nifs.go.kr/frcenter/species/?_p=species_view&mf_tax_id=MF0004344" #독가시치
"https://www.nifs.go.kr/frcenter/species/?_p=species_view&mf_tax_id=MF0004119" #미역치
"https://www.nifs.go.kr/frcenter/species/?_p=species_view&mf_tax_id=MF0009212"#쏨뱅이
"https://www.nifs.go.kr/frcenter/species/?_p=species_view&mf_tax_id=MF0003032"#쏠종개
"https://www.nifs.go.kr/frcenter/species/?_p=species_view&mf_tax_id=MF0008694"#쑤기미
'''

from bs4 import BeautifulSoup
import urllib.request as req

base_url = "https://www.nifs.go.kr/frcenter/species/?_p=species_view&mf_tax_id={}"
base_url

idurl = ["MF0004344", "MF0004119", "MF0009212", "MF0003032", "MF0008694"]
name=[]     #어류종
shape=[]    #형태
ecology=[]  #생태
place=[]    #분포
eat=[]      #먹이



for i in idurl:
    url = base_url.format(i)
    res = req.urlopen(url)
    soup = BeautifulSoup(res, 'html.parser')
    print(url) #url연결확인
    
    names = soup.select_one("#contents > div:nth-child(2) > div.subCon > table > tbody > tr:nth-child(1) > td:nth-child(2)").get_text()
    shapes = soup.select_one("#contents > div:nth-child(3) > table:nth-child(4) > tbody > tr:nth-child(4) > td").get_text()      #형태
    ecologies = soup.select_one("#contents > div:nth-child(3) > table:nth-child(4) > tbody > tr:nth-child(3) > td").get_text()  #생태
    places = soup.select_one("#contents > div:nth-child(3) > table:nth-child(4) > tbody > tr:nth-child(2) > td").get_text()    #분포
    eats = soup.select_one("#contents > div:nth-child(3) > table:nth-child(4) > tbody > tr:nth-child(7) > td").get_text()       #먹이

    name.append(names) #어류종
    shape.append(shapes) #형태
    ecology.append(ecologies) #생태
    place.append(places) #분포
    eat.append(eats) #먹이
    
    
    
print(name)
print(shape)
print(ecology)
print(place)
print(eat)


'''
확인용
'''

from bs4 import BeautifulSoup
import urllib.request as req



url = "https://www.nifs.go.kr/frcenter/species/?_p=species_view&mf_tax_id=MF0008694"
res = req.urlopen(url) #인터넷을 통해 url에 연결
print(res) #url을 통해서 연결된 응답 데이터
soup = BeautifulSoup(res,'html.parser')
names = soup.select_one("#contents > div:nth-child(2) > div.subCon > table > tbody > tr:nth-child(1) > td:nth-child(2)").get_text()
shape = soup.select_one("#contents > div:nth-child(3) > table:nth-child(4) > tbody > tr:nth-child(4) > td").get_text()
ecology = soup.select_one("#contents > div:nth-child(3) > table:nth-child(4) > tbody > tr:nth-child(3) > td").get_text()  #생태
place = soup.select_one("#contents > div:nth-child(3) > table:nth-child(4) > tbody > tr:nth-child(2) > td").get_text()    #분포
eat = soup.select_one("#contents > div:nth-child(3) > table:nth-child(4) > tbody > tr:nth-child(7) > td").get_text()       #먹이

print(name)
print(shape)
print(ecology)
print(place)
print(eat)



#▶ 데이터 프레임으로 변환 후 엑셀화
import pandas as pd
import openpyxl

toxic = pd.DataFrame(zip(name, shape, ecology, place, eat),\
                     columns=['name', 'shape', 'ecology', 'place' ,'eat'])
    
toxic = toxic.to_excel("data/독성어류.xlsx")
toxic = pd.read_excel("data/독성어류.xlsx")
toxic
###############################################################################
