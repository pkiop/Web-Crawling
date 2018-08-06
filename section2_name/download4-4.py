# 앞으로 스크래핑 할 html 은 a태그를 가져온다고 하면 엄청나게 많은 것을
# 가져오게 된다. 그것 중에서 필요한 걸 가져오려면 코드가 길어진다.

# 그래서 CSS 선택자

import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding = "utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding = "utf-8")

html = """
<html><body>
<div id="main">
    <h1>강의목록</h1>
    <ul class="lecs">
        <li>Java 초고수 되기</li>
        <li>파이썬 기초 프로그래밍</li>
        <li>파이썬 머신러닝 프로그래밍</li>
        <li>안드로이드 블루투스 프로그래밍</li>
    </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
h1 = soup.select("div#main > h1") # 선택자 사용
print('h1', h1) # h1 [<h1>강의목록</h1>]

for z in h1:
    print(z.string)

# h1이 list 타입이라 포문 사용해서 꺼내야함 번거로움

h1_1 = soup.select_one("div#main > h1")
#print('h1_1',type(h1_1)) #h1_1 <class 'bs4.element.Tag'>
print('h1_1', h1_1.string)

# 더 깔끔

#ul 태그의 list 다 가져오기

list_li = soup.select("div#main > ul.lecs > li")
for li in list_li:
    print("li >>> ", li.string)

#id 값은 지금 하나밖에 없으므로 이렇게 암시적으로 해도 된다.
list_li = soup.select("#main > .lecs > li")
for li in list_li:
    print("li >>> ", li.string)

#CSS 선택자의 장점. CSS로 한번 짠 코드는 다시 수정하려면 엄청나게 큰 일이 된다.
#일일이 다 손으로 고쳐야 하기 때문 그래서 잘 수정이 안되니까 CSS 선택자를 쓰면 수정되어서 생기는 문제는 왠만하면 없다 .
