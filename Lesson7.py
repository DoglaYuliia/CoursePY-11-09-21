
import os
def read_file(file_names):
    with open(file_names, 'r') as txt_file:
        data = txt_file.readlines()
    return data

# #1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).

def get_domains_list(file):
    with open(file, 'r') as domains:
        domains_list = [line.replace('.', '')[:-1] for line in domains.readlines()]
        return domains_list

file_name_domains = 'domains.txt'
domains = get_domains_list(file_name_domains)
print(domains)

# #2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"
def get_surname_list(file_names):
    res_list = [surname.split('\t')[1] for surname in read_file(file_names)]
    return res_list

file_names = 'names.txt'
names = get_surname_list(file_names)
print(names)

# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date_original": date_original, "date_modified": date_modified}
# в которых date_original - это дата из строки (если есть),
# а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]
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
#разделяем даты с списки
def get_date_list(file_names):
    create_date_list = []
    for data in read_file(file_names):
        data = data.split('-')[0]
        data = data.split()
        if len(data) == 3:
            create_date_list.append(data)
    return create_date_list

#созд новые словари
def date_modified_date(file_names):
    new_date_dict = []
    for data in get_date_list(file_names):
        data_1 = data[0]
        data_1 = data_1[:-2]
        if len(data_1) == 1:
            data_1 = '0' + data_1
        new_date_dict.append({'date_original': ' '.join(data),
                       'date_modified': f'{data_1}/{months.get(data[1])}/{data[2]}'})
    return new_date_dict

file_date_authors = 'authors.txt'
modified_date = date_modified_date(file_date_authors)
print(modified_date)













