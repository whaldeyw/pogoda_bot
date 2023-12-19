from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from dotenv import load_dotenv
load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)