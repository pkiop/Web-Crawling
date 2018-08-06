from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://finance.naver.com/sise/"
req = req.urlopen(url).read()
soup = BeautifulSoup(req, "html.parser")

top3 = soup.select("#siselist_tab_0 > tr")

i = 1
for e in top3 :
    if e.find("a") is not None:
        print(i, e.select_one(".tltle").string)
        i += 1
