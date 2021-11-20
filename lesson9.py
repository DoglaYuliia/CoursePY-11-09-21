
# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат.
# и возвращает список оветов сервиса http://forismatic.com/ru/api/.
# Если автор не указан, цитату не брать. Цитаты не должны повторяться.
import requests
import csv

def get_raw_quote(key):
    url = "http://api.forismatic.com/api/1.0/"
    list_quotes = []
    for numb in range(key):
        params = {"method": "getQuote",
                  "format": "json",
                  "key": numb,
                  "lang": "ru"}
        r = requests.get(url, params=params)
        data = r.json()
        if data["quoteAuthor"] == "" or [data["quoteAuthor"], data["quoteText"], data["quoteLink"]] in list_quotes:
            continue
        else:
            list_quotes.append([data["quoteAuthor"], data["quoteText"], data["quoteLink"]])
    return list_quotes

quotes = get_raw_quote(10)
#print(quotes)

# 2. Написать функцию, которая принимает результат предыдущей функции и сохраняет в csv файл.
# ВАЖНО!!! -10 баллов за невыполнение этих пунктов!!!
# 1) Имя файла сделать параметром по умолчанию.
# 2) Заголовки csv файла: Author, Quote, URL.
# 3) Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).

def quote_csv(key, filename="Quotes_list.csv"):
    with open(filename, "w") as csv_file:
        writer = csv.writer(csv_file)
        heading = ["Author", "Quote", "URL"]
        quote_data = get_raw_quote(key)
        sorted_list = sorted(quote_data, key=lambda x: x[0])
        writer.writerows([heading] + sorted_list)

quote_csv(10)

