import telebot
token = '5209209288:AAE2TcFelXOkvp7GQKOr5Bgh9mbJxEMUe1w'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
       bot.send_message(message.chat.id, messege.text)
if __name__ == '__main__':
       bot.infinity_polling()