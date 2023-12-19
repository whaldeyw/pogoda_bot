import requests
from bs4 import BeautifulSoup
from time import sleep
from creat_bot import dp, bot
from aiogram import types, Dispatcher
from Button_pogoda.button_region import key_today

async def vad_7_day(message: types.Message):
    headers = {"User-Agent":
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}


    url = 'https://yandex.ru/pogoda/details/10-day-weather?lat=55.531463&lon=44.20923&via=mf#9'
    r = requests.get(url, headers)

    soup = BeautifulSoup(r.text, 'lxml')

    all_data = soup.findAll('span', class_='a11y-hidden')
    wetter = soup.findAll('td', class_='weather-table__body-cell weather-table__body-cell_type_condition')

    today = all_data[0].text
    morning_temp = all_data[3].text
    morning_wetter = wetter[0].text

    day_temp = all_data[6].text
    day_wetter = wetter[1].text

    evening_temp = all_data[9].text
    evening_wetter = wetter[2].text

    night_temp = all_data[12].text
    night_wetter = wetter[3].text

    day_1 = f'{today}\n {morning_temp} {morning_wetter} \n {day_temp} {day_wetter}\n' \
            f'{evening_temp} {evening_wetter}\n {night_temp} {night_wetter}'
    tomorrow = all_data[17].text
    morning_temp = all_data[20].text
    morning_wetter = wetter[4].text

    day_temp = all_data[23].text
    day_wetter = wetter[5].text

    evening_temp = all_data[26].text
    evening_wetter = wetter[6].text

    night_temp = all_data[29].text
    night_wetter = wetter[7].text

    day_2 = f'{tomorrow}\n {morning_temp} {morning_wetter} \n {day_temp} {day_wetter}\n' \
            f'{evening_temp} {evening_wetter}\n {night_temp} {night_wetter}'

    tomorrow = all_data[34].text
    morning_temp = all_data[37].text
    morning_wetter = wetter[8].text

    day_temp = all_data[40].text
    day_wetter = wetter[9].text

    evening_temp = all_data[43].text
    evening_wetter = wetter[10].text

    night_temp = all_data[46].text
    night_wetter = wetter[11].text

    day_3 = f'{tomorrow}\n {morning_temp} {morning_wetter} \n {day_temp} {day_wetter}\n' \
            f'{evening_temp} {evening_wetter}\n {night_temp} {night_wetter}'

    tomorrow = all_data[51].text
    morning_temp = all_data[54].text
    morning_wetter = wetter[9].text

    day_temp = all_data[57].text
    day_wetter = wetter[10].text

    evening_temp = all_data[60].text
    evening_wetter = wetter[11].text

    night_temp = all_data[63].text
    night_wetter = wetter[12].text

    day_4 = f'{tomorrow}\n {morning_temp} {morning_wetter} \n {day_temp} {day_wetter}\n' \
            f'{evening_temp} {evening_wetter}\n {night_temp} {night_wetter}'

    tomorrow = all_data[68].text
    morning_temp = all_data[71].text
    morning_wetter = wetter[10].text

    day_temp = all_data[74].text
    day_wetter = wetter[11].text

    evening_temp = all_data[77].text
    evening_wetter = wetter[12].text

    night_temp = all_data[80].text
    night_wetter = wetter[13].text

    day_5 = f'{tomorrow}\n {morning_temp} {morning_wetter} \n {day_temp} {day_wetter}\n' \
            f'{evening_temp} {evening_wetter}\n {night_temp} {night_wetter}'

    tomorrow = all_data[85].text
    morning_temp = all_data[88].text
    morning_wetter = wetter[11].text

    day_temp = all_data[91].text
    day_wetter = wetter[12].text

    evening_temp = all_data[94].text
    evening_wetter = wetter[13].text

    night_temp = all_data[97].text
    night_wetter = wetter[14].text

    day_6 = f'{tomorrow}\n {morning_temp} {morning_wetter} \n {day_temp} {day_wetter}\n' \
            f'{evening_temp} {evening_wetter}\n {night_temp} {night_wetter}'

    tomorrow = all_data[85].text
    morning_temp = all_data[88].text
    morning_wetter = wetter[11].text

    day_temp = all_data[91].text
    day_wetter = wetter[12].text

    evening_temp = all_data[94].text
    evening_wetter = wetter[13].text

    night_temp = all_data[97].text
    night_wetter = wetter[14].text

    day_7 = f'{tomorrow}\n {morning_temp} {morning_wetter} \n {day_temp} {day_wetter}\n' \
            f'{evening_temp} {evening_wetter}\n {night_temp} {night_wetter}'

    day_10 = f'{day_1}\n\n{day_2}\n\n{day_3}\n\n{day_4}\n{day_5}\n\n{day_6}\n\n{day_7}'


    await bot.send_message(message.from_user.id, day_10, reply_markup=key_today )

def register_handlers_vad_7_day(dp : Dispatcher):
    dp.register_message_handler(vad_7_day, commands=['Неделя'])
