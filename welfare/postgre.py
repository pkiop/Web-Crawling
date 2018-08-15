import psycopg2

try:
    conn = psycopg2.connect("dbname='welfare'")
except:
    print("unable to connect")


cur = conn.cursor()

#cur.execute("CREATE TABLE IF NOT EXISTS welfare(ID INT NOT NULL AUTO_INCREMENT, \
cur.execute("CREATE TABLE welfare(ID INT PRIMARY KEY NOT NULL, \
                    TITLE          TEXT, \
                    MAIN_TEXT      TEXT,\
                    WHO            TEXT,\
                    WHAT           TEXT,\
                    HOW            TEXT,\
                    LINK           TEXT)")
conn.commit()

print("do")

#CREATE USER pkiop superuser 로 user 등록
