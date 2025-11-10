import random as rd
import telebot
import buttons


symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
length = [6, 8, 10, 12]

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Добро пожаловать!\n'
                              'Я — бот-генератор паролей 🔐')
    bot.send_message(user_id, 'Выберите пункт меню:',
                     reply_markup=buttons.main_menu())
    bot.register_next_step_handler(message, choose_length)

def choose_length(message):
    user_id = message.from_user.id
    if message.text == 'Сгенерировать пароль':
        bot.send_message(user_id, 'Давайте сгенерируем вам пароль!',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(user_id, 'Укажите длину вашего пароля:',
                         reply_markup=buttons.len_of_password())
        bot.register_next_step_handler(message, send_psw)
    else:
        bot.send_message(user_id, '👀👀👀',
                         reply_markup=buttons.main_menu())
        bot.register_next_step_handler(message, choose_length)

def send_psw(message):
    user_id = message.from_user.id
    user_text = message.text
    try:
        user_length = int(user_text)
    except ValueError:
        bot.send_message(user_id, 'Введите число! 🔢')
        bot.send_message(user_id, 'Выберите длину:',
                         reply_markup=buttons.len_of_password())
        bot.register_next_step_handler(message, send_psw)
        return
    if user_length in length:
        password = ''.join(rd.sample(symbols, user_length))
        bot.send_message(user_id, f'Вот ваш пароль:\n{password}')
        bot.send_message(user_id, 'Хотите сгенерировать ещё пароль?',
                         reply_markup=buttons.main_menu())
        bot.register_next_step_handler(message, choose_length)
    else:
        bot.send_message(user_id, 'Выберите один из предложенных вариантов!',
                         reply_markup=buttons.len_of_password())
        bot.send_message(user_id, 'Попробуйте снова:')
        bot.register_next_step_handler(message, send_psw)


bot.polling(none_stop=True)


