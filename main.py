# 1 Завдання (Декілька варіантів вирішення)

# Варіант 1.0

# who_i_love = 'I love Python\n'
# print(who_i_love * 42)

# Варіант 1.1

# number = 42
# print('Завдання 1.2 рази)
# print('I love Python\n' * number)

# Варіант 1.2, замість 42 можна будь-яке число
print('I love Python\n' * 42)


# 2 Завдання

age_in_month = 12 * 26
print('Вік в місяцях:', age_in_month)
# print('Тип данних:', type(age_in_month))


# 3 Завдання

age_in_years = age_in_month/12
age_in_years = int(age_in_years)
print('Вік в роках:', age_in_years)


# 4 Завдання

# (дивний варіант)
# tx_names = 'Му name is Anton'
# tx_who = ' I`m '
# tx_years = ' years old'
# my_age = (tx_names + tx_who + age_in_years + tx_years)

# Зручний варіант
my_age = 'Му name is Anton I`m ' + str(age_in_years) + ' years old'
print(my_age)


# 5 Завдання
# Бачив в обговреннях на ютуб що змінні які не міняються -
# - під час життя проекту прийнято писати з велкиої літери

nums = 1
# result_1 = nums < 2
# result_2 = nums == 4
# result_3 = nums <= 1
# result_4 = nums > 1.5
# result_5 = nums != 5

# Більш простий варіант зробити порівняння відразу в "Прінт"
print((nums < 2, 'nums < 2'),
      (nums == 4, 'nums == 4'),
      (nums <= 1, 'nums <= 1'),
      (nums > 1.5, "nums > 1.5"),
      (nums != 5, 'nums != 5'),
      sep='\n')


# 6 Завдання

var_a = 2
var_b = 5
var_c = 6
var_d = str(var_a) + str(var_b) + str(var_c)

print('Змінна d:', var_d)
print('Тип змінної d:', type(var_d))


# etc
print()
print('Дякую за увагу^^')
