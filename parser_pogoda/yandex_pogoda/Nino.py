import requests
from bs4 import BeautifulSoup
from time import sleep
from fake_useragent import UserAgent

headers ={
    "Accept": "*/*",
    "User-Agent":  "UserAgent().chrome"
}

sleep(2)
url ='https://yandex.ru/pogoda/?lat=56.32679749&lon=44.00651932'
r = requests.get(url, headers=headers)
src = r.text

soup = BeautifulSoup(src, 'lxml')

data_4 = soup.find_all(class_='link link_theme_normal text forecast-briefly__day-link i-bem')
data_5 = soup.find(class_='fact__temp-wrap').get('aria-label')

title = 'Прогноз погоды в Нижнем Новгороде'
a1 = data_4[0].get('aria-label')
a2 = data_4[1].get('aria-label')
a3 = data_4[2].get('aria-label')
a4 = data_4[3].get('aria-label')
a5 = data_4[4].get('aria-label')
a6 = data_4[5].get('aria-label')
a7 = data_4[6].get('aria-label')
a8 = data_4[7].get('aria-label')
a9 = data_4[8].get('aria-label')
a10 = data_4[9].get('aria-label')
a11 = data_4[10].get('aria-label')
a12 = data_4[11].get('aria-label')
a13 = data_4[12].get('aria-label')
a14 = data_4[13].get('aria-label')
a15 = data_4[14].get('aria-label')
a16 = data_4[15].get('aria-label')
a17 = data_4[16].get('aria-label')
a18 = data_4[17].get('aria-label')
a19 = data_4[18].get('aria-label')
a20 = data_4[19].get('aria-label')
a21 = data_4[20].get('aria-label')
a22 = data_4[21].get('aria-label')
a23 = data_4[22].get('aria-label')
a24 = data_4[23].get('aria-label')
a25 = data_4[24].get('aria-label')
a26 = data_4[25].get('aria-label')
a27 = data_4[26].get('aria-label')
a28 = data_4[27].get('aria-label')
a29 = data_4[28].get('aria-label')
a30 = data_4[29].get('aria-label')
a31 = data_4[30].get('aria-label')

nino = f'{title}\n{a1}\n{a2}\n{a3}\n{a4}\n{a5}\n{a6}\n{a7}\n{a8}\n{a9}\n{a10}\n{a11}\n{a12}\n{a13}\n{a14}\n/' \
          f'{a15}\n{a16}\n{a17}\n{a18}\n{a19}\n{a20}\n{a21}\n{a22}\n{a23}\n{a24}\n{a25}\n{a26}\n{a27}\n{a28}\n{a29}\n{a30}\n{a31}'

nino1 = f'{title}\n{a1}\n{a2}\n{a3}\n{a4}\n{a5}\n{a6}\n{a7}'