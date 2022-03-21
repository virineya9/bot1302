import telebot
from telebot import types
token = '5209209288:AAE2TcFelXOkvp7GQKOr5Bgh9mbJxEMUe1w'
bot = telebot.TeleBot(token)

    
@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, text = "Ты заблудился ночью в лесу. Долго ходил-бродил и искал выход из леса, но ТУТ ты увидел жутко темный, жутко подозрительный и жутко жуткий замок.")  
    
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
        markup= types.ReplyKeyboardMarkup(resize_keyboard = True)
        b1 = types.KeyboardButton("Темный и страшный, с ножницами в лапках")
        b2 = types.KeyboardButton("Белый и пушистый, с колбасой")
        markup.add(b1)
        markup.add(b2)
        bot.send_message(message.chat.id, 'Перед тобой две двери, на одной из них нарисован темный и страшный кот, который держит в руках ножницы, а на другой белый и пушистый котик, в руках которого колбаса. В какую дверь пойдешь?', reply_markup = markup)  
         

@bot.message_handler(content_types=["text"])
def message_reply(message):
    if message.text == "Поступить разумно и дальше искать выход из леса.":
        bot.send_message(message.chat.id, 'Удачи с этим.')           

if __name__ == '__main__':
     bot.infinity_polling()

        

