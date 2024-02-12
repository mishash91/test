
# 5.6
  # 5.6.1
import random

list_of_num = random.sample(range(0, 10), 10)  # список на вход
print(list_of_num)
e_max = max(list_of_num)  # максимальное значение
e_min = min(list_of_num)  # минимальное значение
index_max = list_of_num.index(e_max)  # индекс максимального значения
index_min = list_of_num.index(e_min)  # индекс минимального значения
list_of_num.pop(index_max)  # удаление максимального значения из списка
list_of_num.insert(index_max, e_min)  # добавление минимального значения в список
list_of_num.pop(index_min)  # удаление минимального значения из списка
list_of_num.insert(index_min, e_max)  # добавление максимального значения в список
print(list_of_num)

  # 5.6.2
list_of_num = [6, 2, 1, 4, 3, 7, 5, 5, 5, 5, 6, 7, 8]  # список на вход
duplicate_list = []
for i in list_of_num:
    if list_of_num.count(i) > 1 and i not in duplicate_list:
        duplicate_list.append(i)
        print(f'Элемент "{i}" встречается {list_of_num.count(i)} раз')

# второй вариант 5.6.2
list_of_num = [6, 2, 1, 4, 3, 7, 5, 5, 5, 5, 6, 7, 8]  # список на вход
for i in set(list_of_num):
    if list_of_num.count(i) > 1:
        print(f'Элемент "{i}" встречается {list_of_num.count(i)} раз')


  # 5.6.3
input_str = input('Введите строку:').split(' ')
save_key = {}
result = []
for i in input_str:
    if i not in save_key.keys():
        save_key[i] = 0
    else:
        save_key[i] += 1
    result.append(save_key[i])
print(result)

  # 5.6.4
import re

pattern_file = r'\w+\.\w+'  # паттерн для файла
operations = {'W': 'write', 'R': 'read', 'X': 'execute'}
files_operations = {'default': '#'}
results = []

steps = {1: 'введите «имя файла» и допустимые операции',
         2: 'введите операцию и имя файла'}  # по умолчанию данные вводятся в 2 этапа
for step in steps.keys():
    input_int = input('Введите число:')
    for i in range(int(input_int)):
        input_str = input(f'введите {steps.get(step)}')
        file = re.search(pattern_file, input_str).group(0)
        if step == 1:  # заводим допустимые операции
            files_operations[file] = [operations[i] for i in input_str.split() if i != file]
        elif step == 2:
            input_str = input_str.split()
            input_str.remove(file)
            input_str = input_str[0]  # по условию должна вводиться одна операция
            results.append('OK' if input_str in files_operations.get(file, files_operations['default']) else 'Denied')

print('\n'.join(results))


# 6.5
  # 6.5.1
def squere(n, m=2):
    return n ** m


def squere_r(n, m=2):
    if m == 1:
        return n
    return n * (squere_r(n, m - 1))


  # 6.5.2
count_int = 0


def squere(n, m=2):
    global count_int
    count_int += 1
    return n ** m


squere(1, 2)
squere(2, 2)
squere(3, 2)
print(f'кол-во запусков {count_int}')

    # 6.5.3
list_prod = ['Бананы', 'Яблоки', 'Макароны', 'Кофе']
count_int = 0


def print_string(string):
    global count_int
    count_int += 1
    print(f'{count_int}) {string}')


def printGroceries(*args):
    for i in args:
        if i in list_prod:
            print_string(i)
    if count_int == 0:
        print('Нет продуктов')


def input_str(string):
    eval(string)


input_str(input())
#  printGroceries('Бананы', [1, 2], ('Python',), 'Яблоки', '', 'Макароны', 5, True, 'Кофе', False)
#  printGroceries([4], {}, 1, 2, {'Mathlab'}, '')


# 7.6
    # 7.6.1

import re

def show_letters(some_str):
    b = r'[a-zA-z]'
    for i in some_str:
        if re.match(b, i):
            yield i

print(list(show_letters('sssfsfsd1213341')))

    # 7.6.2
def i_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return i_fib(n - 1) + i_fib(n - 2)


def fib(n):
    #return [fib(i) for i in range(1, n+1)]
    for x in range(1, n + 1):
        yield i_fib(x)


    # 7.6.3
dic_list = [
     {"code": "CSE-401", "name": "Multimedia", "Credit": 2.0},
     {"code": "CSE-101", "name": "Computer Fundamental", "Credit": 1.5},
     {"code": "CSE-305", "name": "Unix Programming", "Credit": 3.0}
]

input_key = 'Credit' #input()
dic_list.sort(key=lambda x: x.get(input_key), reverse=True)
print(dic_list)

    # 7.6.4
import re
chars = ['a', 'e', 'y', 'u', 'i', 'o']  # гласные


def calc_char(string, char=chars):
    pattern = r'[a-zA-Z]'
    input_str = re.findall(pattern, string)
    return [x for x in input_str if x.lower() in char]

result = (lambda x: len(calc_char(x))) (input('введите строку'))

print(f'кол-во гласных букв = {result}')


# 7.6.5
def reseved_list(in_list):
    return [x[::-1] for x in in_list]

result = (lambda x: reseved_list(x)) (input('введите строку').split())

print(' '.join(result))
