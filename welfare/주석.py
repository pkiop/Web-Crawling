import sys
import io
from bs4 import BeautifulSoup
import requests
import urllib.request as req
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


#한글 출력할 때 문제 없게
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#크롬 브라우저  CLI환경에서
chrome_options = Options()
chrome_options.add_argument("--headless") #CLI환경
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:/welfare/chromedriver") # geckodriver 위치
soup = BeautifulSoup('', 'html.parser')



#--------함수들-----------

#앞뒤 공백, 태그 제거
'''
def only_string(temp_text) :
    ret_text = ''
    for e in temp_text.childGenerator() :
        #print('e : ', e, 'e.get_text : ', e.get_text())
        if e.string is not None :
            ret_text += e.string
        else :
            print('printed : ', repr(e.strings))
    return ret_text.strip() #문장 맨 앞뒤 whitespace 제거
'''
def main_crawling() :
    main_title = soup.select_one('#contents > div.bokjiDetailWrap > h4 > span')
    #print(main_title.string)
    main_text = soup.select_one('#contents > div.bokjiDetailWrap > div')
    print('제목 : ', main_title.get_text().strip())
    print()
    print('핵심내용 : ', main_text.get_text().strip())
    #main_text = only_string(main_text_temp)
    #print(main_text)
    print()

def support_target_crawling():
    #지원 대상
    #print(temp)
    support_target = soup.select_one('#backup > div:nth-of-type(1) > div > ul > li:nth-of-type(1) > ul')
    if support_target is not None :
        print('지원대상 : ', support_target.get_text().strip())
    else :
        print('지원대상 항목 없음')
    #print(support_target_temp)
    #print(support_target_temp)
    #print(type(support_target_temp))
    #support_target = only_string(support_target_temp)
    #print('지원 대상 : ', support_target)
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
    #a = req.urlopen(url)
    #print(a.getcode())
    #if a.getcode() == 404:
    #    return True
    #return False
    #print(selection_criteria_temp)
    #print(type(selection_criteria_temp))

    #selection_criteria = only_string(selection_criteria_temp)
    #print('선정기준 : ')
    #print(selection_criteria)
    #selection_criteria_temp = soup.select_one('#backup > div:nth-of-type(1) > div > ul > li:nth-of-type(2) > ul > li > ul')
    #print(selection_criteria_temp.get_text())

def init(url):
    driver.implicitly_wait(3)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

url_front = 'http://www.bokjiro.go.kr/welInfo/retrieveGvmtWelInfo.do?searchIntClId=04&searchCtgId=999&welInfSno='
url_back = '&pageGb=1&domainName=&firstIndex=0&recordCountPerPage=10&cardListTypeCd=list&welSrvTypeCd=01&searchGb=01&searchWelInfNm=&pageUnit=10&key1=list&stsfCn='


if __name__ == '__main__' :
    for i in range(1,30) :
        url = url_front + str(i) + url_back
        init(url)

        if if_not_valid_stop(url):
            print('not_valid')
            continue

        main_crawling()
        support_target_crawling()
        selection_criteria_crawling()

driver.quit()




#driver.save_screenshot("D:/welfare/temp1_nobrowser.png")# test



#invalid_tags = ['<br/>']
#for tag in invalid_tags:
#    for match in soup.findAll(tag):
#        match.replaceWithChildren()


#가장 위에 있는 제목

#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------

#



























'''
참고한 사이트

selenium : https://hashcode.co.kr/questions/2039/beautifulsoup%EC%9C%BC%EB%A1%9C-%EC%9B%B9%ED%81%AC%EB%A1%A4%EB%A7%81-%ED%95%A0%EB%95%8C-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC-%EB%AA%BB-%EC%9D%BD%EC%96%B4%EC%98%A4%EB%8A%94%EA%B1%B4-%EC%96%B4%EB%96%BB%EA%B2%8C-%ED%95%B4%EA%B2%B0%ED%95%A0%EC%88%98%EC%9E%88%EC%9D%84%EA%B9%8C%EC%9A%94
geckodriver : http://blog.junshoong.net/python/selenium3-FireFox50-geckodriver-error-solve/
'''
