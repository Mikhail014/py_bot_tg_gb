from random import randint
from tic_tac_toe import data


bot = data.bot


def set_name_user1(msg):
    bot.register_next_step_handler(msg, set_name_user2)
    data.user1 = msg.text
    bot.send_message(chat_id=msg.from_user.id, text="Введите имя соперника:")


def set_name_user2(msg):
    bot.register_next_step_handler(msg, check_turn)
    data.user2 = msg.text
    bot.send_message(chat_id=msg.from_user.id, text=f"Играют {data.user1} против {data.user2}")

    data.players.append(data.user1 if randint(0, 9) % 2 == 0 else data.user2)
    data.players.append(data.user2 if data.players[0] != data.user2 else data.user1)

    bot.send_message(chat_id=msg.from_user.id, text=f"Игру начинает - {data.players[0]}")
    bot.send_message(chat_id=msg.from_user.id, text=update_field(data.playing_field))

    pl = data.players[0]
    bot.send_message(chat_id=msg.from_user.id, text=f"\n{pl}, сделай ход - '{data.turn}' (введи число от 1 до 9)")



def update_field(arr):
    field = ""
    for row in arr:
        for i in row:
            field += str(i)
        field += "\n"
    return field


def check_turn(msg):
    ans = msg.text
    if not ans.isdigit():
        bot.register_next_step_handler(msg, check_turn)
        bot.send_message(chat_id=msg.from_user.id, text="Введи число!")
        return
    else:
        ans = int(ans)

    if (ans < 1 or ans > 9) or ans in (data.all_steps[0] + data.all_steps[1]):
        bot.register_next_step_handler(msg, check_turn)
        bot.send_message(chat_id=msg.from_user.id, text="Введи число от 1 до 9! Ходить на уже занятые позиции нельзя!")
    else:
        data.all_steps[data.ind].append(ans)
        for row in data.playing_field:
            for i, v in enumerate(row):
                if v == ans:
                    row[i] = data.turn

        for win in data.winning_combs:
            count = 0
            for n in data.all_steps[data.ind]:
                if n in win:
                    count += 1
                    if count == 3:
                        bot.send_message(chat_id=msg.from_user.id, text=f"Игрок {data.players[data.ind]} победил!!! Поздравляем!!!")
                        bot.send_message(chat_id=msg.from_user.id, text=update_field(data.playing_field))
                        reset_game()
                        return

        data.total_counter += 1

        if data.total_counter == 9:
            bot.send_message(chat_id=msg.from_user.id, text="Ничья")
            bot.send_message(chat_id=msg.from_user.id, text=update_field(data.playing_field))
            reset_game()
            return

        bot.register_next_step_handler(msg, check_turn)
        bot.send_message(chat_id=msg.from_user.id, text=update_field(data.playing_field))

        if data.ind == 1:
            data.ind = 0
            data.turn = data.cross
        else:
            data.ind = 1
            data.turn = data.zero

        pl = data.players[data.ind]
        bot.send_message(chat_id=msg.from_user.id, text=f"\n{pl}, сделай ход - '{data.turn}' (введи число от 1 до 9)")


def reset_game():
    data.players.clear()
    data.ind = 0
    data.playing_field = [
        [1, " | ", 2, " | ", 3],
        ["-------------"],
        [4, " | ", 5, " | ", 6],
        ["-------------"],
        [7, " | ", 8, " | ", 9]
    ]
    data.all_steps = [[], []]
    data.total_counter = 0
