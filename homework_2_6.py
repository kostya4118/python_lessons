# ЗАДАНИЕ 6
# products = [(1, {'name': 'iphone', 'price': 50000.99, 'count': 3, 'unit': 'шт'}), (2, {'name': 'imac', 'price': 90000.0, 'count': 7, 'unit': 'шт'}), (3, {'name': 'ipad', 'price': 40000.0, 'count': 7, 'unit': 'шт'}), (4, {'name': 'семечки', 'price': 99.5, 'count': 800, 'unit': 'кг'})]

analitics = {
    'names': [], 'prices': [], 'counts': [], 'units': []
}
products = []
num = 1
while True:
    product = (
        num, {'name': str(input('Введите название товара: ')), 'price': float(input('Введите цену товара: ')),
              'count': int(input('Введите количество товара: ')),
              'unit': str(input('Введите единицу измерения товара: '))}
    )
    products.append(product)
    analitics['names'].append(product[1]['name'])
    analitics['prices'].append(product[1]['price'])
    analitics['counts'].append(product[1]['count'])
    analitics['units'].append(product[1]['unit'])
    num += 1
    if input('Добавить ещё товар? (Да/Нет)').title() == 'Нет':
        break

for product in products:
    print(product)

for k, v in analitics.items():
    print(k, v)
