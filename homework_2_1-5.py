# ЗАДАНИЕ 1

types = [12.4, 7, complex(5, 6), 'this is a string', [11, 28], tuple('обычная строка'), set('abrakadabra'), False]

for var in types:
    print(var)
    print(type(var))


# ЗАДАНИЕ 2

my_list = []

while True:
    a = input('Введите элемент списка или end для завершения ввода: ')
    if a.title() == 'End':
        break
    else:
        my_list.append(a)
    print(my_list)

for i in range(len(my_list) - 1):
    if i % 2 == 0:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 1

print(my_list)

# ЗАДАНИЕ 3

seasons = {
    'Зима': [1, 2, 12],
    'Весна': [3, 4, 5],
    'Лето': [6, 7, 8],
    'Осень': [9, 10, 11],
}

month = int(input('Введите номер месяца: '))

for key in seasons:
    if month in seasons[key]:
        print(f'Это {key}')
        break

# ЗАДАНИЕ 4


string = input('Введите строку из нескольких слов, разделённых пробелами: ')

my_list = string.split()

print(my_list)

for num, word in enumerate(my_list, 1):
    print(num, word[:10])


# ЗАДАНИЕ 5

rating = [7, 5, 3, 3, 2]

while True:
    try:
        num = int(input('Введите новый элемент рейтинга: '))
    except ValueError:
        print('Неверное значение!')
    else:
        break

if num in rating:
    i = rating.index(num)
    rating.insert(i + 1, num)
else:
    rating.append(num)

print(sorted(rating, reverse=True))
