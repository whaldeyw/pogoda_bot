from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

key_1 = KeyboardButton('/Вад')
key_back = KeyboardButton('/Назад_Вад')
key_back_2 = KeyboardButton('/Назад_Выбор_Метеостанции')
key_bigmur = KeyboardButton('/Большое_Мурашкино')
key_perevoz = KeyboardButton('/Перевоз')
key_arzic = KeyboardButton('/Арзамас')
key_buturlino = KeyboardButton('/Бутурлино')
key_konya = KeyboardButton('/Княгинино')
key_nino = KeyboardButton('/Нижний_Новгород')
key_bor = KeyboardButton('/Бор')



key_region =ReplyKeyboardMarkup(resize_keyboard=True).row(key_1, key_perevoz, key_bor, key_arzic)\
    .add(key_bigmur).row(key_buturlino,key_konya, key_nino).add(key_back_2)

key_today = ReplyKeyboardMarkup(resize_keyboard=True).add(key_back)