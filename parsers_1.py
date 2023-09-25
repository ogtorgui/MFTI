import requests
from bs4 import BeautifulSoup as BS

page = 1

while True:
    if page == 3:
        break
    r = requests.get("https://stopgame.ru/topgames?p=" + str(page))
    html = BS(r.content, 'lxml') # или html.parser\ pip install lxml
    items = html.select(".item > .details > .row > .caption > a")
    if len(items):
        print(page)
        with open("1.txt", 'a', encoding="utf-8") as f:
            for i in items:
                f.write(i.text)
    else:
        break

    page += 1

