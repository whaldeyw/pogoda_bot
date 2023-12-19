from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

key_1 = KeyboardButton('/Сегодня')
key_2 = KeyboardButton('/Завтра')
key_3 = KeyboardButton('/Неделя')
key_4 = KeyboardButton('/Назад_Выбор_Региона')
key_time =ReplyKeyboardMarkup(resize_keyboard=True).row(key_1, key_2, key_3).add(key_4)

key_mur1 = KeyboardButton('/Прогноз_На_неделю')
key_mur2 = KeyboardButton('/Прогноз_На_месяц')
key_mur3 = KeyboardButton('/Назад_Выбор_Региона')
key_mur = ReplyKeyboardMarkup(resize_keyboard=True).row(key_mur1, key_mur2).add(key_mur3)

back_mu = KeyboardButton('/Назад_Мурашкино')
back_mur = ReplyKeyboardMarkup(resize_keyboard=True).add(back_mu)

per1 = KeyboardButton('/Прогноз_На_неделю_Перевоз')
per2 = KeyboardButton('/Прогноз_На_месяц_Перевоз')
per3 = KeyboardButton('/Назад_Выбор_Региона')
perv = ReplyKeyboardMarkup(resize_keyboard=True).row(per1, per2).add(per3)

back_pe = KeyboardButton('/Назад_Перевоз')
back_per = ReplyKeyboardMarkup(resize_keyboard=True).add(back_pe)

arz1 = KeyboardButton('/Прогноз_На_неделю_Арзамас')
aez2 = KeyboardButton('/Прогноз_На_месяц_Арзамас')
arz3 = KeyboardButton('/Назад_Выбор_Региона')
arzb = ReplyKeyboardMarkup(resize_keyboard=True).row(arz1, aez2).add(arz3)

back_ar = KeyboardButton('/Назад_Арзамас')
back_arz = ReplyKeyboardMarkup(resize_keyboard=True).add(back_ar)

but1 = KeyboardButton('/Прогноз_На_неделю_Бутурлино')
but2 = KeyboardButton('/Прогноз_На_месяц_Бутурлино')
but3 = KeyboardButton('/Назад_Выбор_Региона')
butb = ReplyKeyboardMarkup(resize_keyboard=True).row(but1, but2).add(but3)

back_u = KeyboardButton('/Назад_Бутурлино')
back_but = ReplyKeyboardMarkup(resize_keyboard=True).add(back_u)

but1 = KeyboardButton('/Прогноз_На_неделю_Княгинино')
but2 = KeyboardButton('/Прогноз_На_месяц_Княгинино')
but3 = KeyboardButton('/Назад_Выбор_Региона')
butkonya = ReplyKeyboardMarkup(resize_keyboard=True).row(but1, but2).add(but3)

back_u = KeyboardButton('/Назад_Княгинино')
back_konya = ReplyKeyboardMarkup(resize_keyboard=True).add(back_u)

but1 = KeyboardButton('/Прогноз_На_неделю_Нижний_Новгород')
but2 = KeyboardButton('/Прогноз_На_месяц_Нижний_Новгород')
but3 = KeyboardButton('/Назад_Выбор_Региона')
butnino = ReplyKeyboardMarkup(resize_keyboard=True).row(but1, but2).add(but3)

back_u = KeyboardButton('/Назад_Нижний_Новгород')
back_nino = ReplyKeyboardMarkup(resize_keyboard=True).add(back_u)

bor1 = KeyboardButton('/Прогноз_На_неделю_Бор')
bor2 = KeyboardButton('/Прогноз_На_месяц_Бор')
bor3 = KeyboardButton('/Назад_Выбор_Региона')
butbor = ReplyKeyboardMarkup(resize_keyboard=True).row(bor1, bor2).add(bor3)

back_bor = KeyboardButton('/Назад_Бор')
back_bor = ReplyKeyboardMarkup(resize_keyboard=True).add(back_bor)


