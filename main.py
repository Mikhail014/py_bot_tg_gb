from telebot import types
from tic_tac_toe import data, interface

bot = data.bot

@bot.message_handler()
def dialogs(msg: types.Message):
    text_msg = msg.text

    if text_msg == "1":
        bot.register_next_step_handler(msg, interface.set_name_user1)
        bot.send_message(chat_id=msg.from_user.id, text="Добро пожаловать в игру 'Крестики и нолики'!!!\n")
        bot.send_message(chat_id=msg.from_user.id, text="Введите свое имя:")
    else:
        bot.send_message(chat_id=msg.from_user.id, text="Нажми 1, чтобы поиграть в крестиики и нолики")



bot.polling()