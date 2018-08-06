from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req
import urllib.parse as rep

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://finance.naver.com/sise/"
quote = rep.quote_plus("추천-강좌") # 유니코드로 바꿔주는 코드
url = base + quote
# 위와 같이 하면 한글 주소를 유니코드 주소로 바꿈
#지금 하는 실습은 필요없어서
url = "https://www.inflearn.com/"
req = req.urlopen(url).read()
soup = BeautifulSoup(req, "html.parser")

recommend = soup.select("section.stripe .block_title")
# #은 id .은 class
for e in recommend :
    print("reco : ", e.string)
