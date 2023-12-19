from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

key_1 = KeyboardButton('/Яндекс')
key_2 = KeyboardButton('/Назад_Выбор_Метеостанции')
b5 = KeyboardButton('/Поделиться местоположением', request_location=True)

key_start =ReplyKeyboardMarkup(resize_keyboard=True).add(key_1, b5)

key_back_yandex_1 = ReplyKeyboardMarkup(resize_keyboard=True).add(key_2)

