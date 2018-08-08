import sys
import io
from bs4 import BeautifulSoup
import requests
import urllib.request as req
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json

#한글 출력할 때 문제 없게
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#전역변수
#크롬 브라우저  CLI환경에서
chrome_options = Options()
chrome_options.add_argument("--headless") #CLI환경
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:/welfare/chromedriver") # geckodriver 위치

#--------함수들-----------
def main_crawling() :
    main_title = soup.select_one('#contents > div.bokjiDetailWrap > h4 > span')
    main_text = soup.select_one('#contents > div.bokjiDetailWrap > div')
    ret = ''
    print('제목 : ', main_title.get_text().strip())
    print()
    print('핵심내용 : ', main_text.get_text().strip())
    print()

def support_target_crawling():
    support_target = soup.select_one('#backup > div:nth-of-type(1) > div > ul > li:nth-of-type(1) > ul')
    if support_target is not None :
        print('지원대상 : ', support_target.get_text().strip())
    else :
        print('지원대상 항목 없음')
    print()

def selection_criteria_crawling():
    #선정기준
    selection_criteria = soup.select_one('#backup > div:nth-of-type(1) > div > ul > li:nth-of-type(2) > ul')
    if selection_criteria is not None:
        print('선정기준 : ', selection_criteria.get_text().strip())
    else :
        print('선정기준 항목 없음')

def if_not_valid_stop(url):
    main_title = soup.select_one('#contents > div.bokjiDetailWrap > h4 > span')
    if main_title is None:
        return True
    return False

def init(url):
    driver.implicitly_wait(3)
    driver.get(url)
    driver.implicitly_wait(3)
    return driver.page_source



url_front = 'http://www.bokjiro.go.kr/welInfo/retrieveGvmtWelInfo.do?searchIntClId=04&searchCtgId=999&welInfSno='
url_back = '&pageGb=1&domainName=&firstIndex=0&recordCountPerPage=10&cardListTypeCd=list&welSrvTypeCd=01&searchGb=01&searchWelInfNm=&pageUnit=10&key1=list&stsfCn='

if __name__ == '__main__' :
    for i in range(1,350) :
        url = url_front + str(i) + url_back
        soup = BeautifulSoup(init(url), 'html.parser')

        if if_not_valid_stop(url):
            print('not_valid')
            continue
        j1 = {' ' , ' '}
        j2 = {' ' , ' '}
        j3 = {' ' , ' '}
        main_crawling()
        support_target_crawling()
        selection_criteria_crawling()

driver.quit()



'''
참고한 사이트

selenium : https://hashcode.co.kr/questions/2039/beautifulsoup%EC%9C%BC%EB%A1%9C-%EC%9B%B9%ED%81%AC%EB%A1%A4%EB%A7%81-%ED%95%A0%EB%95%8C-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC-%EB%AA%BB-%EC%9D%BD%EC%96%B4%EC%98%A4%EB%8A%94%EA%B1%B4-%EC%96%B4%EB%96%BB%EA%B2%8C-%ED%95%B4%EA%B2%B0%ED%95%A0%EC%88%98%EC%9E%88%EC%9D%84%EA%B9%8C%EC%9A%94
geckodriver : http://blog.junshoong.net/python/selenium3-FireFox50-geckodriver-error-solve/
'''
