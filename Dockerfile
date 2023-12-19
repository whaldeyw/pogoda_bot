FROM python:3.10

WORKDIR /app

RUN pip install aiogram

COPY . .

RUN pip install -r requirements.txt

CMD ["python" , "pogoda_bot.py"]