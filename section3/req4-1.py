import sys
import io
from bs4 import BeautifulSoup
import requests

#Rest : Post, Get, Put(Fetch), Delete
#post 데이터보내기
#get 가져오기
#put 업데이트하고 교체하는 성격
#fetch 약간 수정하는 느낌
#delete 지우기

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#로그인 유저 정보
LOGIN_INFO = {
    'user_id' : '아이디',
    'user_pw' : '비밀번호'
}

with requests.Session() as s:
    login_req = s.post('https://user.ruliweb.com/member/login_proc',data=LOGIN_INFO)
    #HTML 소스 확인
    #print('login_req', login_req.text) html딱 보자마자 알 수가 없다. 적당히 보고 html에 틀렸다는 이야기 없으면 맞을지도
    #Header 확인
    #print('headers', login_req.headers)
    if login_req.status_code == 200 and login_req.ok :
        post_one = s.get('http://market.ruliweb.com/read.htm?table=market_ps&num=4547098')
        post_one.raise_for_status() #예외처리
        soup = BeautifulSoup(post_one.text, 'html.parser') #bS가 이해할 수 있는 html로 바꾸거
        #print(soup.prettify()) 긁어서 메모장에 붙여놓고 맞는 글인지 확인
        article = soup.select_one("table:nth-of-type(3)").find_all('p') #글이 포함되어 있는 곳이 세번째 테이블인 것을 확인
        #print(article)
        for i in article:
            if i.string is not None:
                #DB insert , 엑셀로 저장, 텍스트 가공
                print(i.string)
