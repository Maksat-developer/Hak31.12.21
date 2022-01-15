import requests
from bs4 import BeautifulSoup
import csv

CSV = 'sulpak_smartphones.csv'
URL = 'https://www.sulpak.kg/f/smartfoniy'
HOST = 'https://www.sulpak.kg'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

def get_html(URL, params=''):
    r = requests.get(URL, headers=HEADERS, params=params, verify=False)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('div', class_='goods-tiles')
    l = []
    for item in items:
        l.append({
            "Названиe" : item.find('h3', class_='title').get_text(strip=True),
            "Цена" : item.find('div', class_='price').get_text(strip=True),
            "Фото" : item.find('div', class_='goods-photo').find('a').find(
                'img').get('src'),
            "Ссыка на товар" : HOST + item.find('div',
        class_='product-container-right-side').find('a').get('href')
        })
    return l

def save(items, path):
    with open(path, 'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Названиe", "Цена", "Фото", "Ссыка на товар" ])
        for item in items:
            writer.writerow([item["Названиe"], item["Цена"], item["Фото"],
                             item["Ссыка на товар"]])

def pagination():
    PAGENATION = input("Введите количество страниц: ")
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        list_page = []
        for page in range(1, PAGENATION):
            print(f"Страница {page} готова")
            html = get_html(URL, params={'page':page})
            list_page.extend(get_content(html.text))
        save(list_page, CSV)
        print("Парсинг готов")
    else:
        print("Error")

pagination()



import requests # библиотека "requests" отправляет запрос по указанному "URL"
from bs4 import BeautifulSoup # библиотка "BeautifulSoup" берет "html" шаблон
from pprint import  pprint as pp # просто красивый принт
import csv # превращаем наши данные в "csv "


URL = 'https://health-diet.ru/'  # сюда ссылка на главную страничку которую мы парсим
HEADERS = {   # сюда "User-Agent" ваш который вы находите в сети
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0'
}

r = requests.get(URL, headers=HEADERS, verify=False) # это "get" запрос для получения данных
 # pp(r)  проверяем
soup = BeautifulSoup(r.text, 'html.parser') # с библиотекой "BeautifulSoup" в виде "html.parser" шаблона
# pp(soup) проверяем

# создаем переменную с которой мы берем " div" в которой находятся все остальные блоки то есть тут мы заходим к главному дереву
posts = soup.findAll('div', class_='mzr-block') #
# pp(posts) проверяем

new_list = [] #  создаем пустой лист для того чтобы в него
# ".append(#)" довабить то что мы получили в "for"

for item in posts:  # начинается цикл который итерирует все что
                    # находится в переменной "posts" в котором мы сперва зошли в головной блок

    #  тут мы аппендим все что получаем
    new_list.append({ # тут мы получаем "name" заходся с циколм "for" и помшью "find" дальше указываем тег "div"
                      # и класс  и в конце если возможно убираем лишний мусор с помошью ".get_text(strip=True)"
        'name' : item.find('div', class_='mzr-block-header-post uk-clearfix').find('a', class_='el-user').get_text(strip=True), #
        'time' : item.find('div', class_='el-timeAgo').get_text(strip=True), #
        'theme' : item.find('div', class_='mzr-font--body18sb').get_text(strip=True), #
        'description' : item.find('div', class_='')
    })
pp(new_list) # И выводим лист нами ранее созданный, к которому мы аппендили все что получили

with open('path', 'a') as file: # открывем новый файл в которую засовывем все что мы получили
    writer = csv.writer(file, delimiter=';') # "csv.writer" метод который читает файл и добавляет в нее все что мы получили

    # тут читаются ключи и присваиватся значения что мы получили к ним
    writer.writerow(['name', 'time', 'theme', 'description'])
    # и с помошью "for" мы проходимся по "new_list" в которую мы аппендили все данные которые добавили
    for item in new_list:
        writer.writerow([item['name'],
                         item['time'],
                         item['theme'],
                         item['description']])

