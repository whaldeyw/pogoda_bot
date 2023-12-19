import requests
from bs4 import BeautifulSoup
from creat_bot import dp, bot
from aiogram import types, Dispatcher
from time import sleep
from Button_pogoda.button_time import butkonya
from Button_pogoda.button_time import back_konya

# @dp.message_handler(commands=['Княгинино'])
async def knyaginino(message: types.Message):
    await bot.send_message(message.from_user.id, f'Теперь выбери период', reply_markup=butkonya)

# @dp.message_handler(commands=['Прогноз_На_Неделю_Княгинино'])
async def knyaginino_7_day(message: types.Message):
    headers = {
        "Accept": "*/*",
        "User-Agent": "UserAgent().chrome"
    }

    sleep(2)
    url = 'https://yandex.ru/pogoda/?lat=55.82056808&lon=45.03225327'
    r = requests.get(url, headers=headers)
    src = r.text

    soup = BeautifulSoup(src, 'lxml')

    data_4 = soup.find_all(class_='link link_theme_normal text forecast-briefly__day-link i-bem')
    title = 'Прогноз погоды в Княгинино'
    a1 = data_4[0].get('aria-label')
    a2 = data_4[1].get('aria-label')
    a3 = data_4[2].get('aria-label')
    a4 = data_4[3].get('aria-label')
    a5 = data_4[4].get('aria-label')
    a6 = data_4[5].get('aria-label')
    a7 = data_4[6].get('aria-label')
    konya1 = f'{title}\n{a1}\n{a2}\n{a3}\n{a4}\n{a5}\n{a6}\n{a7}'
    await bot.send_message(message.from_user.id, konya1, reply_markup=back_konya )
    print(soup.text)

# @dp.message_handler(commands=['Назад_Княгинино'])
async def back_knyaginino(message: types.Message):
    await bot.send_message(message.from_user.id, f'Теперь выбери период', reply_markup=butkonya )

# @dp.message_handler(commands=['Прогноз_На_Месяц_Княгинино'])
async def knyaginino_30_day(message: types.Message):
    headers = {
        "Accept": "*/*",
        "User-Agent": "UserAgent().chrome"
    }

    sleep(2)
    url = 'https://yandex.ru/pogoda/?lat=55.56781769&lon=44.90482712'
    r = requests.get(url, headers=headers)
    src = r.text

    soup = BeautifulSoup(src, 'lxml')
    title = 'Прогноз погоды в Княгинино'
    data_4 = soup.find_all(class_='link link_theme_normal text forecast-briefly__day-link i-bem')
    for i in data_4:
        item = i.get('aria-label')
        await bot.send_message(message.from_user.id,f'{title}\n {item}', reply_markup=back_konya )

def register_handlers_knyaginino(dp : Dispatcher):
    dp.register_message_handler(knyaginino, commands=['Княгинино'])
    dp.register_message_handler(knyaginino_7_day, commands=['Прогноз_На_Неделю_Княгинино'])
    dp.register_message_handler(back_knyaginino, commands=['Назад_Княгинино'])
    dp.register_message_handler(knyaginino_30_day, commands=['Прогноз_На_Месяц_Княгинино'])