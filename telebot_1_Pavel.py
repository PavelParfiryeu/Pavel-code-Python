import telebot
from telebot import types # для кнопочек
TOKEN = '5452456287:AAEQbBFE0AHgC29cJJkY5HW68yJ8s4Mdx8w'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    mt = f'Hi, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mt, parse_mode='html')
    #print(message)

'''
@bot.message_handler(commands=['message'])
def get_message(message):
    mt = f'{message}'
    bot.send_message(message.chat.id, mt)
    print(message)
'''
'''
@bot.message_handler()
def get_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Здравствуй человек!')
    elif message.text == 'Как дела':
        bot.send_message(message.chat.id, 'Я бот, всегда без изменений')
    elif message.text == 'ID':
        mes = f'{message.from_user.id}'
        bot.send_message(message.chat.id, mes)
    elif message.text == 'картинку':
        photo = open('1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю!')

'''
@bot.message_handler(content_types=['photo'])

def get_p(message):
    bot.send_message(message.chat.id, 'Вы отправили картинку')

@bot.message_handler(commands=['link'])

def link_site(massege):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://pypi.org/project/pyTelegramBotAPI/'))
    bot.send_message(massege.chat.id, 'Документация к боту', reply_markup=markup)

@bot.message_handler(commands=['helper'])

def helper(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    link = types.KeyboardButton('ссылка')
    start = types.KeyboardButton('приветствие')
    markup.add(link, start)
    bot.send_message(message.chat.id, 'Инфа', reply_markup=markup)


bot.polling(none_stop=True)

