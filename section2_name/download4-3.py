#태그 선택자를 통해 가져오기

import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding = "utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding = "utf-8")

html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="https://www.google.com">google</a></li>
        <li><a href="https://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a") # 태그에 포함된 정보를 한번에 담는다.
print('links', type(links)) # links <class 'bs4.element.ResultSet'>

for a in links:
    #print('a',type(a),a)
    href = a.attrs['href'] #attrs의 리턴값은 dic타입 key 값은 속성
    txt = a.string
    print('txt >> ', txt, 'href >> ',href)

#txt >>  naver href >>  http://www.naver.com
#txt >>  daum href >>  http://www.daum.net
#txt >>  google href >>  https://www.google.com
#txt >>  tistory href >>  https://www.tistory.com

#두번째 가져오는 방법

b = soup.find_all("a", string="daum")
print('b', b)

c = soup.find("a")
print('c', c) # 가장 위에 것 가져온다.

d = soup.find_all("a", limit=3)
print('d', d)

e = soup.find_all(string=["naver","google"])
print('e', e)

#find 를 통해 태그를 통해 바로 데이터 추출 가능
#이것도 많이 사용하긴 한데 다음 예제 CSS 선택자를 더 많이 사용
