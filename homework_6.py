# ЗАДАНИЕ 1

from time import sleep


class TrafficLight:
    __color = ['красный', 'жёлтый', 'зелёный']

    def __init__(self, time):
        self.time = time

    def changeColor(self):
        iter = 0
        while iter != 20:
            print(f'горит {TrafficLight.__color[0]} свет')
            sleep(7)
            print(f'горит {TrafficLight.__color[1]} свет')
            sleep(2)
            print(f'горит {TrafficLight.__color[2]} свет')
            sleep(self.time)
            iter += 1

try:
    svetofor = TrafficLight(int(input('Введите время горения зелёного: ')))
    svetofor.changeColor()
except ValueError:
    print('Введены некорректные значения!')


# ЗАДАНИЕ 2

class Road():
    __weight = 0.025
    __height = 5
    def __init__(self, length, width):
        self._length = length
        self._width = width
        if self._length <= 0 or self._width <= 0:
            print('Введены некорректные параметры!')
        else:
            m = self._length * self._width * Road.__weight * Road.__height
            print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна: {m} т')

try:
    r = Road(int(input('Введите длину дороги в метрах: ')), int(input('Введите ширину дороги в метрах: ')))
except ValueError:
    print('Введены некорректные параметры!')


# ЗАДАНИЕ 3

class Worker:
    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, wage, bonus)
        self.position = position

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

try:
    p = Position(name = input('Имя: ').title(), surname = input('Фамилия: ').title(), position = input('Должность: ').upper(), wage = float(input('Оклад: ')), bonus = float(input('Премия: ')))
    print(f'Полное имя - {p.get_full_name()}')
    print(f'Доход - {p.get_total_income()}')
except ValueError:
    print('Введены некорректные значения!')


# ЗАДАНИЕ 4

class Car:
    name = 'undefined'
    color = 'белый'
    speed = 60
    is_police = False

    def go(self):
        return f'{self.name} поехала'
    def stop(self):
        return f'{self.name} остановилась'
    def turn(self, direction=None):
        if direction:
            return f'{self.name} повернул {direction}'
        else:
            return f'{self.name} едет прямо'

    def show_speed(self):
        return f'Скорость движения: {self.speed}'

class TownCar(Car):
    name = 'Лада'
    speed = 75

    def show_speed(self):
        if self.speed > 60:
            return f'Скорость выше допустимой на {self.speed - 60} км/ч'
        else:
            return f'Скорость движения: {self.speed}'

class SportCar(Car):
    name = 'Lotus'
    speed = 170

class WorkCar(Car):
    name = 'BMW'
    color = 'синий'

    def show_speed(self):
        if self.speed > 40:
            return f'Скорость выше допустимой на {self.speed - 40} км/ч'
        else:
            return f'Скорость движения: {self.speed}'

class PoliceCar(Car):
    name = 'Ford'
    is_police = True
    color = 'чёрный'

tc = TownCar()
print(tc.color, tc.go(), tc.show_speed())

sc = SportCar()
print(sc.turn('налево'), sc.show_speed())

wc = WorkCar()
print(wc.color, wc.turn() + ' Это полицейская машина? - ' + str(wc.is_police), wc.show_speed())

pc = PoliceCar()
print(pc.color, pc.stop() + ' Это полицейская машина? - ' + str(pc.is_police))


# ЗАДАНИЕ 5

class Stationery():
    def __init__(self, title = ''):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'

class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


pen = Pen('ручкой')
print(pen.draw())

pencil = Pencil('карандашем')
print(pencil.draw())

handle = Handle('маркером')
print(handle.draw())