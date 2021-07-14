# ЗАДАНИЕ 1

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def get_date(cls, date_str):
        date = ''
        for el in date_str:
            date = ''.join([date, (el if el in '1234567890' else ' ')])
        d, m, y = map(int, date.split())
        return cls(d, m, y)

    @staticmethod
    def valid_date(obj):
        if (obj.day > 0 and obj.day < 32) and (obj.month > 0 and obj.month < 13) and (obj.year > 0 and obj.year < 3000):
            print(f'{obj.day:02}-{obj.month:02}-{obj.year}\nДата корректна!')
        else:
            print('Введены некорректные день, месяц или год')


try:
    dat = Date.get_date(input('Введите день, месяц и год в числовом формате: '))
    Date.valid_date(dat)
except ValueError:
    print('Не введены день, месяц или год')


# ЗАДАНИЕ 2

class ZeroErr(Exception):
    def __init__(self, txt):
        self.txt = txt

x = input('Введите делимое: ')
y = input('Введите делитель: ')

try:
    if float(y) == 0:
        raise ZeroErr('На ноль делить нельзя!')
    else:
        res = float(x) / float(y)
except ValueError:
    print('Вы ввели не число!')
except ZeroErr as err:
    print(err)
else:
    print(f'Частное = {round(res, 4)}')


# ЗАДАНИЕ 3

class Isnotdig(Exception):
    def __init__(self, txt):
        self.txt = txt


class GetListDig:
    @staticmethod
    def get():
        li = []
        while True:
            try:
                el = input('введите новый элемент списка (stop - для остановки): ')
                if el.isdigit():
                    li.append(int(el))
                elif el.lower() == 'stop':
                    break
                else:
                    raise Isnotdig('Вы ввели не число!')
            except Isnotdig as err:
                print(err)
        print(li)


GetListDig.get()


# ЗАДАНИЕ 4-6

class NoYear(Exception):
    def __init__(self, txt):
        self.txt = txt


class Sklad:
    _equipments = {'printer': [], 'xerox': [], 'scanner': []}

    def delivery(self,  *equips):
        for equip in equips:
            self._equipments[equip.eq_type].remove(equip.unit)

    def reception(self,  *equips):
        for equip in equips:
            self._equipments[equip.eq_type].append(equip.unit)


class Equipment:
    def __init__(self, vender, model, year, eq_type=None):
        self.vender = vender
        self.model = model
        self.eq_type = eq_type

        try:
            self.year = year
            if str(year).isdigit() == False:
                raise NoYear('Год введён неверно!')
        except NoYear as err:
            self.year = str(err)

        self.unit = {'Тип': self.eq_type, 'Производитель': self.vender, 'Модель': self.model, 'Год': self.year}

    def __str__(self):
        return f'Info: {self.unit}'



class Printer(Equipment):
    def __init__(self, vender, model, year, eq_type='printer'):
        super().__init__(vender, model, year, eq_type)
        self.eq_type = eq_type

class Scanner(Equipment):
    def __init__(self, vender, model, year, eq_type='scanner'):
        super().__init__(vender, model, year, eq_type)
        self.eq_type = eq_type

class Xerox(Equipment):
    def __init__(self, vender, model, year, eq_type='xerox'):
        super().__init__(vender, model, year, eq_type)
        self.eq_type = eq_type


e1 = Printer('Sony', 'kthb', 'yyyy')
print(e1)
e2 = Printer('HP', 'OfficeJet Pro 8210', 2020)
e3 = Scanner('RIXET', 'RIXET', 2019)
e4 = Xerox('4018', '4018', 2017)

s = Sklad()
s.reception(e1, e2, e3, e4)
s.delivery(e1)

for k, v in s._equipments.items():
    print(f'{k} - {v}\n')

# ЗАДАНИЕ 7

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)