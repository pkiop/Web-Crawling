from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding = 'utf-8')

fp = open("cars.html" ,encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

#funtion 을 만들어 효율적으로
def car_func(selector):
    print("car_func", soup.select_one(selector).string)

car_func("#gr")
car_func("li#gr")
car_func("ul > li#gr")
car_func("#cars #gr")
car_func("#cars > #gr")
car_func("li[id='gr']")

print("car_func", soup.select("li")[3].string)
print("car_func", soup.find_all("li")[3].string)


car_lambda = lambda q : print("car_lamda", soup.select_one(q).string)

car_lambda("#gr")
car_lambda("li#gr")
car_lambda("ul > li#gr")
car_lambda("#cars #gr")
car_lambda("#cars > #gr")
car_lambda("li[id='gr']")
