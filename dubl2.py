from bs4 import BeautifulSoup as BS
import requests

rq = requests.get("https://www.eapteka.ru/goods/vitaminy_i_bad/?PAGEN_1=2")

soup = BS(rq.content, "lxml")

s = soup.find_all('a', {'class': "cc-item--title"})

for i in s:
    print(i.text)