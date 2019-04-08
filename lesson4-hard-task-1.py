# Задание:
# Эта программа являет собой упрощенный симулятор банкомата, пользователь вводит номер карты и пин код,
# в случае успеха программа предлагает меню для выбора действий, где он может проверить счет, или снять деньги.
#
# Эта задача не так похожа на другие, но она, как никогда прежде приближена к реалиям разработки общего проекта.
#
# Ваша задача исправить ошибки логики, и выполнить проверки данных, которые вводит пользователь.
# Обязательно убедитесь, что вы выполнили все проверки, попробуйте сами сломать свою программу вводя неверные данные!
#4276123465440000 9090


person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}

bank = [person1, person2, person3]


def get_person_by_card(card_number):
    for person in bank:
        if person['card'] == card_number:
            return person


def is_pin_valid(person, pin_code):
    if person['pin'] == pin_code:
        return True
    return False


def check_account(person):
    return round(person['money'], 2)


def withdraw_money(person, money):
    if person['money'] - money >= 0:
        person['money'] -= money
        return 'Вы сняли {} рублей.'.format(money)
    else:
        return 'На вашем счету недостаточно средств!'


def process_user_choice(choice, person):
    if choice == 1:
        print(check_account(person))
    elif choice == 2:
        count = float(input('Сумма к снятию:'))
        print(withdraw_money(person, count))


def is_number(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


def is_input_valid():
    while True:
        try:
            card_number, pin_code = input('Введите номер карты и пин код через пробел:').split()
        except ValueError:
            print('введите согласно шаблону (номер карты и пин код через пробел)')
            continue
        if is_number(card_number):
            card_number = int(card_number)
        else:
            print("номер карты должен состоять только из цифр")
            continue
        if is_number(pin_code):
            pin_code = int(pin_code)
        else:
            print("пинкод должен состоять только из цифр")
            continue
        break
    return card_number, pin_code


def start():
    card_number, pin_code = is_input_valid()
    person = get_person_by_card(card_number)
    if person and is_pin_valid(person, pin_code):
        while True:
            choice = input('Выберите пункт:\n'
                               '1. Проверить баланс\n'
                               '2. Снять деньги\n'
                               '3. Выход\n'
                               '---------------------\n'
                               'Ваш выбор:')
            if not is_number(choice):
                print('Пожалуйста, сделайте выбор (введите 1,2 или 3)')
                continue
            if int(choice) == 3:
                print('Благодарим за сотрудничество, приходите еще')
                break
            elif int(choice) == 1 or int(choice) == 2:
                process_user_choice(int(choice), person)
            else:
                print('Такого пункта в меню нет')
    else:
        print('Номер карты или пин код введены не верно!')


start()
