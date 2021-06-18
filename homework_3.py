# ЗАДАНИЕ 1

def division(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        return str('На ноль делить нельзя!')
    return c


print(division(float(input('Введите делимое: ')), float(input('Введите делитель: '))))


# ЗАДАНИЕ 2

def anketa(**kwargs):
    ank = kwargs
    for k, v in ank.items():
        print(k, v)


anketa(Имя=input('Введите имя: ').title(), Фамилия=input('Введите фамилию: ').title(), Год=int(input('Введите год рождения: ')), Город=input('Введите город проживания: ').title(), email=input('Введите email: '), Телефон=int(input('Введите телефон: ')))


# ЗАДАНИЕ 3

def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    return sum(my_list)


print(my_func(float(input('Введите первое число: ')), float(input('Введите второе число: ')), float(input('Введите третье число: '))))


# ЗАДАНИЕ 4

def involution(x, y):
    if x < 0 or y >= 0:
        return str('введены некорректные числа!')
    else:
        return float(x) ** int(y)


print(involution(4, -5))


def involution_hard(x, y):
    if x < 0 or y >= 0:
        return str('введены некорректные числа!')
    else:
        a = x
        for i in range(abs(y) - 1):
            a *= x
        res = 1 / a
        return res


print(involution_hard(4, -5))


# ЗАДАНИЕ 5

result = 0

while True:
    my_list = input('Введите список чисел через пробел, или "end" для завершения')

    my_list = my_list.split()

    if 'end' in my_list:
        i = my_list.index('end')
        my_list = my_list[:i]
        stop = True
    else:
        stop = False

    result_list = list(map(float, my_list))
    # result_list = [float(el) for el in my_list]

    sub_result = sum(result_list)

    result += sub_result

    print(result)

    if stop:
        break


# ЗАДАНИЕ 6-7

def int_func(s):
    # s = s.title()
    s = s.split()
    s_res = []
    for word in s:
        if word.islower():
            word = word.title()
        s_res.append(word)
    s = ' '.join(s_res)
    return s


print(int_func(input('Введите строку: ')))
