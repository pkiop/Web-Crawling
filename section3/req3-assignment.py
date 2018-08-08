import sys
import io
import requests, json

#Rest : Post, Get, Put(Fetch), Delete
#post 데이터보내기
#get 가져오기
#put 업데이트하고 교체하는 성격
#fetch 약간 수정하는 느낌
#delete 지우기

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

r = requests.get('https://developers.skplanetx.com/apidoc/kor/melon/current-musical/')
print(r.text)
