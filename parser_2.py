from bs4 import BeautifulSoup as BS
import requests

rq = requests.get("https://stopgame.ru/topgames?p=")

soup = BS(rq.content, "lxml")

s = soup.find_all('div', {'class': "caption caption-bold"})

for i in s:
    print(i.find('a').text)

