import sys
import io
from bs4 import BeautifulSoup
import requests
import urllib.request as req
import selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://cu.bgfretail.com/product/product.do?category=product&depth2=4&sf=N')

html = driver.page_source
soup = BeautifulSoup(html)
prodList = soup.find_all("p", {"class": "prodPrice"})
print(len(prodList))
#한글 출력할 때 문제 없게
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#여러줄로 나뉜 string 을 한 줄로
def only_string(temp_text) :
    ret_text = ''
    for e in temp_text.childGenerator() :
        if e.string is not None :
            ret_text += e.string
    return ret_text.strip() #문장 맨 앞뒤 whitespace 제거

url = 'http://www.bokjiro.go.kr/welInfo/retrieveGvmtWelInfo.do?searchIntClId=04&searchCtgId=999&welInfSno=253&pageGb=1&domainName=&firstIndex=0&recordCountPerPage=10&cardListTypeCd=list&welSrvTypeCd=01&searchGb=01&searchWelInfNm=&pageUnit=10&key1=list&stsfCn='
req = req.urlopen(url).read()
#print(req)
soup = BeautifulSoup(req, 'html.parser')
print(soup.prettify())
#print('------------text-------------')

#가장 위에 있는 제목

main_title = soup.select_one('#contents > div.bokjiDetailWrap > h4 > span')
print(main_title.string)
main_text_temp = soup.select_one('#contents > div.bokjiDetailWrap > div')
main_text = only_string(main_text_temp)

#print(main_text)
#지원 대상
#backup > div:nth-child(1) > div > ul > li.first > ul > li
#backup > div:nth-child(1) > div > ul > li.first > ul > li
#backup > div:nth-child(1)
#backup > div:nth-child(1) > div > ul > li > ul > li
temp = soup.findAll('div', style="position: relative;")
print(temp)
support_target_temp = soup.select_one('div#backup')
print(support_target_temp)

#support_target = only_string(support_target_temp)
#print(support_target)
#선정기준

#selection_criteria = soup.select('#backup')
#print(selection_criteria)
