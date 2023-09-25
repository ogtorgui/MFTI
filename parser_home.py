import requests
from bs4 import BeautifulSoup as BS

page = 1

while True:
    if page == 4:
        break
    r = requests.get("https://www.igromania.ru/games/all/all/all/all/all/0/" + str(page) + "/")
    html = BS(r.content, 'lxml')
    items = html.select(".game-card > .top-block > .left-block > a")
    if len(items):
        with open("parser_home.txt", 'a', encoding="utf-8") as f:
            for i in items:
                f.write(i.text + "\n")
    else:
        break

    page += 1

