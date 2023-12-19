from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


bor1 = KeyboardButton('/Прогноз_На_Неделю_Бор')
bor2 = KeyboardButton('/Прогноз_На_Месяц_Бор')
bor3 = KeyboardButton('/Назад_Выбор_Региона')
butbor = ReplyKeyboardMarkup(resize_keyboard=True).row(bor1, bor2).add(bor3)

back_bor = KeyboardButton('/Назад_Бор')
back_bor = ReplyKeyboardMarkup(resize_keyboard=True).add(back_bor)