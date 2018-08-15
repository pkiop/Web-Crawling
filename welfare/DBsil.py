import pymysql
import simplejson as json
import datetime

#MySQL Connection
conn = pymysql.connect(host='localhost', user='python', password='1111!',
                        db='python_app1', charset='utf8')

#pyMysql 버전 확인
print('pymysql.version', pymysql.__version__)

#데이터베이스 선택
#이미 위에서 선택되었기 때문에 주석. 중간에 바꾸고 싶으면 이방법
#conn.select_db('python_app1') #첫 공백에 db이름

#Cursor 연결
c = conn.cursor()
#print(type(c)) <class 'pymysql.cursors.Cursor'>

#데이터베이스 생성
#c.execute('create database python_app2') #권한 있는 유저는 이렇게 db 생성 가능 #DDL. DML. DCL 언어 다 활용 가능

#커서 반환
#c.close() #resource 낭비 방지

#접속 해제
#conn.close()

#트랜잭션 시작 선언 rollback 하면 선언한 상황으로 돌아갈 수 있다 .
#conn.begin()

#커밋
#conn.commit()

#롤백
#conn.rollback()

#날짜 생성
now = datetime.datetime.now()
nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')#시간형식으로 바꿔주는 함수
print('nowDateTime',nowDateTime)

c.execute("CREATE TABLE IF NOT EXISTS users(id bigint(20) NOT NULL, \
                    username varchar(20), \
                    email varchar(30),\
                    phone varchar(30),\
                    website varchar(30),\
                    regdate varchar(20) NOT NULL, PRIMARY KEY(id))")
#2번 방법
"""
sql = """
"CREATE TABLE IF NOT EXISTS users(id bigint(20) NOT NULL, \
                    username varchar(20), \
                    email varchar(30),\
                    phone varchar(30),\
                    website varchar(30),\
                    regdate varchar(20) NOT NULL, PRIMARY KEY(id))"
"""
c.execute(sql)

#이런 방법도 가능하다
"""
#if not 을 해줘야 반복적으로 코드 실행할 때 에러 없다 .
# AUTO_INCREMENT 자동으로 증가하면서 , DEFAULT 'TEST' 이걸 추가하면 데이터 값 안들어오면 알아서 TEST 로 초기화

#위에서 curser 를 가져올 수 있지만 한번에 try 문으로 처리할 수도 있다.
try:
    with conn.cursor() as c:
        #JSON to MySQL
        with open("D:/Web-Crawling/Web-Crawling/section5/data/users.json", 'r') as infile:
            r = json.load(infile)
            userData = []
            for user in r:
                t = (user['id'], user['username'],user['email'], user['phone'], user['website'], nowDateTime)
                #c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (%s, %s, %s, %s, %s, %s)",(user['id'], user['username'],user['email'], user['phone'], user['website'], nowDateTime) ) #many 쓰기 싫으면 이렇ㄱ ㅔ하나하나 넣을 수 도 있다.
                userData.append(t);
            c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (%s, %s, %s, %s, %s, %s)", userData) #여기서 %는 Mysql에서 의 의미
            #c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (%s, %s, %s, %s, %s, %s)", tuple(userData)) # 명시적으로 tuple 선언해줘도 된다.
        conn.commit()
finally: #try문이 끝나면 반드시 한번 실행
    conn.close()
