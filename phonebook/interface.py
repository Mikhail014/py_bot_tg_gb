from phonebook import operations
from phonebook import data
import data_bot

bot = data_bot.bot

def action_choice(msg):
    ans = msg.text
    if not ans.isdigit():
        bot.send_message(chat_id=msg.from_user.id, text="Введите число!")
        bot.register_next_step_handler(msg, action_choice)
        return
    else:
        ans = int(ans)

    if ans == 1:
        bot.send_message(chat_id=msg.from_user.id, text="Введите фамилию:")
        bot.register_next_step_handler(msg, set_last_name)
    elif ans == 2:
        contacts = operations.print_contacts()
        bot.send_message(chat_id=msg.from_user.id, text=contacts)
        bot.send_message(chat_id=msg.from_user.id, text="Нажми 3, если хочешь вызвать меню телефонной книги")
    elif ans == 3:
        bot.send_message(chat_id=msg.from_user.id, text="Выберите формат экспорта:\n"
                                                        "1. Данные одного пользователя на разных строках;\n"
                                                        "2. Данные одного пользователя на одной строке.")
        bot.register_next_step_handler(msg, set_format_export)
    elif ans == 4:
        data.import_from_file()
        bot.send_message(chat_id=msg.from_user.id, text=f"Данные импортированы из резервного хранилища!")
        bot.send_message(chat_id=msg.from_user.id, text="Нажми 3, если хочешь вызвать меню телефонной книги")
    else:
        bot.send_message(chat_id=msg.from_user.id, text="Введите число от 1 до 4!!!")
        bot.register_next_step_handler(msg, action_choice)

def set_format_export(msg):
    format_exp = msg.text
    if not format_exp.isdigit():
        bot.send_message(chat_id=msg.from_user.id, text="Введите число!")
        bot.register_next_step_handler(msg, set_format_export)
        return
    else:
        format_exp = int(format_exp)

    if format_exp == 1 or format_exp == 2:
        data.export_to_file(mode=format_exp)
        bot.send_message(chat_id=msg.from_user.id, text=f"Данные экспортированы в резервное хранилище!")
        bot.send_message(chat_id=msg.from_user.id, text="Нажми 3, если хочешь вызвать меню телефонной книги")
    else:
        bot.send_message(chat_id=msg.from_user.id, text="Введите число 1 или 2!!! Инструкцию смотрите выше!")
        bot.register_next_step_handler(msg, set_format_export)

def set_last_name(msg):
    data.lastname = msg.text
    bot.send_message(chat_id=msg.from_user.id, text="Введите имя:")
    bot.register_next_step_handler(msg, set_first_name)

def set_first_name(msg):
    data.firstname = msg.text
    bot.send_message(chat_id=msg.from_user.id, text="Введите номер телефона:")
    bot.register_next_step_handler(msg, set_phone_num)

def set_phone_num(msg):
    data.phone = msg.text
    bot.send_message(chat_id=msg.from_user.id, text="Введите описание контакта:")
    bot.register_next_step_handler(msg, set_about_contact)

def set_about_contact(msg):
    data.about = msg.text
    ln = data.lastname
    fn = data.firstname
    phone = data.phone
    about = data.about
    operations.add_contact(ln, fn, phone, about)
    bot.send_message(chat_id=msg.from_user.id, text=f"Контакт {ln} {fn} добавлен!")
    bot.send_message(chat_id=msg.from_user.id, text="Нажми 3, если хочешь вызвать меню телефонной книги")
