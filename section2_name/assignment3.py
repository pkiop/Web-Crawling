import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = "utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = "utf-8")

url1 = "https://ssl.pstatic.net/tveta/libs/1198/1198832/092558ab24900f5d2fea_20180803165406066.jpg"
url2 = "https://ssl.pstatic.net/tveta/libs/1205/1205132/4e7f7f4dc0869473d576_20180802101157053.gif"

spath1 = "D:/section2_name/ad1.gif"
spath2 = "D:/section2_name/ad2.gif"

req.urlretrieve(url1, spath1)
req.urlretrieve(url2, spath2)
