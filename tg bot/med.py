import telebot
from telebot import types
import requests

token = "8391260970:AAHDOEeJVoH6KuZ7-s5nKw9rV5KSiK1ghVk"
wheather_API_KEY='35a25a4f8ae94d7fa76153709253006'
bot = telebot.TeleBot(token)

def get_weather(city):
    try:
        url=f'https://api.weatherapi.com/v1/current.json?key={wheather_API_KEY}&q={city}&aqi=no'
        response= requests.get(url)
        data = response.json()

        if 'error' not in data:
            location = data['location']['name']
            country = data['location']['country']
            current =data['current']
            weather_desc= current['condition']['text']
            temp=current['temp_c']
            humidity=current['humidity']
            wind_speed=current['wind_kph']
            weather_report=(
                f'Current weather in{location},{country}:\n'
                f'Description:{weather_desc}\n'
                f'Температура:{temp} C\n'
                f'Влажность:{humidity}\n'
                f'Скорость ветра:{wind_speed}\n'
            )
        else:
            weather_report=f"Error: {data['error']['message']}"
    except requests.exceptions.RequestException:
        weather_report= 'Ошибка'
    return weather_report


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'здравстуйте напишите город и я отправлю вам текущую погоду ')
    
@bot.message_handler(func= lambda message: True)
def send_weather(message):
    city= message.text.strip()
    weather_report= get_weather(city)
    bot.reply_to(message, weather_report)
    
    
    
    
bot.polling(none_stop=True)
    
