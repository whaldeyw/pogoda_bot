import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from creat_bot import dp, bot
from aiogram import types, Dispatcher
from Button_pogoda.button_time import key_mur
from Button_pogoda.button_time import back_mur


# @dp.message_handler(commands=['Большое_Мурашкино'])
async def mes_big_mur(message: types.Message):
    await bot.send_message(message.from_user.id, f'Теперь выбери период', reply_markup=key_mur )

# @dp.message_handler(commands=['Прогноз_На_Неделю'])
async def mes_big_mur_7_day(message: types.Message):
    headers = {
        "Accept": "*/*",
        "User-Agent": "UserAgent().chrome"
    }

    url = 'https://yandex.ru/pogoda/?lat=55.78131866&lon=44.77259827'
    r = requests.get(url, headers=headers)
    src = r.text

    soup = BeautifulSoup(src, 'lxml')

    data_4 = soup.find_all(class_='link link_theme_normal text forecast-briefly__day-link i-bem')
    # for item4 in data_4:
    #     big_mur = item4.get('aria-label')

    title = 'Прогноз погоды в Большое Мурашкино'
    a2 = data_4[1].get('aria-label')
    a3 = data_4[2].get('aria-label')
    a4 = data_4[3].get('aria-label')
    a5 = data_4[4].get('aria-label')
    a6 = data_4[5].get('aria-label')
    a7 = data_4[6].get('aria-label')
    big_mur1 = f'{title}\n{a1}\n{a2}\n{a3}\n{a4}\n{a5}\n{a6}\n{a7}'

    await bot.send_message(message.from_user.id, big_mur1, reply_markup=back_mur )

# @dp.message_handler(commands=['Назад_Мурашкино'])
async def mes_back_mur(message: types.Message):
    await bot.send_message(message.from_user.id, f'Теперь выбери период', reply_markup=key_mur )

# @dp.message_handler(commands=['Прогноз_На_Месяц'])
async def mes_big_mur_mes(message: types.Message):
    headers = {
        "Accept": "*/*",
        "User-Agent": "UserAgent().chrome"
    }

    url = 'https://yandex.ru/pogoda/?lat=55.78131866&lon=44.77259827'
    r = requests.get(url, headers=headers)
    src = r.text

    soup = BeautifulSoup(src, 'lxml')

    data_4 = soup.find_all(class_='link link_theme_normal text forecast-briefly__day-link i-bem')
    for item4 in data_4:
        big_mur = item4.get('aria-label')
        await bot.send_message(message.from_user.id, big_mur, reply_markup=back_mur )

def register_handlers_big_mur(dp : Dispatcher):
    dp.register_message_handler(mes_big_mur, commands=['Большое_Мурашкино'])
    dp.register_message_handler(mes_big_mur_7_day, commands=['Прогноз_На_Неделю'])
    dp.register_message_handler(mes_back_mur, commands=['Назад_Мурашкино'])
    dp.register_message_handler(mes_big_mur_mes, commands=['Прогноз_На_Месяц'])