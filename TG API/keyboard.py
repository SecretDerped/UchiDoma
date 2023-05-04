import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = '5803675179:AAHtgKLhtwZC4caauw7aa3ilvDtgCd7v1J4'

bot = telebot.TeleBot(TOKEN)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Hello'))
keyboard.add(KeyboardButton('Bye'))


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Я тестовый бот!', reply_markup=keyboard)


@bot.message_handler(regexp=r'hello\.*')
def say_hello(message):
    bot.send_message(message.chat.id, "Hello!")


@bot.message_handler(func=lambda s: 'Bye' in s.text)
def say_bye(message):
    bot.send_message(message.chat.id, "Bye!")


bot.infinity_polling()
