# 6
# Спарсить сайт
#
# https://coinmarketcap.com
#
# 1 Название валюты
# 2 Цена
# 3 Вывести все данные в телеграм бот


# import requests
# from bs4 import BeautifulSoup
# from telebot import types
# import telebot
#
# URL = 'https://coinmarketcap.com'
#
# HEADER = {
#     "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
# }
#
# bot = telebot.TeleBot('5022234246:AAHQd_M-0IHUmUJhpPOjvO4RlJjzreD-Jug')
# @bot.message_handler(commands = ["start"])
# def parsing(message):
#     markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
#
#     button1 = types.KeyboardButton("Выведи мне данные с сайта")
#
#     markup.add(button1)
#
#
# @bot.message_handler(content_types = ["text"])
# def lalala(message):
#     try:
#         if message.chat.type == 'private':
#             if message.text == "Спарсить сайт":
#                 r = requests.get(URL, headers=HEADER, verify=False)
#                 soup = BeautifulSoup(r.text, "html.parser")
#                 news = soup.findall('div', class_= 'h7vnx2-2')
#                 new_list = []
#                 for new in news:
#                     new_list.append({
#                         "price" : new.find('div', class_= 'sc-131di3y-0').get_text(),
#                         "currency name" : new.find('div', class_="sc-16r8icm-0").find('p').get_text(strip=True)
#
#                     })

import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types, utils
from aiogram.types import ParseMode


















