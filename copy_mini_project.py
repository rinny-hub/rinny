import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

url_1 = "https://www.11st.co.kr/products/8485979166?&trTypeCd=05&trCtgrNo=585021&checkCtlgPrd=true"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

response = requests.get(url_1)
stanley = BeautifulSoup(response.text, 'html.parser')

site_tag = stanley.find("a", href="https://www.11st.co.kr/main")
if site_tag:
    site = site_tag.get_text().strip()
else:
    site = "11번가"
# 헤더/메뉴 영역이 JS로 렌더링되기 때문에 Requests + BeautifulSoup으로는 안 뜸. 직접 지정해야함


name = stanley.find("h1", {"class": "title"}).text.strip()
price = stanley.find("span", {"class": "value"}).text.strip()
print("사이트:", site)
print("상품명:", name)
print("가격:", price)

dic = {"site": site, "name": name, "price": price}
print(dic)

# data = {"사이트": [site], "상품명": [name], "가격": [price]}
# df = pd.DataFrame(data)
# df.to_excel("stanley_11st.xlsx")
