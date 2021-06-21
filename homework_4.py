# ЗАДАНИЕ 1

# -*- coding: utf-8 -*-

from sys import argv

def zp(hours, rate, prize):
    res = (hours * rate) + prize
    return res

try:
    hours, rate, prize = map(int, argv[1:4])
    print(zp(hours, rate, prize))
except ValueError:
    print('Введены неверные параметры! Введите выработку в часах, ставку в час и премию через пробел')


# ЗАДАНИЕ 2

li = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

res = [li[i] for i in range(1, len(li)) if li[i] > li[i - 1]]

print(res)


# ЗАДАНИЕ 3

li = [el for el in range(20, 240 + 1) if el % 20 == 0 or el % 21 == 0]

print(li)


# ЗАДАНИЕ 4

li = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 1]

res = [el for el in li if li.count(el) == 1]

print(res)


# ЗАДАНИЕ 5

from functools import reduce

li = [el for el in range(100, 1000 + 1) if el % 2 == 0]

def mult(el, next_el):
    return el * next_el

print(reduce(mult, li))


# ЗАДАНИЕ 6

# -*- coding: utf-8 -*-

from sys import argv
from itertools import count

try:
    li = []
    for el in count(int(argv[1])):
        if el > 15:
            break
        else:
            li.append(el)

    print(li)
except IndexError:
    print('Введите начальное значение через пробел после названия скрипта')
except ValueError:
    print('Введите числовое значение параметра')


# -*- coding: utf-8 -*-

from sys import argv
from itertools import cycle

def my_cycle(li):
    i = 1
    for el in cycle(li):
        if i > 15:
            break
        print(el)
        i += 1
try:
    if argv[1]:
        my_cycle(argv[1:])
except IndexError:
    li = input('Введите элементы некоторого списка через пробел: ').split()
    my_cycle(li)


# ЗАДАНИЕ 7

# -*- coding: utf-8 -*-
from sys import argv

try:
    if argv[1]:
        num = int(argv[1])
except IndexError:
    num = int(input('Факториал какого числа необходимо вычислить? '))


def fact(x):
    res = 1
    for i in range(1, x + 1):
        res *= i
        yield res


if num > 0:
    for ind, el in enumerate(fact(num), 1):
        print(f'!{ind} = {el}')
elif num == 0:
    print(f'!{num} = 1')
else:
    print('Факториал отрицательного числа не вычисляется!')
