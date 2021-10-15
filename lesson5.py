######### 1 #########

number = 10520305200
numb_zero = str(number)
numb_zero = str(numb_zero.count('0'))
print(numb_zero)

######### 2 #########

number = 5076070000
count_zero = 0
while number % 10 == 0:
    count_zero += 1
    number //= 10
print(count_zero)

# number = 202020000
# n_zero= len(str(number)) - len(str(int(str(number)[::-1])))
# print(n_zero)

######### 3 #########

my_str = '43 больше чем 34 но меньше чем 56'
k = 0
for num in my_str.split():
    if num.isdigit():
        k += int(num)
print(k)

# sum(int(numb) for numb in my_str.split() if numb.isdigit())

######### 4 #########

my_str = 'My long string'
l_limit = 'o'
r_limit = 'g'
index1 = my_str.find(l_limit)
index2 = my_str.rfind(r_limit)
part_of_str = my_str[index1+1:index2]
print(part_of_str)

# my_str[my_str.find(l_limit)+1 : my_str.rfind(r_limit)]

######### 5 #########

my_list = ['азбука', 'буква', 'алфавит', 'цифра', 'слово', 'букварь', 'арифметика']
new_list = []
for word in my_list:
    if 'а' in word[0]:
        new_list.append(word)
print(new_list)

# new_list = [new_list for new_list in my_list if 'а' in new_list[0]]

######### 6 #########

my_list = ['азбука', 'буква', 'алфавит', 'олово', 'цифра', 'слово', 'букварь', 'арифметика']
new_list = []
for word in my_list:
    if 'а' in word:
        new_list.append(word)
print(new_list)

# new_list = [new_list for new_list in my_list if 'а' in new_list]

######### 7 #########

my_list = [12, 2, '45', 3, '24', 8, '8', 7, '14', '6', '8', '321', 51]
new_list = []
for symbol in my_list:
    if symbol is str(symbol):
        new_list.append(symbol)
print(new_list)

######### 8 #########

my_str = 'этот символ встречается в строк только один раз'
my_list = []
for symbol in my_str:
    if my_str.count(symbol) == 1:
        my_list.append(symbol)
print(my_list)

######### 9 #########

my_str_1 = 'состояние'
my_str_2 = 'сословие'
my_list = []
for symbol in my_str_1:
    for symbol1 in my_str_2:
        if symbol == symbol1:
            my_list.append(symbol)
print(list(set(my_list)))

######### 10 #########

my_str_1 = 'zzzqxxxwccce'
my_str_2 = 'vvvqbbbwnnne'
my_list = []
for symbol in my_str_1:
        if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
            my_list.append(symbol)
print(my_list)

######### 11 #########

my_str = 'tjcyjgbdfthkhngcyjd'
my_list = []
for ind in range(0, len(my_str), 2):
    if ind % 2 == 0:
        symb = my_str[ind:ind+2]
        if len(symb) > 1:
            my_list.append(symb)
        else:
            my_list.append(symb + '_')
print(my_list)

