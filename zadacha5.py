# 6
# Спарсить сайт
#
# https://coinmarketcap.com
#
# 1 Название валюты
# 2 Цена
# 3 Вывести все данные в телеграм бот

from bs4 import BeautifulSoup
import requests
from pprint import pprint as pp

URL = 'https://coinmarketcap.com'
HEADERS = {
"user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

r = requests.get(URL, headers=HEADERS, verify=False)
#print(r)

soup = BeautifulSoup(r.text, 'html.parser')
#print(soup)
items = soup.findAll('tr')
# pp(items)

l =[]
for item in items:
    l.append({
        'Названия': item.find('a', class_='cmc-link'),
        'Цена': item.find('div', class_='sc-131di3y-0 cLgOOr')
    })
