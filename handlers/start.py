from creat_bot import dp, bot
from aiogram import types, Dispatcher
import json
from Button_pogoda.button_1 import key_start
import requests
from bs4 import BeautifulSoup
from time import sleep


# @dp.message_handler(commands=['start'])
async def start(message: types.Message):

    with open("us.json", 'r', encoding='utf-8') as f_o:
        data_from_json = json.load(f_o)

    user_id = message.from_user.id
    user_name= message.from_user.username
    ful_name = message.from_user.full_name

    if str(user_id) not in data_from_json:
        data_from_json[user_id] ={'user_id' : user_id}, {'user_name': user_name}, {'ful_name' : ful_name}

    with open('us.json', 'w', encoding='utf-8') as f_o:
        json.dump(data_from_json , f_o, indent=4, ensure_ascii=False)


    await bot.send_message(message.chat.id, f'Привет {message.from_user.full_name}, Жми на кнопки и получи погоду'
                                            f' для своего региона и выбери метеостанцию.\n'
                                            f'Теперь можно получить погоду где бы вы не находились '
                                            f'достаточно лишь поделиться своим местоположением ', reply_markup=key_start)

async def pos(message: types.Message):
        with open("us.json", 'r', encoding='utf-8') as f_o:
            data_from_json = json.load(f_o)
        for i, v in data_from_json.items():
            full_name = v[2]['ful_name']
            user_name = v[1]["user_name"]
            await bot.send_message(message.from_user.id, f'User_Name  - {user_name}, Полное Имя: {full_name}')

@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "latitude:  {}\nlongitude: {}".format(lat, lon)

    headers = {"User-Agent":
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}


    url = f'https://yandex.ru/pogoda/details/10-day-weather?lat={lat}&lon={lon}&via=mf#9'
    r = requests.get(url, headers)

    soup = BeautifulSoup(r.text, 'lxml')
   
    data = soup.find_all('article', class_='card')

    for i in data:
        day = i.find('span', class_='a11y-hidden')
        if day == None:
            continue
        else:
            day = i.find('span', class_='a11y-hidden').text
        wetter = i.find('td', class_='weather-table__body-cell weather-table__body-cell_type_condition').text

        morning = i.find_all('span', class_='a11y-hidden')[3]
        day_temp = i.find_all('span', class_='a11y-hidden')[6]
        evening = i.find_all('span', class_='a11y-hidden')[9]
        night = i.find_all('span', class_='a11y-hidden')[12]

        d = f'\n{day}\n {morning.text}\n {day_temp.text} {wetter}\n {evening.text}\n {night.text}'

        await bot.send_message(message.from_user.id, d)

def register_handlers_start(dp : Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(pos, commands=['посетители'])
    dp.register_message_handler(handle_location, content_types=['location'])