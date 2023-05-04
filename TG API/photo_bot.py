import requests
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = 'TOKEN'
URL = 'https://cataas.com/cat'

bot = telebot.TeleBot(TOKEN)
keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True)
keyboard.add(KeyboardButton('Котика!'))


def get_cat():
    response = requests.get(URL)
    return response.content


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Я тестовый бот!",
                     reply_markup=keyboard)


@bot.message_handler(regexp='кот')
def cat_image_message(message):
    photo = get_cat()
    bot.send_photo(message.chat.id, photo)


bot.infinity_polling()
