import telebot
from telebot import types

TOKEN = '5803675179:AAHtgKLhtwZC4caauw7aa3ilvDtgCd7v1J4'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Да!')
    btn2 = types.KeyboardButton('Чуть позже')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text='Привет, {0.first_name}! Я могу подобрать для вас идеальную пиццу, которую вы хотите '
                          'сейчас. Начнём?'.format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'Да!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Острую')
        btn2 = types.KeyboardButton('Не острую')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text='Какую пиццу вы хотите?', reply_markup=markup)
    elif message.text == 'Чуть позже':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Я хочу пиццу прямо сейчас!')
        markup.add(btn1)
        bot.send_message(message.chat.id, text='Буду вас ждать здесь!')
    else:
        bot.send_message(message.chat.id, text='На такую комманду я не запрограммирован(')


bot.infinity_polling()
