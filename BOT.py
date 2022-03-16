import telebot
from telebot import types
token = '5209209288:AAE2TcFelXOkvp7GQKOr5Bgh9mbJxEMUe1w'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, text = "Приветик, {0.first_name}!".format(message.from_user))  
    
@bot.message_handler(commands=["button"])
def button_message(message):
    markup= types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("Кнопочка")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Выберите, зачем вы тут', reply_markup = markup)    

@bot.message_handler(commands=["img"]) 
def image(message):
    bot.send_photo(message.chat.id, photo = open('kotikdlybotik.jpg,crdownload', 'rb'))     
    
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()

        

