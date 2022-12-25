operation = None
n1 = None
n2 = None

def show_logs():
    logs = "История операций:\n\n"
    with open("./calc/logs_calc", "r") as file:
        for i in file.readlines():
            logs += f"{i}\n"
    return logs
