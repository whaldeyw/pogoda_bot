import requests
from bs4 import BeautifulSoup
from creat_bot import dp, bot
from aiogram import types, Dispatcher
from time import sleep
from Button_pogoda.button_bor import butbor
from Button_pogoda.button_bor import back_bor
import json


# @dp.message_handler(commands=['Бор'])
async def bor(message: types.Message):
    with open("us.json", 'r', encoding='utf-8') as f_o:
        data_from_json = json.load(f_o)

    user_id = message.from_user.id
    user_name= message.from_user.username
    ful_name = message.from_user.full_name

    if str(user_id) not in data_from_json:
        data_from_json[user_id] ={'user_id' : user_id}, {'user_name': user_name}, {'ful_name' : ful_name}

    with open('us.json', 'w', encoding='utf-8') as f_o:
        json.dump(data_from_json , f_o, indent=4, ensure_ascii=False)

    await bot.send_message(message.from_user.id, f'Теперь выбери период', reply_markup=butbor)

# @dp.message_handler(commands=['Прогноз_На_Неделю_Бутурлино'])
async def bor_7_day(message: types.Message):
    headers = {
        "Accept": "*/*",
        "User-Agent": "UserAgent().chrome"
    }

    sleep(2)
    url = 'https://yandex.ru/pogoda/?lat=56.35652161&lon=44.0645752'
    r = requests.get(url, headers=headers)
    src = r.text

    soup = BeautifulSoup(src, 'lxml')
    title = 'Прогноз погоды на Бору'
    data_4 = soup.find_all(class_='link link_theme_normal text forecast-briefly__day-link i-bem')
    a1 = data_4[0].get('aria-label')
    a2 = data_4[1].get('aria-label')
    a3 = data_4[2].get('aria-label')
    a4 = data_4[3].get('aria-label')
    a5 = data_4[4].get('aria-label')
    a6 = data_4[5].get('aria-label')
    a7 = data_4[6].get('aria-label')
    bor1 = f'{title}\n{a1}\n{a2}\n{a3}\n{a4}\n{a5}\n{a6}\n{a7}'
    await bot.send_message(message.from_user.id,bor1,reply_markup= back_bor)

# @dp.message_handler(commands=['Назад_Бор'])
async def back_bor1(message: types.Message):
    await bot.send_message(message.from_user.id, f'Теперь выбери период', reply_markup=butbor )

# @dp.message_handler(commands=['Прогноз_На_Месяц_Бор'])
async def bor_30_day(message: types.Message):
    headers = {
        "Accept": "*/*",
        "User-Agent": "UserAgent().chrome"
    }

    sleep(2)
    url = 'https://yandex.ru/pogoda/?lat=56.35652161&lon=44.0645752'
    r = requests.get(url, headers=headers)
    src = r.text

    soup = BeautifulSoup(src, 'lxml')

    title = 'Прогноз погоды на Бору'
    data_4 = soup.find_all(class_='link link_theme_normal text forecast-briefly__day-link i-bem')
    for i in data_4:
        item = i.get('aria-label')

        await bot.send_message(message.from_user.id, f'{title}\n {item}', reply_markup=back_bor )

def register_handlers_bor(dp : Dispatcher):
    dp.register_message_handler(bor, commands=['Бор'])
    dp.register_message_handler(bor_7_day, commands=['Прогноз_На_Неделю_Бор'])
    dp.register_message_handler(back_bor1, commands=['Назад_Бор'])
    dp.register_message_handler(bor_30_day, commands=['Прогноз_На_Месяц_Бор'])