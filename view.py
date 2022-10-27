from fractions import Fraction

def get_type():
    print('Выберите калькулятор: \n\t 1. рациональный \n\t 2. комплексный \n')
    return input('Тип калькулятора № ')

def get_action():
    return input('\tВведите действие: ')

def get_value(type):
    if int(type) == 2:
        a = int(input('\tВведите действительную часть числа: '))
        b = int(input('\tВведите мнимую часть числа: '))
        return complex (a, b)
    else:
        return Fraction (input('\tВведите число: '))

def view_data(data, title):
    print(f'{title}{data}')