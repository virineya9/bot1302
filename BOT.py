import telebot
token = '5209209288:AAE2TcFelXOkvp7GQKOr5Bgh9mbJxEMUe1w'
bot = telebot.TeleBot(token)

    
@bot.message_handler(commands=["start"])
def  start_message(message):
    bot.send_message(message.chat.id, text = "Hi")

if __name__ == '__main__':
     bot.infinity_polling()
        
