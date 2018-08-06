from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding = 'utf-8')

fp = open("food-list.html" ,encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

#양주를 가져오는 것이 목표
print("1", soup.select_one("li:nth-of-type(8)").string) # 조건에 맞는 한개의 스트랑 엘리먼트로 바로 가져올 수 있음
print("2", soup.select_one("#ac-list > li:nth-of-type(4)").string) # > 가 있으면 자식 선택자 이게 없으면 자손 선택자
print("3", soup.select("#ac-list > li[data-lo='cn']")[0].string) #select 는 list형태로 return
print("4", soup.select("#ac-list > li.alcohol.high")[0].string) # CSS 문법은 띄어쓰기 허용. 하지만 여기선 허용안하므로 띄어쓰기는 . 으로 구분

param = {"data-lo" : "cn" ,"class" : "alcohol"}
print("5", soup.find("li", param).string) # param 같이 정보가 있을때 효율적으로 접근
print("6", soup.find(id="ac-list").find("li",param).string) # 매우 명시적 접근

for ac in soup.find_all("li") :
    if ac['data-lo'] == 'us' :
        print('data-lo == us', ac.string)
