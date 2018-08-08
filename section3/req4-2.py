import sys
import io
from bs4 import BeautifulSoup
import requests
import urllib.parse as rep

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
"lsd" : "AVo6FMn8",
"api_key" : "1101702136522636",
"cancel_url": "https://www.inflearn.com/wp-content/plugins/wordpress-social-login/hybridauth/?hauth_done=Facebook&error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=da069011cd0f65966b8cb008a1182872#_=_",
"display": "page",

"legacy_return": "0",

"skip_api_login": "1",
"signed_next": "1",
"trynum": "1",
"timezone": "-540",
"lgndim": "eyJ3IjoyMDQ4LCJoIjoxMTUyLCJhdyI6MjA0OCwiYWgiOjExNTIsImMiOjI0fQ==",
"lgnrnd": "212655_XiX7",
"lgnjs": "1533702419",
"email": "+821024421601",
"pass": "warcare1!!",
"prefill_contact_point": "+821024421601",
"prefill_source": "browser_dropdown",
"prefill_type": "password",
"first_prefill_source": "browser_dropdown",
"first_prefill_type": "contact_point",
"had_cp_prefilled": "true",
"had_password_prefilled": "true"
}

with requests.Session() as s:
    login_req = s.post('https://www.facebook.com/login.php?login_attempt=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.8%2Fdialog%2Foauth%3Fredirect_uri%3Dhttps%253A%252F%252Fwww.inflearn.com%252Fwp-content%252Fplugins%252Fwordpress-social-login%252Fhybridauth%252F%253Fhauth_done%253DFacebook%26state%3Dda069011cd0f65966b8cb008a1182872%26scope%3Demail%252Cpublic_profile%252Cuser_friends%26response_type%3Dcode%26auth_type%3Drerequest%26client_id%3D1101702136522636%26ret%3Dlogin%26sdk%3Dphp-sdk-5.4.4%26logger_id%3Dcbb5d605-4ffb-512a-d7ed-119e594fa874&lwv=100',data=LOGIN_INFO)
    #HTML 소스 확인
    print('login_req', login_req.text) #html딱 보자마자 알 수가 없다. 적당히 보고 html에 틀렸다는 이야기 없으면 맞을지도
    #Header 확인
    #print('headers', login_req.headers)
    '''
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
                '''
