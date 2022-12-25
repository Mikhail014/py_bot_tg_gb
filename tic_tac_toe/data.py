from telebot import TeleBot
import emoji

bot = TeleBot("5872986648:AAED0rgZ68Q8UO17B-z9HAGoINkJNGo7zPo")

cross = emoji.emojize(":cross_mark:")
zero = emoji.emojize(":hollow_red_circle:")
square = emoji.emojize(":green_square:")

players = []
ind = 0
user1 = None
user2 = None
turn = cross

playing_field = [
    [1, " | ", 2, " | ", 3],
    ["-------------"],
    [4, " | ", 5, " | ", 6],
    ["-------------"],
    [7, " | ", 8, " | ", 9]
]



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

total_counter = 0

