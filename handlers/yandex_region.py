from creat_bot import dp, bot
from aiogram import types, Dispatcher
from Button_pogoda.button_region import key_region
from Button_pogoda.button_time import key_time
from Button_pogoda.button_1 import key_start
import json

# @dp.message_handler(commands=['Яндекс'])
async def mes_yandex(message: types.Message):
    with open("us.json", 'r', encoding='utf-8') as f_o:
        data_from_json = json.load(f_o)

    user_id = message.from_user.id
    user_name= message.from_user.username
    ful_name = message.from_user.full_name

    if str(user_id) not in data_from_json:
        data_from_json[user_id] ={'user_id' : user_id}, {'user_name': user_name}, {'ful_name' : ful_name}

    with open('us.json', 'w', encoding='utf-8') as f_o:
        json.dump(data_from_json , f_o, indent=4, ensure_ascii=False)
    await bot.send_message(message.from_user.id, f'Теперь выбери регион' , reply_markup=key_region)

# @dp.message_handler(commands=['Назад_Выбор_Региона'])
async def mes_region(message: types.Message):
    await bot.send_message(message.from_user.id, f'Теперь выбери регион', reply_markup=key_region )

# @dp.message_handler(commands=['Вад'])
async def mes_vad(message: types.Message):
    await bot.send_message(message.from_user.id, f'Теперь выбери период' , reply_markup=key_time)

# @dp.message_handler(commands=['Назад_Выбор_Метеостанции'])
async def mes_back_meteo(message: types.Message):
    await bot.send_message(message.from_user.id, f'Выбери метеостанцию' , reply_markup=key_start)

# @dp.message_handler(commands=['Назад_Вад'])
async def mes_back_vad(message: types.Message):
    await bot.send_message(message.from_user.id, f'Теперь выбери период' , reply_markup=key_time)

def register_handlers_yandex_region(dp : Dispatcher):
    dp.register_message_handler(mes_yandex, commands=['Яндекс'])
    dp.register_message_handler(mes_region, commands=['Назад_Выбор_Региона'])
    dp.register_message_handler(mes_vad, commands=['Вад'])
    dp.register_message_handler(mes_back_meteo, commands=['Назад_Выбор_Метеостанции'])
    dp.register_message_handler(mes_back_vad, commands=['Назад_Вад'])
