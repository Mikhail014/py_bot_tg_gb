list_data = []
lastname = None
firstname = None
phone = None
about = None

def export_to_file(filename="contacts", mode=2):
    with open(f"./phonebook/{filename}" , "a", encoding="utf-8") as file:
        for contact in list_data:
            for key, value in contact.items():
                if mode == 1:
                    file.write(f"{value}; \n")
                elif mode == 2:
                    file.write(f"{value}; ")
                if key == "Описание":
                    file.write(f"\n")
        if mode == 2:
            file.write(f"\n")

def import_from_file(filename="contacts"):
    with open(f"./phonebook/{filename}", "r", encoding="utf-8") as file:
        data_file = file.readlines()
        imp_data = []
        for el in data_file:
            for item in el.split("; "):
                imp_data.append(item)
        imp_data = list(filter(lambda x: x != "\n", imp_data))
        for i, v in enumerate(imp_data):
            if i % 4 == 0:
                list_data.append({
                    "Фамилия": imp_data[i],
                    "Имя": imp_data[i + 1],
                    "Телефон": imp_data[i + 2],
                    "Описание": imp_data[i + 3]
                })