from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req
import urllib.parse as rep
import os # os 명령 사용가능 21번줄위해

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

opener = req.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)

base = "https://www.inflearn.com/"
quote = rep.quote_plus("")
url = base + quote
print(url)

res = req.urlopen(url)
savePath = "D:/Web-Crawling/Web-Crawling/imagedown" # escape 문자쓸때 \\ 두번써야 \ 랑 같음 윈도우에서는 / 게 써도 경로 가능
#imagedown 폴더는 지금 존재하지 않음 만드는 코드도 작성

try:
    if not  (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))

except OSError as e:
    if e.errno != errno.EEXIST: # errno 에러넘버
        print("폴더 만들기 실패")
        raise

soup = BeautifulSoup(res, 'html.parser')
#_sau_imageTab > div.photowall._photoGridWrapper > div.photo_grid._box > div:nth-child(1) > a.thumb._thumb > img -> 크롬에서 copyselector 이용해서 구한다음 수정

img_list = soup.select("section.stripe ul.grid > li")

for i, e in enumerate(img_list,1):
    with open(savePath+"text_"+str(i)+".txt","wt") as f:
        f.write(e.select_one("h4.block_title > a").string)
    fullFileName = os.path.join(savePath, savePath+'\imagedown'+str(i)+'.png') # jpg
    req.urlretrieve(e.select_one("img")['src'],fullFileName)



print('다운로드 완료')
