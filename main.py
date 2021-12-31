# class Student:
#     """Описание 'Student' """
#     def __init__(self, name, lastname, year_of_entrance, department):
#         """Свойства '' """
#
#         self.name = name
#         self.lastname = lastname
#         self.year_of_entrance = year_of_entrance
#         self.department =department
#
#     def get_student_info(self):
#         """Выводит сообщение в каком году поступил 'Student' """
#         print("Student " + self.name + self.lastname +
#               " Enrolled in " + str(self.year_of_entrance) + # чтобы введенное в обьекте числа считались как строки конвертируем их в "str"
#               " years To the faculty " + self.department)
#
# # Не забывайте пробелы между переданных в обьекте значениях чтобы на  выводе они не слепились
# Student1 = Student("Adler ", "Franklin", 1995, "Programming")
#
#     # """так мы выводим только "name" and "lastname" Students"""
#     # print(Student1.name, Student1.lastname)  так мы выводим только "name" and "lastname" Students
#
# Student1.get_student_info()




# import requests
# from bs4 import BeautifulSoup
# import telebot
# import json
#
# URL = 'https://news.ycombinator.com/'
# HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
# }
# bot = telebot.TeleBot('5090981615:AAHPD44nKBiP-klwv78Cj1lVQUQ0IeL7fAE')
#
# @bot.message_handler(commands=['start'])
# def parsing(message):
#
#     markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#
#     item1 = telebot.types.KeyboardButton("Спарсить сайт")
#     item2 = telebot.types.KeyboardButton("Получить ссылки")
#     markup.add(item1, item2)
#
#     bot.send_message(message.chat.id,
#                     '''Добро пожаловать''',
#                     reply_markup=markup)
#
# @bot.message_handler(content_types=['text'])
# def lalala(message):
#     try:
#         if message.chat.type == 'private':
#             if message.text == "Спарсить сайт":
#                 r = requests.get(URL, headers=HEADERS, verify=False)
#                 soup = BeautifulSoup(r.text, 'html.parser')
#                 news = soup.findAll('a', class_='titlelink')
#                 news_list = {}
#                 news_split = URL.split('/')[-1]
#                 news_split = news_split[:-4]
#                 for new in news:
#                     with open('hacker_news.json', 'a') as f:
#                         news_list[news_split] = {
#                             'title': new.get_text(strip=True),
#                             'link': new.get('href')
#                         }
#                         json.dump(news_list, f, indent=4, ensure_ascii=False)
#
#                 markup = telebot.types.InlineKeyboardMarkup(row_width=2)
#                 item1 = telebot.types.InlineKeyboardButton("Получить документ",
#                                                            callback_data="Получить документ")
#                 markup.add(item1)
#                 bot.send_message(message.chat.id,
#                                  "Парсинг готов",
#                                  reply_markup=markup)
#             elif message.text == "Получить ссылки":
#                 with open('hacker_news.json') as file:
#                     news_list = json.load(file)
#                 for k, v in sorted(news_list.items()):
#                     news = f"{k['title']} \n {v['link']}"
#                 bot.send_message(message.chat.id, news)
#             else:
#                 bot.send_message(message.chat.id,
#                     "Я не знаю что ответить")
#     except:
#         print("Что-то не то")
#         bot.send_message(message.chat.id, 'Что-то не то')
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     try:
#         if call.message:
#             if call.data == "Получить документ":
#                 with open('hacker_news.json') as file:
#                     news_list = json.load(file)
#                     bot.send_document(call.message.chat.id, news_list)
#     except:
#         print("Что то не то")
#         bot.send_message(call.message.chat.id, "Что то не то")
#
# bot.polling(none_stop=True)


import telebot
from telebot import types

bot = telebot.TeleBot('5049822153:AAF_vCDWlGtTsR2dfasB9-inwQ-PEjzsVCM')
#  qwer это старт бота
@bot.message_handler(commands=['start'])
def welcom(message): # создаем функцию которая приветствует пользователя при нажатии старта

    photo = open('iphone.jpeg', 'rb') # перердаем с помошью функции "open" картинку в формате "jpeg"

    bot.send_photo(message.chat.id, photo) # тут предаем message-в чат телеграмма photo это переменная

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1. переменная markup.
                                                             # 2.types указывем тип кнопок
                                                             # 3.ReplyKeyboardMarkup
                                                             # 4.resize_keyboard=True пускай выводит мне следуюшие кнопки

    button1 = types.KeyboardButton('Могу приступить к осмотру моделей') # первая созданная кнопка которая высвечивает
                                                   # сообщение 'Идем дальше'
    bot.send_message(message.chat.id,
                     f' "#" {message.from_user}',
                     reply_markup=markup)

    button2 = types.KeyboardButton('"Купить смартфон"') # тут добавляем кнопку еше одну с помошью переменной 'button2'
                                                # и передаем ей тип кнопки 'types'-'KeyboardButton'

    markup.add(button1,button2) # в переменну 'markup' мы добавляем
                                # эти две переменные в которых есть кнопки "button1", "button2"
# создаем декоратор в которую заварачиваем новые кнопки и действия к ним
@bot.message_handler(content_types = ['text']) # Декоратор
def aswer(message): # функция отвечать на конпки

    if message.text == "#":  # если нажать на кнопку  " # "
        bot.send_message(message.chat.id, '#') # то выведи мне следующее сообщение
    elif message.text == '#': # а еше если нажмет на кнопку " # " то выведи следующие типы марок смартфона

        markup = types.InlineKeyboardMarkup(row_width=3) # в начале обозначаете тип кнопок для следующих марок смартфона

        button3= types.InlineKeyboardButton("iphone", # создаёте переменную
                                                      # в которую указвается тип кнопки и "имя кнопки"
                                                      # дальще callback_data="имя кнопки "
                                            callback_data='iphone')

        button4 = types.InlineKeyboardButton("iphone 2",
                                             callback_data='iphone 2')

        button5 = types.InlineKeyboardButton("iphone 3",
                                             callback_data='iphone 3')

        markup.add(button3,button4,button5) # обьединяете все кнопки с помощью метода .add()
                                            # добавляете в ранее созданном переменном (markup) где указан тип кнопки

        bot.send_message(message.chat.id, # вместе с кнопками высветилась сообщение
                                          # передаёте ее в bot.send_message(message.chat.id, " # ", reply_markup=markup)
                         'Какую марку айфона вы хотите?',
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'error') # в другом случае показывай сообщение "error"

@bot.callback_query_handler(func=lambda call : True) # заварачиваем это все в декоратор в котором
def callback_inline(call): # создаем новую функцию которая отвечает за обратный вызов то есть ответ на кнопки
    try: # Засовываем это все в проверку
        if call.message: # если " call " это message то
            if call.data == 'iphone':  # и если нажали на кнопку " iphone "
                bot.send_message(call.message.chat.id, #  то высвети следующее сообщение
                                 '500$')

            if call.data == 'iphone 2':
                bot.send_message(call.message.chat.id,
                                     '600$')

            if call.data == 'iphone 3':
                bot.send_message(call.message.chat.id,
                                     '700$')

    except:
        print('error')

bot.polling(none_stop=True)
