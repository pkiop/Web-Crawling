import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "https://dthumb-phinf.pstatic.net/?src=%22https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F3150_000_6%2F20140804170709450_F5AUOHQVL.jpg%2FS158_SKY_9392.jpg%3Ftype%3Dw690_fst_n%26wm%3DY%22&twidth=690&theight=458&opts=17"
htmlURL = "http://google.com"

savePath = "D:/section2_name/test1.jpg"
savePath2 = "D:/section2_name/index.html"

dw.urlretrieve(imgUrl, savePath)
dw.urlretrieve(htmlURL, savePath2)

print("다운로드 완료!")
