import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#r = requests.get('https://api.github.com/events')
#r = requests.get('https://api.github.com/events', cookies='') #이전시간 쿠키 전달하는 방법. 더 규격화된 방법 15번줄에서 시작

#r.raise_for_status() # 에러가 발생했을 때 예외를 발생시켜준다.
#print(r.text)


jar = requests.cookies.RequestsCookieJar()
jar.set('name','kim',domain='httpbin.org',path='/cookies') # 한번 지정해두면 jar 변수만 넣어서 쉽게 사용가능

'''
r = requests.get('http://httpbin.org/cookies',cookies=jar)
r.raise_for_status()
print(r.text)

r = requests.get('https://github.com',timeout=5) # 초단위. 5초동안 대기하면서 그안에 받겠다.
print(r.text)

r = requests.post('http://httpbin.org/post', data={'name' : 'kim'}, cookies=jar)
print(r.text)
'''

payload = {'key1' : 'value1', 'key2' : 'value2'}# 페이로드 데이터를 서버상에 request 할 때 담을 수 있는 것 API 할 때 페이로드라는 단어 많이 나옴
payload2 = (('key1','value1'), ('key2', 'value2')) # 위에것은 dict형태로 이거는 tuple 형태로

r = requests.post('http://httpbin.org/post', data=payload2)
print(r.text)

#json 데이터를 보낼수도

payload3 = {'some' : 'nice'}

r = requests.post('http://httpbin.org/post', data=json.dumps(payload3))
print(r.text)
