from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding = 'utf-8')

url = "http://finance.daum.net/"
req = req.urlopen(url).read()
soup = BeautifulSoup(req, "html.parser")

#print('soup', soup.prettify())

top = soup.select("ul#topMyListNo1 > li") # 35개 더보기로 누르고 나서 생기는 정보느 ㄴ가져올 수 없다. 지금
#print(top)

for i, z in enumerate(top, 1) : # 이 함수를 이용하면 인덱스 줄 수 있음  1은 시작인덱스
    print(i , ' : ', z.find("a").string, ' ', z.find("span").string) #z자체는 bs4.element.tag 상태인 인스턴스 거기에 하나밖에 없는 a태그를 이용해 가져오고 string 으로


#정보를 가져옴
