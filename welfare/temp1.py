import sys
import io
from bs4 import BeautifulSoup
import requests
import urllib.request as req
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
import psycopg2

#한글 출력할 때 문제 없게
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#postgresql 연동
try:
    conn = psycopg2.connect("dbname='welfare'")
except:
    print("unable to connect")


cur = conn.cursor()
#cur.execute("DROP TABLE welfare")
cur.execute("CREATE TABLE IF NOT EXISTS welfare(\
                    ID INT PRIMARY KEY NOT NULL, \
                    TITLE          TEXT, \
                    MAIN_TEXT      TEXT,\
                    WHO            TEXT,\
                    WHAT           TEXT,\
                    STANDARD       TEXT,\
                    HOW            TEXT,\
                    LINK           TEXT)")
conn.commit()

#전역변수
#크롬 브라우저  CLI환경에서
chrome_options = Options()
chrome_options.add_argument("--headless") #CLI환경
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:/welfare/chromedriver") # chromedriver 위치
driver.set_page_load_timeout(10)

#--------함수들-----------
def main_crawling() :
    main_title = soup.select_one('#contents > div.bokjiDetailWrap > h4 > span')
    main_text = soup.select_one('#contents > div.bokjiDetailWrap > div')

    data[0] = main_title.get_text().strip()
    data[1] = main_text.get_text().strip()


def WHO():
    support_target = soup.select_one('#backup > div:nth-of-type(1) > div > ul > li:nth-of-type(1) > ul')
    if support_target is not None :
        data[2] = support_target.get_text().strip()
    else :
        data[2] = 'empty'

def WHAT():
    get_what = soup.select_one('#backup > div:nth-of-type(2) > div > ul > li > ul')
    if get_what is not None:
        data[3] = get_what.get_text().strip()
    else:
        data[3] = 'empty'

def STANDARD():
    selection_criteria = soup.select_one('#backup > div:nth-of-type(1) > div > ul > li:nth-of-type(2) > ul')
    if selection_criteria is not None:
        data[4] = selection_criteria.get_text().strip()
    else :
        data[4] = 'empty'

def HOW():
    how = soup.select_one('#backup > div:nth-of-type(3) > div > ul.bokjiContsIn > li.first > ul > li')
    if how is not None:
        data[5] = how.get_text().strip()
    else:
        data[5] = 'empty'

def if_not_valid_stop(url):
    main_title = soup.select_one('#contents > div.bokjiDetailWrap > h4 > span')
    if main_title is None:
        return True
    return False

def init(url):
    driver.get(url)
    driver.implicitly_wait(1);
    return driver.page_source

def str_replace(str):
    str = str.replace('\n','')
    str = str.replace('\t','')
    str = str.replace('  ','')
    return str


url_front = 'http://www.bokjiro.go.kr/welInfo/retrieveGvmtWelInfo.do?searchIntClId=04&searchCtgId=999&welInfSno='
#url_back = '&pageGb=1&domainName=&firstIndex=0&recordCountPerPage=10&cardListTypeCd=list&welSrvTypeCd=01&searchGb=01&searchWelInfNm=&pageUnit=10&key1=list&stsfCn='

"""
for i in range(1,1000) :
    print(i)
    url = url_front + str(i)
    soup = BeautifulSoup(init(url), 'html.parser')

    if if_not_valid_stop(url):
        print('not_valid')
        continue
    data = ["","","","","","",""]
    main_crawling()#제목, 메인텍스트
    WHO()#지원대상
    WHAT()#지원내용
    STANDARD() #선정기준
    HOW() #신청방법
    data[6] = url
    #for s in data:
    #    print(s)
    cur.execute("INSERT INTO welfare (ID, TITLE, MAIN_TEXT, WHO, WHAT, STANDARD, HOW, LINK) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(i, str_replace(data[0]),str_replace(data[1]),str_replace(data[2]),str_replace(data[3]),str_replace(data[4]),str_replace(data[5]),str_replace(data[6])))
"""
conn.commit()
cur.execute("SELECT * FROM welfare ORDER BY id ASC") #ASC == 오름차순
rows = cur.fetchall()
for row in rows:
    print('>> ', row)

cur.execute("COPY welfare TO 'D:/Web-Crawling/Web-Crawling/welfare/welfare_test7.csv' DELIMITER ',' CSV HEADER ENCODING 'utf8'")

conn.close()
driver.quit()



'''
참고한 사이트

selenium : https://hashcode.co.kr/questions/2039/beautifulsoup%EC%9C%BC%EB%A1%9C-%EC%9B%B9%ED%81%AC%EB%A1%A4%EB%A7%81-%ED%95%A0%EB%95%8C-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC-%EB%AA%BB-%EC%9D%BD%EC%96%B4%EC%98%A4%EB%8A%94%EA%B1%B4-%EC%96%B4%EB%96%BB%EA%B2%8C-%ED%95%B4%EA%B2%B0%ED%95%A0%EC%88%98%EC%9E%88%EC%9D%84%EA%B9%8C%EC%9A%94
geckodriver : http://blog.junshoong.net/python/selenium3-FireFox50-geckodriver-error-solve/
pycopg2 : https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
postgresql doc : https://www.tutorialspoint.com/postgresql/postgresql_create_database.htm
'''
