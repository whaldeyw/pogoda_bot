import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from creat_bot import dp, bot
from aiogram import types, Dispatcher
from Button_pogoda.button_time import perv
from Button_pogoda.button_time import back_per
import json

# @dp.message_handler(commands=['Перевоз'])
async def perevoz(message: types.Message):
    with open("us.json", 'r', encoding='utf-8') as f_o:
        data_from_json = json.load(f_o)

    user_id = message.from_user.id
    user_name= message.from_user.username
    ful_name = message.from_user.full_name

    if str(user_id) not in data_from_json:
        data_from_json[user_id] ={'user_id' : user_id}, {'user_name': user_name}, {'ful_name' : ful_name}

    with open('us.json', 'w', encoding='utf-8') as f_o:
        json.dump(data_from_json , f_o, indent=4, ensure_ascii=False)

    await bot.send_message(message.from_user.id, f'Теперь выбери период', reply_markup=perv )

# @dp.message_handler(commands=['Прогноз_На_Неделю_Перевоз'])
async def perevoz_7_day(message: types.Message):
    headers = {
        "Accept": "*/*",
        "User-Agent": "UserAgent().chrome"
    }

    url = 'https://yandex.ru/pogoda/?lat=55.59685135&lon=44.54493713'
    r = requests.get(url, headers=headers)
    src = r.text

    soup = BeautifulSoup(src, 'lxml')
    data_4 = soup.find_all(class_='link link_theme_normal text forecast-briefly__day-link i-bem')

    title = 'Прогноз погоды в Перевозе'
    a1 = data_4[0].get('aria-label')
    a2 = data_4[1].get('aria-label')
    a3 = data_4[2].get('aria-label')
    a4 = data_4[3].get('aria-label')
    a5 = data_4[4].get('aria-label')
    a6 = data_4[5].get('aria-label')
    a7 = data_4[6].get('aria-label')
    per1 = f'{title}\n{a1}\n{a2}\n{a3}\n{a4}\n{a5}\n{a6}\n{a7}'
    await bot.send_message(message.from_user.id, per1, reply_markup=back_per )

# @dp.message_handler(commands=['Назад_Перевоз'])
async def Perevoz_back(message: types.Message):
    await bot.send_message(message.from_user.id, f'Теперь выбери период', reply_markup=perv )

# @dp.message_handler(commands=['Прогноз_На_Месяц_Перевоз'])
async def perevoz_mes(message: types.Message):
    headers = {
        "Accept": "*/*",
        "User-Agent": "UserAgent().chrome"
    }

    url = 'https://yandex.ru/pogoda/?lat=55.59685135&lon=44.54493713'
    r = requests.get(url, headers=headers)
    src = r.text

    soup = BeautifulSoup(src, 'lxml')

    data_4 = soup.find_all(class_='link link_theme_normal text forecast-briefly__day-link i-bem')
    for item4 in data_4:
        per = item4.get('aria-label')
        await bot.send_message(message.from_user.id, per, reply_markup=back_per )

def register_handlers_Perevoz(dp : Dispatcher):
    dp.register_message_handler(perevoz, commands=['Перевоз'])
    dp.register_message_handler(perevoz_7_day, commands=['Прогноз_На_Неделю_Перевоз'])
    dp.register_message_handler(Perevoz_back, commands=['Назад_Перевоз'])
    dp.register_message_handler(perevoz_mes, commands=['Прогноз_На_Месяц_Перевоз'])
