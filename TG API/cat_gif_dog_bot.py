import requests
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = 'Вставьте свой токен сюда'

CAT_URL = 'https://cataas.com/cat'
CAT_GIF_URL = 'https://cataas.com/cat/gif'
DOG_URL = 'https://dog.ceo/api/breeds/image/random'

bot = telebot.TeleBot(TOKEN)
keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True)
keyboard.add(KeyboardButton('Котика!'))
keyboard.add(KeyboardButton('Гифку!'))
keyboard.add(KeyboardButton('Пёсика!'))


def get_cat():
    response = requests.get(CAT_URL)
    return response.content


def get_cat_gif():
    response = requests.get(CAT_GIF_URL)
    return response.content


def get_dog():
    response = requests.get(DOG_URL)
    json = response.json()
    return json['message']


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Я отправляю картинки с котами и пёселями по нажатию кнопки!",
                     reply_markup=keyboard)


@bot.message_handler(regexp='кот')
def cat_image_message(message):
    photo = get_cat()
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(regexp='гиф')
def cat_gif_message(message):
    video = get_cat_gif()
    bot.send_video(message.chat.id, video)


@bot.message_handler(regexp='пёс')
def dog_image_message(message):
    photo = get_dog()
    bot.send_photo(message.chat.id, photo)


bot.infinity_polling()
