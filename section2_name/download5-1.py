from bs4 import BeautifulSoup
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding = 'utf-8')

html = """
<html><body>
    <ul>
        <li><a id="naver" href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
        <li><a href="https://www.google.com">google</a></li>
        <li><a href="https://www.tistory.com">tistory</a></li>
</body></html>
"""
#1번 패턴
soup = BeautifulSoup(html, 'html.parser')
test = soup.find('a', string="naver")
print(test.string)

#2번 패턴 id 값으로 가져오기
print(soup.find(id="naver").string)


#3번 패턴 정규표현식 사용
li = soup.find_all(href=re.compile(r"^https://"))
print('li',li)
#li [<a href="https://www.google.com">google</a>, <a href="https://www.tistory.com">tistory</a>]

for e in li:
    print(e.attrs['href'])

#https://www.google.com
#https://www.tistory.com

li = soup.find_all(href=re.compile(r"da"))
print('li',li)
#li [<a href="https://www.google.com">google</a>, <a href="https://www.tistory.com">tistory</a>]

for e in li:
    print(e.attrs['href'])

#https://www.google.com
#https://www.tistory.com
