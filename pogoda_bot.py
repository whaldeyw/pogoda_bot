from aiogram import executor
from creat_bot import dp

async def on_startup(_):
    print('Бот вышел онлайн')

from handlers import start, yandex_region, vad_7_day, vad_today, vad_tomorrow, murashkino, Perevoz, Arzamas, Buturlino\
    ,Knyaginino, Nino, Bor
start.register_handlers_start(dp)
yandex_region.register_handlers_yandex_region(dp)
vad_today.register_handlers_vad_today(dp)
vad_7_day.register_handlers_vad_7_day(dp)
vad_tomorrow.register_handlers_vad_today(dp)
murashkino.register_handlers_big_mur(dp)
Perevoz.register_handlers_Perevoz(dp)
Arzamas.register_handlers_arzamas(dp)
Buturlino.register_handlers_buturlino(dp)
Knyaginino.register_handlers_knyaginino(dp)
Nino.register_handlers_Nino(dp)
Bor.register_handlers_bor(dp)

executor.start_polling(dp,skip_updates=True, on_startup=on_startup)

