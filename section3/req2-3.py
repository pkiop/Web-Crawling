import sys
import io
import requests, json # json import 하면 json.loads 사용가능

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

s = requests.Session()

r = s.get('http://httpbin.org/stream/20', stream = True)
print(r.text)
#print(r.json()) JSON 같아서 파싱했는데 안된다. JSON으로 변환해야함
print(r.encoding) #인코딩 확인해보니 None 으로 되어있다. unicode 형태로 decode 해줘야 한글로 쓸 수 있다.

#인코딩 안되어있으면 utf-8로 하자

if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True): #줄바꿈이 문제여서 줄바꿈 처리 해줬다.
    #print(line)
    b = json.loads(line)
    #print(type(b)) # dict 가 나오면 정확히 json 으로 컨버팅 되었다.
    #print(b['origin'])
    for e in b.keys() :
        print('key', e, 'value', b[e])
