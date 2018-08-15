import pymysql

#MySQL Connection
conn = pymysql.connect(host='localhost', user='python', password='1111!',
                        db='python_app1', charset='utf8')

try:
    with conn.cursor() as c: #conn.cursor(pymysql.cursors.DictCursor) #dict형태로 받고 싶으면
        #데이터 수정1
        c.execute("UPDATE users SET username = %s WHERE id = %s",('niceman',1))
        #데이터 수정2
        c.execute("UPDATE users SET username = '%s' WHERE id = '%d'" % ('goodboy',2))
        #insert 문 검색ㅎ새ㅓ 
        #c.execute("INSERT INTO users SET VALUES ('urbest',11)")
        #중간 데이터 확인
        c.execute("SELECT * FROM users ORDER BY id DESC")
        for row in c.fetchall():
            print('check1 > ', row)

        #데이터 삭제1
        c.execute("DELETE FROM users WHERE id = %s" ,(1,)) #1번 데이터를 지우겠다. where 안쓰면 데이터 다 날라가니까 주의

        #데이터 삭제1
        c.execute("DELETE FROM users WHERE id = '%s'" %(2,))
        c.execute("SELECT * FROM users ORDER BY id DESC")
        for row in c.fetchall():
            print('check2 > ', row)
    conn.commit()
finally:
    conn.close()
