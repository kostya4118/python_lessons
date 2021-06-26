# ЗАДАНИЕ 1

try:
    with open('my_text.txt', 'w', encoding='utf-8') as f:
        while True:
            my_str = input('Введите строку или нажмите enter для завершения: ')
            if my_str == '':
                break
            else:
                f.write(f'{my_str}\n')
except IOError:
    print('Ошибка ввода-вывода!')


# ЗАДАНИЕ 2

try:
    with open('my_text.txt', 'r', encoding='utf-8') as f:
        print(f.read())
        f.seek(0)
        lines = len(f.readlines())
        print(f'В файле содержится {lines} строк.')
        f.seek(0)
        i = 0
        for line in f:
            words = len(line.split())
            i += 1
            print(f'В строке {i} содержится {words} слов.')
except IOError:
    print('Ошибка ввода-вывода!')


# ЗАДАНИЕ 3

total_zp = 0
workers = 0
try:
    with open('zp.txt', 'r', encoding='utf-8') as f:
        print('Сотрудники с ЗП менее 20 тыс.: ')
        for line in f:
            if line != '\n':
                line = line.split()
                if float(line[1]) < 20000:
                    print(line[0])
                total_zp += float(line[1])
                workers += 1
except IOError:
    print('Ошибка ввода-вывода!')
try:
    print('Средняя зарплата:', total_zp / workers)
except ZeroDivisionError:
    print('Список работников пуст.')


# ЗАДАНИЕ 4

from os import path, remove

translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

if path.exists('nums_rus.txt'):
    remove('nums_rus.txt')

try:
    with open('nums_eng.txt', 'r', encoding='utf-8') as f1:
        for line in f1:
            line = line.split()
            line[0] = translate[line[0]]
            line = ' '.join(line)
            with open('nums_rus.txt', 'a', encoding='utf-8') as f2:
                f2.write(f'{line}\n')
except IOError:
    print('Ошибка ввода-вывода!')
except KeyError:
    print('Программа не знает перевод слова из файла!')


# ЗАДАНИЕ 5

# Лучше конечно проверять вводимые данные до записи в файл, но поскольку по условию это не просили, сделал так


try:
    with open('nums_str.txt', 'w+', encoding='utf-8') as f:
        f.write(input('Введите набор чисел, разделенных пробелами: '))
        f.seek(0)
        nums = f.read().split()
        result = sum(map(float, nums))
    print('Сумма чисел в файле:', result)
except IOError:
    print('Ошибка ввода-вывода!')
except ValueError:
    print('Можно вводить только числа!')


# ЗАДАНИЕ 6

my_dict = {}
try:
    with open('scool.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.split()
            subject = line[0][:-1]
            line.pop(0)
            hours = 0
            for i in line:
                digit = [c for c in i if c.isdigit()]
                if digit:
                    i = int(''.join(digit))
                    hours += i
            my_dict.update({subject: hours})
except IOError:
    print('Ошибка ввода-вывода!')
print(my_dict)


# ЗАДАНИЕ 7

import json

firms_res = {}
aver_profit = {}
res = [firms_res, aver_profit]
aver_prof = 0
firm_prof = 0
try:
    with open('firms.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.split()
            profit = float(line[2]) - float(line[3])
            firms_res.update({line[0]: profit})
            if profit >= 0:
                aver_prof += profit
                firm_prof += 1
except IOError:
    print('Ошибка ввода-вывода!')
aver_profit.update({'average_profit': (aver_prof / firm_prof)})

print(res)

with open('firms.json', 'w', encoding='utf-8') as f_json:
    json.dump(res, f_json)
