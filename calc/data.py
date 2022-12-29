from datetime import datetime
import os

os.chdir(os.path.dirname(__file__))
operation = None
n1 = None
n2 = None
is_complex_nums = False

def write_logs(event):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    with open("logs_calc", "a", encoding="utf-8") as file:
        file.write(f"{dt_string} --- {event}\n")

def show_logs():
    logs = "История операций:\n\n"
    with open("logs_calc", "r", encoding="utf-8") as file:
        for i in file.readlines():
            logs += f"{i}\n"
    return logs
