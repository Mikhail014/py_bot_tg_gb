from random import randint
import emoji

print("------------------------------------------------------")
print("Добро пожаловать в игру 'Крестики и нолики'!!!")
print("------------------------------------------------------")

cross = emoji.emojize(":cross_mark:")
zero = emoji.emojize(":hollow_red_circle:")
square = emoji.emojize(":green_square:")

players = []
user1 = input("Введи имя первого игрока: ")
user2 = input("Введи имя второго игрока: ")

players.append(user1 if randint(0, 9) % 2 == 0 else user2)
players.append(user2 if players[0] != user2 else user1)

print("\n---------------------------------")
print(f"Игру начинает - {players[0]}")
print("---------------------------------\n")

playing_field = [
    [1, " | ", 2, " | ", 3],
    ["---------"],
    [4, " | ", 5, " | ", 6],
    ["---------"],
    [7, " | ", 8, " | ", 9]
]

def print_array(arr):
    for row in arr:
        for i in row:
            print(i, end="")
        print()

isEnd = False
all_steps = [[], []]

winning_combs = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]

print_array(playing_field)

total_counter = 0

while not isEnd:
    for ind, pl in enumerate(players):
        turn = "X" if ind == 0 else "0"
        print(f"\n{pl}, сделай ход - '{turn}' (введи число от 1 до 9)")
        step = int(input("Ответ: "))
        while (step < 1 or step > 9) or step in (all_steps[0] + all_steps[1]):
            print("Введи другое число!")
            step = int(input("Ответ: "))
        all_steps[ind].append(step)
        for row in playing_field:
            for i, v in enumerate(row):
                if v == step:
                    row[i] = turn

        for win in winning_combs:
            count = 0
            for n in all_steps[ind]:
                if n in win:
                    count += 1
                    if count == 3:
                        isEnd = True
                        print("---------------------")
                        print(f"{players[ind]} победил!!! Поздравляем!!!")
                        print("---------------------")
                        break
            if isEnd:
                break

        print_array(playing_field)
        total_counter += 1

        if total_counter == 9 and not isEnd:
            print("-------------------")
            print("Ничья!!!")
            print("-------------------")
            isEnd = True
            break

        if isEnd:
            break
