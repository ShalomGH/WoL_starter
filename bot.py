import os

import telebot
from dotenv import load_dotenv


dotenv_path = os.path.join('', '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    with open('.env', 'w') as env:
        env.write('TOKEN=\n')
    raise Exception('You need to fill in the .env file')

token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Включить', 'Майнкрафт')
    bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'включить':
        print(message.text.lower())
        bot.send_message(message.chat.id, 'Включаю компутер!')
    elif message.text.lower() == 'майнкрафт':
        print(message.text.lower())
        bot.send_message(message.chat.id, 'Включаю компутер и Майнкрафт!')


bot.infinity_polling()
