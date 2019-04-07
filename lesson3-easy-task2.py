# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них


def max_num(*args):
    '''
    Так я формально решил домашку - создал функцию,но ока, кмк, излишняя, если, конечно, в процессе разработки мне не
    не нужно постоянно искать "наибольщее" из нескольких аргументов
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
print(max_num(three_num))
print((lambda num_max: max(num_max))(three_num))   # Так я формально не написал функцию, как требует постановка задачи.
max_num = lambda num_max: max(num_max)   #Так ругается, говорит делайте через def - это признанная практика?
print(max_num(three_num))
