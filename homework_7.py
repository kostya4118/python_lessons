# ЗАДАНИЕ 1

class Matrix():
    def __init__(self, m):
        self.m = m

    def __str__(self):
        for line in self.m:
            for el in line:
                print(f'  {el}  ', end='')
            print('')
        return ''

    def __add__(self, other):
        try:
            for i in range(len(self.m)):
                for el in range(len(self.m[i])):
                    self.m[i][el] = self.m[i][el] + other.m[i][el]
            return Matrix.__str__(self)
        except IndexError:
            return 'Невозможно сложить разноразмерные матрацы'

m1 = Matrix([[-1, 0], [-1, 0], [1, -1]])
print(m1)

m2 = Matrix([[-1, 1], [8, 1], [0, -1]])
print(m2)

print(m1 + m2)


# ЗАДАНИЕ 2

from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return f'Суммарный расход ткани: {round(self.consumption() + other.consumption(), 2)}'


class Coat(Clothes):

    @property
    def param(self):
        return self.__param

    @param.setter
    def param(self, param):
        if param < 35:
            self.__param = 35
        elif param > 70:
            self.__param = 70
        else:
            self.__param = param

    def consumption(self):
        return round((self.param / 6.5 + 0.5), 2)

    def __str__(self):
        return f'Расход ткани на пальто составит: {round((self.param / 6.5 + 0.5), 2)}'


class Costume(Clothes):


    @property
    def param(self):
        return self.__param

    @param.setter
    def param(self, param):
        if param < 0.8:
            self.__param = 0.8
        elif param > 2.5:
            self.__param = 2.5
        else:
            self.__param = param

    def consumption(self):
        return round((2 * self.param + 0.3), 2)
    def __str__(self):
        return f'Расход ткани на костюм составит: {round((2 * self.param + 0.3), 2)}'

while True:
    try:
        coat = Coat(int(input('Введите Ваш размер одежды: ')))
        costume = Costume(int(input('Введите Ваш рост в см: ')) / 100)

        print(coat)
        print(costume)
        print(coat + costume)
        break

    except ValueError:
        print('Введено неверное значение! Попробуйте ещё раз.')


# ЗАДАНИЕ 3

class Cell:
    def __init__(self, count):
        self.count = count

    def __str__(self):
        return f'количество ячеек: {self.count}'

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if (self.count - other.count) <= 0:
            return f'Разность количества ячеек двух клеток должна быть больше нуля!'
        else:
            return Cell(self.count - other.count)

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, n):
        s = ''
        for i in range(self.count // n):
            s += ('*' * n + '\n')
        s += ('*' * (self.count % n) + '\n')
        return s



c1 = Cell(8)
c2 = Cell(6)
c3 = Cell(5)

print(c1 / c2)
print(c3 - c1)
print(c1 - c3)

print((c1 + c2 * c3).make_order(5))