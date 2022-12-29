import data_bot
from calc import data

bot = data_bot.bot

def set_operation(msg):
    ans = msg.text
    data.write_logs(ans)
    if not ans.isdigit():
        mess = "Введите число!"
        bot.send_message(chat_id=msg.from_user.id, text=mess)
        bot.register_next_step_handler(msg, set_operation)
        data.write_logs(mess)
        return
    else:
        ans = int(ans)

    if ans == 1:
        mess = "Выбрана операция сложения!"
        bot.send_message(chat_id=msg.from_user.id, text=mess)
        data.write_logs(mess)
    elif ans == 2:
        mess = "Выбрана операция вычитания!"
        bot.send_message(chat_id=msg.from_user.id, text=mess)
        data.write_logs(mess)
    elif ans == 3:
        mess ="Выбрана операция умножения!"
        bot.send_message(chat_id=msg.from_user.id, text=mess)
        data.write_logs(mess)
    elif ans == 4:
        mess ="Выбрана операция деления!"
        bot.send_message(chat_id=msg.from_user.id, text=mess)
        data.write_logs(mess)
    elif ans == 5:
        bot.send_message(chat_id=msg.from_user.id, text=data.show_logs())
        return
    else:
        bot.register_next_step_handler(msg, set_operation)
        bot.send_message(chat_id=msg.from_user.id, text="Введи число от 1 до 4!")
        return

    data.operation = ans
    mess = "Выберите режим работы калькулятора:\n" \
           "Клавиша 1 -> Работа с комплексными числами\n" \
           "Любая клавиша -> Работа с рациональными числами."
    bot.register_next_step_handler(msg, select_type_calc)
    bot.send_message(chat_id=msg.from_user.id, text=mess)
    data.write_logs(mess)


def select_type_calc(msg):
    ans = msg.text
    if ans == "1":
        data.is_complex_nums = True
        bot.send_message(chat_id=msg.from_user.id, text="Выбран режим работы с комплексными числами!")
    else:
        bot.send_message(chat_id=msg.from_user.id, text="Выбран режим работы с рациональными числами!")

    mess = "Введите первое число:"
    bot.register_next_step_handler(msg, enter_the_first_num)
    bot.send_message(chat_id=msg.from_user.id, text=mess)
    data.write_logs(mess)


def enter_the_first_num(msg):
    ans = msg.text
    data.write_logs(ans)
    if not ans.isdigit():
        mess = f"Ввод данного текста '{ans}' преобразовывается в число 0"
        bot.send_message(chat_id=msg.from_user.id, text=mess)
        data.n1 = 0
        data.write_logs(mess)
    else:
        data.n1 = int(ans)

    mess = "Введите второе число:"
    bot.register_next_step_handler(msg, enter_the_second_num)
    bot.send_message(chat_id=msg.from_user.id, text=mess)
    data.write_logs(mess)


def enter_the_second_num(msg):
    ans = msg.text
    data.write_logs(ans)
    if not ans.isdigit():
        mess = f"Ввод данного текста '{ans}' преобразовывается в число 0"
        bot.send_message(chat_id=msg.from_user.id, text=mess)
        data.n2 = 0
        data.write_logs(mess)
    else:
        data.n2 = int(ans)

    n1 = data.n1
    n2 = data.n2
    res = None

    if data.operation == 1:
        if data.is_complex_nums:
            res = f"{complex(n1, n2)} = z"
        else:
            res = f"{n1} + {n2} = {n1 + n2}"
        bot.send_message(chat_id=msg.from_user.id, text=res)
    elif data.operation == 2:
        if data.is_complex_nums:
            res = f"{complex(n1, n2).conjugate()} = z"
        else:
            res = f"{n1} - {n2} = {n1 - n2}"
        bot.send_message(chat_id=msg.from_user.id, text=res)
    elif data.operation == 3:
        if data.is_complex_nums:
            res = f"{n1 * n2}j = z"
        else:
            res = f"{n1} * {n2} = {n1 * n2}"
        bot.send_message(chat_id=msg.from_user.id, text=res)
    elif data.operation == 4:
        if n2 == 0:
            res = "На ноль делить нельзя!"
            bot.send_message(chat_id=msg.from_user.id, text=res)
            data.write_logs(res)
            return
        if data.is_complex_nums:
            res = f"{n1 // n2 if n1 % n2 == 0 else n1 / n2}j = z"
        else:
            res = f"{n1} / {n2} = {n1 / n2}"
        bot.send_message(chat_id=msg.from_user.id, text=res)

    bot.send_message(chat_id=msg.from_user.id, text="Нажми 2, чтобы открыть меню операций. Или нажми на любой символ,"
                                                    "кроме 1, 2 и 3, чтобы открыть главное меню.")

    data.is_complex_nums = False
    data.write_logs(res)

