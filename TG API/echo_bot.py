import telebot

TOKEN = '5803675179:AAHtgKLhtwZC4caauw7aa3ilvDtgCd7v1J4'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Я тестовый бот!")


@bot.message_handler(content_types=['text'])
def echo_message(message):
    bot.send_message(message.chat.id, message.text)


bot.infinity_polling()
