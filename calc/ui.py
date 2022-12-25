import data_bot
from calc import data

bot = data_bot.bot

def set_operation(msg):
    ans = msg.text
    if not ans.isdigit():
        bot.send_message(chat_id=msg.from_user.id, text="Введите число!")
        bot.register_next_step_handler(msg, set_operation)
        return
    else:
        ans = int(ans)

    if ans == 1:
        bot.send_message(chat_id=msg.from_user.id, text="Выбрана операция сложения!")
    elif ans == 2:
        bot.send_message(chat_id=msg.from_user.id, text="Выбрана операция вычитания!")
    elif ans == 3:
        bot.send_message(chat_id=msg.from_user.id, text="Выбрана операция умножения!")
    elif ans == 4:
        bot.send_message(chat_id=msg.from_user.id, text="Выбрана операция деления!")
    elif ans == 5:
        bot.send_message(chat_id=msg.from_user.id, text=data.show_logs())
        return
    else:
        bot.register_next_step_handler(msg, set_operation)
        bot.send_message(chat_id=msg.from_user.id, text="Введи число от 1 до 4!")
        return

    data.operation = ans
    bot.register_next_step_handler(msg, enter_the_first_num)
    bot.send_message(chat_id=msg.from_user.id, text="Введите первое число:")



def enter_the_first_num(msg):
    ans = msg.text
    if not ans.isdigit():
        bot.send_message(chat_id=msg.from_user.id, text=f"Ввод данного текста '{ans}' преобразовывается в число 0")
        data.n1 = 0
    else:
        data.n1 = int(ans)

    bot.register_next_step_handler(msg, enter_the_second_num)
    bot.send_message(chat_id=msg.from_user.id, text="Введите второе число:")

def enter_the_second_num(msg):
    ans = msg.text
    if not ans.isdigit():
        bot.send_message(chat_id=msg.from_user.id, text=f"Ввод данного текста '{ans}' преобразовывается в число 0")
        data.n2 = 0
    else:
        data.n2 = int(ans)

    n1 = data.n1
    n2 = data.n2
    res = None

    if data.operation == 1:
        res = f"{n1} + {n2} = {n1 + n2}"
        bot.send_message(chat_id=msg.from_user.id, text=res)
    elif data.operation == 2:
        res = f"{n1} - {n2} = {n1 - n2}"
        bot.send_message(chat_id=msg.from_user.id, text=res)
    elif data.operation == 3:
        res = f"{n1} * {n2} = {n1 * n2}"
        bot.send_message(chat_id=msg.from_user.id, text=res)
    elif data.operation == 4:
        if n2 == 0:
            bot.send_message(chat_id=msg.from_user.id, text="На ноль делить нельзя!")
            return
        res = f"{n1} / {n2} = {n1 / n2}"
        bot.send_message(chat_id=msg.from_user.id, text=res)

    with open("./calc/logs_calc", "a") as file:
        file.write(f"{res}\n")

