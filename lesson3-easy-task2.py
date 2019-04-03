# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них


def print_max(*args):
    '''
    Функция нахождения максимума из нескольких чисел
    '''
    return max(*args)


def is_number(s):
    '''
    Является ли аргумент числом (float)
    '''
    try:
        float(s)
        return True
    except ValueError:
        return False


print('Введите три числа;')
three_num = []
for num_number in range(1, 4):
    while True:
        num = input(f'введите число{num_number}->')
        if is_number(num):
            break
        else:
            print('Вы ввели не число, повторите ввод')
    three_num.append(float(num))
print(print_max(three_num))