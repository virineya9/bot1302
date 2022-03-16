import telebot
from telebot import types
token = '5209209288:AAE2TcFelXOkvp7GQKOr5Bgh9mbJxEMUe1w'
bot = telebot.TeleBot(token)
    
@bot.message_handler(commands=["button"])
    def button_message(message):
        markup= types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton("Кнопочка")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Выберите, зачем вы тут', reply_markup = markup)    
    


if __name__ == '__main__':
     bot.infinity_polling()
        

