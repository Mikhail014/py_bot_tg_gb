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


# def player_turn(msg):
#     bot.register_next_step_handler(msg, check_turn)
#     if data.ind == 1:
#         data.ind = 0
#         data.turn = data.cross
#     else:
#         data.ind = 1
#         data.turn = data.zero
#
#     pl = data.players[data.ind]
#
#


def check_turn(msg):
    ans = msg.text
    if not ans.isdigit():
        bot.register_next_step_handler(msg, check_turn)
        bot.send_message(chat_id=msg.from_user.id, text="Введи число!")
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

# # while not isEnd:
# #     for ind, pl in enumerate(players):
# #         turn = "X" if ind == 0 else "0"
# #         print(f"\n{pl}, сделай ход - '{turn}' (введи число от 1 до 9)")
# #         step = int(input("Ответ: "))
# #         while (step < 1 or step > 9) or step in (all_steps[0] + all_steps[1]):
# #             print("Введи другое число!")
# #             step = int(input("Ответ: "))
# #         all_steps[ind].append(step)
# #         for row in playing_field:
# #             for i, v in enumerate(row):
# #                 if v == step:
# #                     row[i] = turn
# #
# #         for win in winning_combs:
# #             count = 0
# #             for n in all_steps[ind]:
# #                 if n in win:
# #                     count += 1
# #                     if count == 3:
# #                         isEnd = True
# #                         print("---------------------")
# #                         print(f"{players[ind]} победил!!! Поздравляем!!!")
# #                         print("---------------------")
# #                         break
# #             if isEnd:
# #                 break
# #
# #         print_array(playing_field)
# #         total_counter += 1
# #
# #         if total_counter == 9 and not isEnd:
# #             print("-------------------")
# #             print("Ничья!!!")
# #             print("-------------------")
# #             isEnd = True
# #             break
# #
# #         if isEnd:
# #             break
