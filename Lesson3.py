# 1 задание ######################################

value = int(input("Введите целое число: "))
#print(value, type(value))
new_value = value/2 if value < 100 else str(-value)
# если имелось ввиду обратное число, тогда строка 8 будет: new_value = value/2 if value < 100 else str(value)[::-1]
print(new_value)

# 2 задание ######################################

value = 105
new_value = 0 if value < 100 else 1
print(new_value)

# 3 задание ######################################

value = 101
new_value = True if value < 100 else False
print(new_value)

# 4 задание ######################################

my_str = 'I Love This Course'
print(my_str.upper())

# 5 задание ######################################

my_str = 'I Love This Course'
print(my_str.lower())

# 6 задание ######################################

my_str = 'Concatenation'
if len(my_str) > 5:
 print((my_str) + 'qwer')
else:
 print(my_str)

# 7 задание ######################################

my_str = 'Cont'
if len(my_str) < 5:
 print((my_str) [::-1])
else:
 print(my_str)