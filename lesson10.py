# Задание 1.
# Реализовать задание ДЗ № 6 (https://github.com/30nt/IntroPython_11_09_2021/blob/main/HW/lasson6.txt)
# в виде одного класса с методами, реализующими условия ДЗ.
# Можно и нужно пользоваться своим кодом, который вы уже сдали, модифицируя его под конкретный класс.

class FileReader:
    def __init__(self, filename):
        self.filename = filename
        self.lines = self.read_file()

    def read_file(self):
        with open(self.filename, "r") as file:
            return file.read().split("\n")

    def get_domains(self):
        self.lines = [line.replace(".", "") for line in self.lines]
        return self.lines

    def get_names(self):
        self.lines = [line.split("\t")[1] for line in self.lines]
        return self.lines

    months = {'January': '01',
               'February': '02',
               'March': '03',
               'April': '04',
               'May': '05',
               'June': '06',
               'July': '07',
               'August': '08',
               'September': '09',
               'October': '10',
               'November': '11',
               'December': '12'}

    def create_split_date_list(self):
        date_list = []
        for data in self.lines:
            data = data.split("-")[0]
            data = data.split()
            if len(data) == 3:
                date_list.append(data)
        return date_list

    def create_res_list(self):
        date_list = []
        for data in self.create_split_date_list():
            data_dd = data[0]
            data_dd = data_dd[:-2]
            if len(data_dd) == 1:
                data_dd = "0" + data_dd
            date_list.append({"date_original": " ".join(data),
                           "date_modified": f"{data_dd}/{self.months.get(data[1])}/{data[2]}"})
        return date_list

# Задание 2.
# В компьютерной игре есть юниты (персонажи).
# Каждый юнит имеет такие характеристики:
# имя
# клан
# здоровье    (int от 1 до 100. Начальное значение 100)
# сила        (int от 1 до 10. Начальное значение 1)
# ловкость    (int от 1 до 10. Начальное значение 1)
# интелект    (int от 1 до 10. Начальное значение 1)
#
# Каждый юнит может лечиться (увеличить свое здоровье на 10 пунктов, максимум 100) - написать метод увеличения здоровья.
# Юнит может учеличить навык силы, ловкости и интелекта на 1 балл. Возможный максимум 10.
#
# Реализовать класс Unit, с нужным функционалом.

class Unit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = 100
        self.force = 1
        self.dexterity = 1
        self.intellect = 1

#здоровье
    def health_up(self):
        if self.health < 90:
            self.health += 10

#сила
    def force_up(self):
        if self.force < 10:
            self.force += 1

# ловкость
    def dexterity_up(self):
        if self.dexterity < 10:
            self.dexterity += 1

# интелект
    def intelligence_up(self):
        if self.intellect < 10:
            self.intellect += 1