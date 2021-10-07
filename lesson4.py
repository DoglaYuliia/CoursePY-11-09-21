
###### 1 задание #######

my_list = [15, 5, 150, 132, 15, 8, 263, 252, 2, 458, 104, 56, 35, 185]
for symbol in my_list:
    if symbol > 100:
        print(symbol)

###### 2 задание #######

my_list = [15, 5, 150, 132, 15, 8, 263, 252, 2, 458, 104, 56, 35, 185]
my_results = []
for num in my_list:
    if num > 100:
        my_results.append(num)
print(my_results)

###### 3 задание #######

my_list = [15, 5, 150, 132, 15, 8, 263, 252, 2, 458, 104, 56, 35, 185]
if len(my_list) < 2:
    my_list.append(0)
    print(my_list)
else:
    my_list.append(my_list[-1] + my_list[-2])
    print(my_list)

###### 4 задание #######

my_string = '0123456789'
my_list = []
for symb_1 in my_string:
    for symb_2 in my_string:
        my_list.append(int(symb_1 + symb_2))
print(my_list)
