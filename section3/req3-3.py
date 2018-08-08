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

payload1 = {'key1' : 'value1', 'key2': 'value2'} #dict
payload2 = (('key1', 'value1'), ('key2', 'value2')) #tuple
payload3 = {'some', 'nice'}

#r = requests.put('http://httpbin.org/put', data=payload1) # url만 봐도 뭘 하려는 지 알 수 있다.
#print(r.text)

r = requests.put('https://jsonplaceholder.typicode.com/posts/1',data=payload1)
'''
{
  "key2": "value2",
  "key1": "value1",
  "id": 1 # id 값을 발급해줌
}
'''
#print(r.text)

r = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)
