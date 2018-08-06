from urllib.parse import urljoin

baseUrl = "http://test,com/html/a.html" # 파일이 있다고 가정
print(">>", urljoin(baseUrl, "b.html"))
#출력 결과 http://test,com/html/b.html 이렇게 치환해준다.
print(">>", urljoin(baseUrl, "sub/b.html"))
# http://test,com/html/sub/b.html
#d여기까지 절대경로
print(">>", urljoin(baseUrl, "../index.html"))
print(">>", urljoin(baseUrl, "../img/img.jpg"))
print(">>", urljoin(baseUrl, "../css/img.css"))
#>> http://test,com/index.html
#>> http://test,com/img/img.jpg
#>> http://test,com/css/img.css
#여기까지 상대경로
