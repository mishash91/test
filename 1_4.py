
# 1.6
input()
input_int = input('Введите трехзначное число:')
print(f'Первая цифра числа = {input_int[0]}')
print(f'Вторая цифра числа = {input_int[1]}')
print(f'Третья цифра числа = {input_int[2]}')
print(f'Сумма всех чисел = {sum(int(x) for x in input_int)}')

# 2.4
# 2.4.1
input_int = input('Введите число от −999 до 999:')
if input_int.replace('-', '').isdigit():
    input_int = abs(int(input_int))
    x = 1  # степень
    for x in range(0, 10):
        if input_int < 10 ** x:
            print(f'Кол-во разрядов = {x}')
            break
else:
    print(f'Введенные данные неверны: {input_int}')

# второй вариант 2.4.1
input_int = input('Введите число от −999 до 999:').replace('-', '')
if input_int.isdigit():
    print(f'Кол-во разрядов = {len(input_int)}')
else:
    print(f'Введенные данные неверны: {input_int}')

    # 2.4.2
input_int = input('Введите трехзначное число:')

if input_int.replace('-', '').isdigit() and 100 <= int(input_int) < 1000:
    if int(input_int[0]) < int(input_int[1]) < int(input_int[2]):
        print('Да')
    else:
        print('Нет')
else:
    print(f'Введенные данные неверны: {input_int}')

    # 2.4.3
input_int = input('Введите четырехразрядное число:')
if input_int.replace('-', '').isdigit() and 1000 <= int(input_int) < 10000:
    if input_int == input_int[::-1]:
        print('Да')
    else:
        print('Нет')
else:
    print(f'Введенные данные неверны: {input_int}')

# 3.5
# 3.5.1
input_int = input('Введите целое число:')
if input_int.replace('-', '').isdigit():
    input_int = abs(int(input_int))
    q_col = 10  # кол-во столбцов
    q_str = 20  # кол-во строк
    for i in range(1, q_str * q_col + 1, 1):
        if i % q_col == 0:
            print(input_int * i, end='\n')
        else:
            print(input_int * i, end=' ')
else:
    print(f'Введенные данные неверны: {input_int}')

    # 3.5.2
input_int = input('Введите число задающее высоту пирамиды:')
if input_int.replace('-', '').isdigit():
    input_int = abs(int(input_int))
    len_str = input_int * 2 - 1  # длина строки
    for i in range(1, input_int * 2 + 1, 2):
        symbol = (len_str - i) // 2 * ' '  # кол-во пробелов слева и справа
        print(symbol, i * 'X', symbol, sep='')
else:
    print(f'Введенные данные неверны: {input_int}')

    # 3.5.3
guest = int(input('Введите кол-во гостей:'))
chair = int(input('Введите кол-во гостей:'))
res = 1
if guest >= chair:
    for i in range(0, chair, 1):
        res *= guest
        guest -= 1
else:
    print('число гостей не должно быть меньше числа мест')
print(res)

# 3.5.4
first_sum = float(input('Введите начальный вклад:'))
q_year = int(input('Введите число лет:'))
rate = float(input('Введите процентную ставку:'))
res = 0
for i in range(1, q_year + 1):
    res += (first_sum + res) * (rate / 100)
print(f'Через {q_year} лет вы получите {res + first_sum:.2f}')

# 3.5.5

first_sum = int(input('Введите начальный вклад:'))
amount = float(input('Введите желаемую сумму:'))
rate = float(input('Введите процентную ставку:'))
res = 0
q_year = 0
while True:
    if first_sum + res >= amount:
        break
    else:
        res += (first_sum + res) * (rate / 100)
        q_year += 1
print(f'{amount:.2f} вы получите через {q_year} лет')

# 4.6
# 4.6.1
input_str = input('Введите строку:')
print(f'Перевернутая строка: {input_str[::-1].capitalize()}')

# 4.6.2
import random

sep = ' '
input_str = input('Введите строку:').split(sep)
random.shuffle(input_str)
print(f'Перевернутая строка: {sep.join(input_str).capitalize()}')

# 4.6.3
import re

pattern = r'\W(\d+)\W\w*\W(\w{1,2}\W\w+)\W\w{1}\W(\d{1,2}.\d{1,2}.\d{1,2}).+\W(\d{1,2}.\d{1,2}.\d{1,2})'

journal = '''Рейс 365 прибыл из Сасово в 12:56:30 сообщение получено в 12:57:20 Сохранено в базу данных
Рейс 452 отправился в Сочи в 13:04:22 сообщение получено в 13:11:32 Ошибка записи в базу данных
Рейс 13 уехал в Москву в 1:15:08 сообщение получено в 1:18:33 Сохранено в базу данных'''

res_print = '[{0}] - Поезд № {1} {2}'
for i in journal.split('\n'):
    str_pattern = re.search(pattern, i)
    if str_pattern:
        time = str_pattern.group(3) if len(str_pattern.group(3)) == 8 else ('0' + str_pattern.group(4))[:8]
        print(res_print.format(time, str_pattern.group(1), str_pattern.group(2)))
    else:
        print(f'строка не подошла по шаблону - {i}')
