import sys
import io
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#get 방식으로 받아온다.
# my ip api 를 구글에 검색
# ipify 의 주소 가져온다.

API = "https://api.ipify.org"

values = {
    'format' : 'json'
}
print('before', values)
params = urlencode(values)
print('after', params)

url = API + "?" + params
print("요청 url", url)
#API 사이트에 있는 형식과 맞아진 것 확인

reqData = req.urlopen(url).read().decode('utf-8')
print("출력", reqData)
