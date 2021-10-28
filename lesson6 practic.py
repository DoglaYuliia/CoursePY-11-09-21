# #1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# # а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых.
# # б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# # в) Посчитать среднее количество лет всех людей из списка.
# # Это одно задание. При выполнении пунктов можно использовать объекты полученные в предыдущих пунктах.
#
# persons = [
#     {"name": "John", "age": 15},
#     {"name": "Michael", "age": 17},
#     {"name": "Adam", "age": 42},
#     {"name": "John", "age": 18},
#     {"name": "Lina", "age": 32},
#     {"name": "Aaron", "age": 25},
#     {"name": "Noa", "age": 15},
#     {"name": "Jack", "age": 55}
# ]
#
# min_age_name = 1500
# max_long_name = 0
# sum_age = 0
#
# # а) Напечатать имя самого молодого человека
#
# for key_name in persons:
#     if key_name["age"] < min_age_name:
#         min_age_name = key_name["age"]
#
# for key_name in persons:
#     if key_name["age"] == min_age_name:
#         print(key_name["name"])
#
# # б) Напечатать самое длинное имя
# for key_name in persons:
#     if len(key_name["name"]) > max_long_name:
#         max_long_name = len(key_name["name"])
#
# for key_name in persons:
#     if len(key_name["name"]) == max_long_name:
#         print(key_name["name"])
#
# #в) Посчитать среднее количество лет всех людей из списка
# for key_name in persons:
#     sum_age += key_name["age"]
# middle_age = sum_age/len(persons)
# print(middle_age)


# 2) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
# Это одно задание. При выполнении пунктов можно использовать объекты полученные в предыдущих пунктах.

my_dict_1 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
my_dict_2 = {'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'one': 5, 'ten': 10, 'five': 6}

# а) Создать список из ключей, которые есть в обоих словарях.
my_list_key = set(my_dict_1.keys()).intersection(set(my_dict_2.keys()))
print(my_list_key)

# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
set_keys = list(set(my_dict_1.keys()) - set(my_dict_2.keys()))
print(set_keys)

# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
my_dict_3 = {}
for item in my_dict_1.items():
    if item[0] not in my_dict_2:
        my_dict_3[item[0]] = item[1]
print(my_dict_3)

# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

my_dict3 = {}
key_1_list = set(my_dict_1.keys())-(set(my_dict_2.keys()))
for key_1 in key_1_list:
    my_dict3[key_1] = my_dict_1[key_1]

key_2_list = set(my_dict_2.keys())-(set(my_dict_1.keys()))
for key_2 in key_2_list:
    my_dict3[key_2] = my_dict_2[key_2]

keys_2_list = set(my_dict_1.keys()).intersection(set(my_dict_2.keys()))
for key_12 in keys_2_list:
    my_dict3[key_12] = [my_dict_1[key_12], my_dict_2[key_12]]

print(my_dict3)

# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержатся
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.

# my_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
# # def my_function(my_list):
# #     new_list = []
# #     for index in range(len(my_list)):
# #         if index % 2:
# #             new_list.append(my_list[index][::-1])
# #         else:
# #             new_list.append(my_list[index])
# #     return new_list
# # new_list = my_function(my_list)
# # print(new_list)
#
#
# def my_function(my_list):
#     new_list = [my_list[index][::-1] if index % 2 else my_list[index] for index in range(len(my_list))]
#     return new_list
# print(my_function(my_list))

# my_list = ["this", "is", "the", "list", "from", "strings"]
# def first_function(some_list):
#     result_list = [some_list[i][::-1] if i % 2 else some_list[i] for i in range(len(some_list))]
#     return result_list
# print(first_function(my_list))

# 4.Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.случайное_число_от_100_до_999@строка_случайных_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
#
# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com
# 
# import random
# import string
# 
# def create_email(domains, names):
#     return random.choice(names)\
#            + "." + str(random.randint(100, 1000))\
#            + "@"\
#            + "".join(random.choice(string.ascii_lowercase) for i in range(random.randint(5, 7)))\
#            + "."\
#            + random.choice(domains)
# 
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)

# 4.Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.случайное_число_от_100_до_999@строка_случайных_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
#
# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com

import random
import string

def create_email(domains, names):
    return random.choice(names)\
           + "." + str(random.randint(100, 1000))\
           + "@"\
           + "".join(random.choice(string.ascii_lowercase) for i in range(random.randint(5, 7)))\
           + "."\
           + random.choice(domains)

names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names)
print(e_mail)

names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]

