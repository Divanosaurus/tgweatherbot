import os
import datetime
import telebot
import requests
import natasha
from config import open_weather_token

bot = telebot.TeleBot('   ')

start_txt = "Привет! Код работает! Теперь можешь запросить прогноз погоды"  # тут у нас приветственное сообщение

@bot.message_handler(commands=['start'])    # обработчик старта, далее вывод приветствия
def start(message):
    bot.send_message(message.from_user.id, start_txt, parse_mode='Markdown')

# здесь должен быть обработчик текстового запроса
@bot.message_handler(content_types=['text'])
def weather(message):
    city = message.text # тут берется название города из сообщения

    url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=    '


    weather_data = requests.get(url).json()
    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])

    w_now = 'Сейчас в городе ' + city + ' ' + str(temperature) + ' °C'
    w_feels = 'Ощущается как ' + str(temperature_feels) + ' °C'

    bot.send_message(message.from_user.id, w_now)
    bot.send_message(message.from_user.id, w_feels)

    

# бесконечная опрашивалка бота на наличие новых сообщений
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            print('Ошибка!')

