import requests
from bs4 import BeautifulSoup
from time import sleep
from fake_useragent import UserAgent



sleep(3)
url ='https://yandex.ru/pogoda/details/10-day-weather?lat=55.531463&lon=44.20923&via=mf#9'
r = requests.get(url, headers= {"User-Agent": UserAgent().chrome})

soup = BeautifulSoup(r.text , 'lxml')

all_data = soup.findAll('span', class_='a11y-hidden')
wetter = soup.findAll('td', class_='weather-table__body-cell weather-table__body-cell_type_condition')

tomorrow = all_data[17].text
morning_temp = all_data[20].text
morning_wetter = wetter[4].text

day_temp = all_data[23].text
day_wetter = wetter[5].text

evening_temp = all_data[26].text
evening_wetter = wetter[6].text

night_temp = all_data[29].text
night_wetter = wetter[7].text

tomorrow_1 = f'{tomorrow}\n {morning_temp} {morning_wetter} \n {day_temp} {day_wetter}\n'\
             f'{evening_temp} {evening_wetter}\n {night_temp} {night_wetter}'

# for key, value in r.request.headers.items():
#     print(key+': '+value)