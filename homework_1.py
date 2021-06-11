# ЗАДАНИЕ 1

a = 8
print(a)
print(type(a))

b = 'hi'
print(b)
print(type(b))

c = str(a) + b
print(c)
print(type(c))

b = '14'
c = a + int(b)
print(c)
print(type(c))

a = int(input('Введите целое число: '))
print(a)
print(type(a))

b = float(input('Введите число: '))
print(b)
print(type(b))

c = a * b
print(c)
print(type(c))

d = input('Введите строку:')
print(f'Ваша строкаа -- {d}')
print(f'Тип строки -- {type(d)}')

# ЗАДАНИЕ 2

time = int(input('Введите время в секундах: '))

hours = time // 3600
minutes = (time % 3600) // 60  # minutes = (time - hours * 3600) // 60
seconds = time % 60  # seconds = time - hours * 3600 - minutes * 60

print(f'Время в формате чч:мм:сс - {hours}:{minutes}:{seconds}')

# ЗАДАНИЕ 3

n = input('Введите число: ')

result = int(n) + int(n + n) + int(n + n + n)

print(f'Сумма чисел {n} + {n + n} + {n + n + n} =', result)

# ЗАДАНИЕ 4

number = int(input('Введите число: '))
max_dig = number % 10
number //= 10  # number = number // 10
while number > 0:
    if number % 10 > max_dig:
        max_dig = number % 10
    number //= 10  # number = number // 10
print(max_dig)

# ЗАДАНИЕ 5

proceeds = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
if proceeds > costs:
    print('Фирма работает с прибылью - ', proceeds - costs)
    profitability = (proceeds - costs) / proceeds
    print('Рентабельность выручки фирмы - ', round(profitability, 2))
    workers = int(input('Введите количество сотрудников фирмы: '))
    print('Прибыль фирмы в расчёте на одного сотрудника - ', round(((proceeds - costs) / workers), 2))
elif proceeds < costs:
    print('Фирма работает в убыток')
else:
    print('Фирма работает в ноль')

# ЗАДАНИЕ 6

a = int(input('Сколько км пробжал спортсмен в первый день: '))
b = int(input('Цель спортсмена в км: '))
days = 1
print(f'{days}-й день: {a}')
while a <= b:
    a = 1.1 * a
    days += 1
    print(f'{days}-й день: {round(a, 2)}')
print(f"На {days}-й день спортсмен достиг результата — не менее {b} км")
