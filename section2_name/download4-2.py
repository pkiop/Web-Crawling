import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding = "utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding = "utf-8")

#쌍따옴표 3개 => 줄바꿈이 포함된 스트링
html = """
<html>
    <body>
        <h1>파이썬 BeautifulSoup 공부</h1>
        <p>태그 선택자</p>
        <p>CSS 선택자</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser') # 명시적으로 parser 지정
#print('soup', type(soup)) #soup <class 'bs4.BeautifulSoup'>
#print('prettyfy', soup.prettify()) #자동 들여쓰기 해준다.


# h1 과 p 는 형제임 . 그래서 들여쓰기할때 같은 띄움 body 가 부모
h1 = soup.html.body.h1
print('h1', type(h1)) # h1 <class 'bs4.element.Tag'>
print(h1.string) # 파이썬 BeautifulSoup 공부

#p가 2개인데 뭘 가져오나
p1 = soup.html.body.p
print('p1',p1) #p1 <p>태그 선택자</p> 첫번째 p 를 가져옴

p2 = p1.next_sibling.next_sibling # 두번하는 이유. enter로 줄바꿈이 되어 있어서 그걸 처리하기 위해
print('p2',p2)

p3 = p1.previous_sibling.previous_sibling # 한번 앞으로 가면 </h1> 으로 한번 더해야 <h1>
print('p3',p3)

print("h1 >> ", h1.string)
print("h2 >> ", p1.string)
print("h3 >> ", p2.string)
