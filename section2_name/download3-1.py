import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.encar.com/index.do?firstFg=Y&WT.hit=index_mobile_1st"

mem = req.urlopen(url)

#print(type(mem))
#print(type({}))
#print(type([]))
#print(type(()))

#print("geturl", mem.geturl())
#print("status", mem.status) #200 정상 , 404 페이지 없음, 403 거절, 500 서버 자체의 에러
#print("headers", mem.getheaders())
#print("info", mem.info())
#print("code", mem.getcode()) # status 랑 같다
#print("read", mem.read()) # read안에 숫자를 넣으면 숫자 만큼의 데이터만 가져온다.
#print("read", mem.read(50).decode("utf-8")) #decode 붙이는 게 정석

print(urlparse(url))
