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

today = all_data[0].text
morning_temp = all_data[3].text
morning_wetter = wetter[0].text

day_temp = all_data[6].text
day_wetter = wetter[1].text

evening_temp = all_data[9].text
evening_wetter = wetter[2].text

night_temp = all_data[12].text
night_wetter = wetter[3].text

today_1 = f'{today}\n {morning_temp} {morning_wetter} \n {day_temp} {day_wetter}\n'\
             f'{evening_temp} {evening_wetter}\n {night_temp} {night_wetter}'

