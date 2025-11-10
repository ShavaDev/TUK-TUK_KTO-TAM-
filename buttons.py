from telebot import types

def main_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Сгенерировать пароль')
    kb.add(but1)
    return kb

def len_of_password():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True)
    but1 = types.KeyboardButton('6')
    but2 = types.KeyboardButton('8')
    but3 = types.KeyboardButton('10')
    but4 = types.KeyboardButton('12')
    kb.add(but1, but2, but3, but4)
    return kb
