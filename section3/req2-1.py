#python 3.0 이상부터는 urllib 보다 requests 모듈이 더 효율적

import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

s = requests.Session()
#r = s.get('https://www.naver.com')#PUT(FETCH), DELETE, GET, POST
#print('1',r.text)

#r = s.get('http://httpbin.org/cookies',cookies={'from' : 'myName'}) # 들어가보면 요청한 것을 반환해주는 연습 사이트
#print(r.text) #cookies 를 response해줌

url = 'http://httpbin.org/get'
headers = {'user-agent':'myPythonApp_1.0.0'}

#r = s.get(url, headers=headers)
#print(r.text)


s.close()

with requests.Session() as s:
    r = s.get('https://www.naver.com')
    print(r.text)
