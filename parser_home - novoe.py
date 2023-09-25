import requests
from bs4 import BeautifulSoup as BS

page = 1

while True:
    if page == 6:
        break
    r = requests.get("https://www.eapteka.ru/goods/vitaminy_i_bad/?PAGEN_1=" + str(page))
    html = BS(r.content, 'lxml')
    items = html.select(".cc-item--title")
    print(items)
    if len(items):
        with open("apteka.txt", 'a', encoding="utf-8") as f:
            for i in items:
                f.write(i.text + "\n")
    else:
        break

    page += 1

