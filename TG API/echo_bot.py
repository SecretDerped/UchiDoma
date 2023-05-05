import telebot

TOKEN = 'Вставьте свой токен сюда'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Я тестовый бот!")


@bot.message_handler(content_types=['text'])
def echo_message(message):
    bot.send_message(message.chat.id, message.text)


bot.infinity_polling()
