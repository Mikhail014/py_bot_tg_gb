from telebot import types
from tic_tac_toe import interface
from calc import ui
import data_bot
from phonebook import interface as ui_note
from phonebook import data as data_phonebook

bot = data_bot.bot
data_phonebook.import_from_file("save_contacts")

@bot.message_handler()
def dialogs(msg: types.Message):
    text_msg = msg.text

    if text_msg == "1":
        bot.register_next_step_handler(msg, interface.set_name_user1)
        bot.send_message(chat_id=msg.from_user.id, text="Добро пожаловать в игру 'Крестики и нолики'!!!\n")
        bot.send_message(chat_id=msg.from_user.id, text="Введите свое имя:")
    elif text_msg == "2":
        bot.send_message(chat_id=msg.from_user.id, text="Это калькулятор!")
        bot.send_message(chat_id=msg.from_user.id, text="Введи число от 1 до 4, чтобы выбрать операцию:\n"
                                                        "1. Сложение;\n"
                                                        "2. Вычитание;\n"
                                                        "3. Умножение;\n"
                                                        "4. Деление;\n"
                                                        "5. Посмотреть историю совершенных операций.")
        bot.register_next_step_handler(msg, ui.set_operation)
    elif text_msg == "3":
        bot.send_message(chat_id=msg.from_user.id, text="Телефонная книга!")
        bot.send_message(chat_id=msg.from_user.id, text="Выберите действие:\n"
                                                        "1. Добавить запись;\n"
                                                        "2. Вывод записей на экран;\n"
                                                        "3. Экспорт записей;\n"
                                                        "4. Импорт записей.")
        bot.register_next_step_handler(msg, ui_note.action_choice)
    else:
        bot.send_message(chat_id=msg.from_user.id, text="Нажми 1, чтобы поиграть в крестики и нолики\n"
                                                        "Нажми 2, чтобы активировать функцию калькулятора\n"
                                                        "Нажми 3, чтобы перейти в телефонную книжку")



bot.polling()