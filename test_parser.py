import re  # для упрощения поиска по тексту

from bs4 import BeautifulSoup as BS  # подключение библиотека для парсинга

with open("parser_test.html", 'r', encoding='utf-8') as f:  # получаем наш сайт
    src = f.read()

soup = BS(src, "lxml")  # парсим сайт с помощью lxml

# --------------------------------------------

print(soup.title.text.strip())
print(soup.find('h1'))
print(soup.find('div', class_="description").find('div'))
print(soup.find('div', {"class": "description"}).find('div'))

# --------------------------------------------

for i in soup.find_all('a'):
    print(i)

# --------------------------------------------

# find_parent(), find_parents - найти родителя\родителей элемента
# .next_element, .previous_element - следующий и предыдущий элемент
# .find_next_sibling(), .find_previous_sibling() - поиск следующего элемента внутри того же блока

# --------------------------------------------

print(soup.find('div', {'data-attr': "tor"}).get('class')[0])  # Получение значения аттрибутов

print(soup.find('div', {'data-attr': "tor"})['class'][0])

# --------------------------------------------

print(soup.find('p', text="С его помощью можно в считанные секунды найти нужную информациб на сайте"))
print(soup.find('p', text=re.compile("С его помощью")))  # Поиск по тексту
print(soup.find_all(text=re.compile("([Пп]арсинг)")))

# --------------------------------------------

import requests

header = {  # Показываем сайту что мы не бот
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
}

req = requests.get("https://stopgame.ru/topgames?p=1", headers=header)

with open("index.html", 'w', encoding='utf-8') as f:  # Сохраняем сайт, чтобы не было лишних вопросов со стороны сайта
    f.write(req.text)
