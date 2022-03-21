import telebot
from telebot import types
token = '5209209288:AAE2TcFelXOkvp7GQKOr5Bgh9mbJxEMUe1w'
bot = telebot.TeleBot(token)

    
@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, text = "Ты заблудился ночью в лесу. Долго ходил-бродил и искал выход из леса, но ТУТ ты увидел жутко темный, жутко подозрительный и жутко жуткий замок.".format(message.from_user))  
    
@bot.message_handler(commands=["button"])
def button_message(message):
    markup= types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("Войти в замок, я же не трус.")
    item2 = types.KeyboardButton("Поступить разумно и дальше искать выход из леса.")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Как поступишь?', reply_markup = markup)    

@bot.message_handler(content_types=["text"])
def message_reply(message):
    if message.text == "Войти в замок, я же не трус.":
         #bot.send_message(message.chat.id, 'Я могу отправить мем с котиком.', reply_markup = markup)  
         

@bot.message_handler(content_types=["text"])
def message_reply(message):
    if message.text == "Поступить разумно и дальше искать выход из леса.":
        bot.send_message(message.chat.id, 'Удачи с этим.', reply_markup = markup)           
    
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()

        

