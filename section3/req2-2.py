import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#Response 상태 코드
s = requests.Session()
r = s.get('http://httpbin.org/get')
print(r.status_code)
print(r.ok)

#JSON 데이터 handling
#https://jsonplaceholder.typicode.com # 연습용 Json 데이터

#r = s.get('https://jsonplaceholder.typicode.com/albums')
#print(r.text) # JSON 형태로 주어짐

r = s.get('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)
print(r.json()) # JSON으로 컨버팅해줌
print(r.json().keys()) #JSON 을 key와 value 로 가져온다.
print(r.json().values())
print(r.encoding) # utf-8
print(r.content) # b'{\n  "userId": 1,\n  "id": 1,\n  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",\n  "body": "quia et suscipit\\nsuscipit recusandae consequuntur expedita et cum\\nreprehenderit molestiae ut ut quas totam\\nnostrum rerum est autem sunt rem eveniet architecto"\n}'
print(r.raw) #<urllib3.response.HTTPResponse object at 0x000001AF93B3E400>






s.close()
