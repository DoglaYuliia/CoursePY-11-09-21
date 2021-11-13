# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла и возвращала содержимое файла в той же структкру, что и в файле.
# Параметр функции - имя файла.
# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.
# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.
# 4. Написать функцию сортировки по количеству слов в поле "text".
#
# Отсортировать данные из файла с помощью данных функций.

import json
import re

# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
def read_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data
filename = 'data.json'
data = read_json(filename)
print(data)


# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.

def sort_surname(data_dict):
    surname_list = data_dict["name"].split(" ")[-1]
    return surname_list

sort_by_surname = sorted(data, key=sort_surname)
print(sort_by_surname)


# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.

def sort_date_of_death(data_dict):
    year = data_dict["years"]
    years = re.findall(r'[0-9BC]+', year)
    if "BC" in years[-1]:
        return -1 * int(years[-2])
    else:
        return int(years[-1])
sort_death_date = sorted(data, key=sort_date_of_death)
print(sort_death_date)


# 4. Написать функцию сортировки по количеству слов в поле "text".

def sort_count_word(data_dict):
    count_word = len(data_dict["text"].split(" "))
    return count_word
sorted_count_word = sorted(data, key=sort_count_word)
print(sorted_count_word)
