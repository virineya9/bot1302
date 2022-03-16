import telebot
token = '5209209288:AAE2TcFelXOkvp7GQKOr5Bgh9mbJxEMUe1w'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def  start_message(message):
    bot.send_message(message.chat.id, text = "Hi, {0.first_name}!".format(message.from_user))
    
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()
        
