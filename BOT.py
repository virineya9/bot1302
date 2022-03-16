import telebot
from telebot import types
token = '5209209288:AAE2TcFelXOkvp7GQKOr5Bgh9mbJxEMUe1w'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, text = "Приветик, {0.first_name}!, я тестовый БОТ".format(message.from_user))  
    
@bot.message_handler(commands=["button"])
def button_message(message):
    markup= types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("Получить мем с котиком")
    item2 = types.KeyboardButton("Узнать, на что способен, Великий БОТ")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Выберите, зачем вы тут', reply_markup = markup)    

@bot.message_handler(content_types=["text"])
def message_reply(message):
    if message.text == "Получить мем с котиком":
        bot.send_photo(message.chat.id, photo = open('p.jpg', 'rb'))   

@bot.message_handler(content_types=["text"])
def message_reply(message):
    if message.text == "Узнать, на что способен, Великий БОТ":
        bot.send_message(message.chat.id, 'Я могу отправить мем с котиком.', reply_markup = markup)           
    
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()

        

