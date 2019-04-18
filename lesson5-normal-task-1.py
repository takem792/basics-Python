# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


def is_folder_name(folder_name):
    '''
    Проверяет имя папки на допустимость
    :param folder_name: имя папки
    :return:
    '''
    import re
    notperm1 = r'[*\|/"><?]'
    notperm2 = r'^(CON|NUL|COM1|COM2|COM3|LPT1|LPT2|LPT3|AUX|PRN|COM1|COM2|COM3|COM4|COM5|COM6|COM7|COM8|COM9|LPT1|LPT2|LPT3|LPT4|LPT5|LPT6|LPT7|LPT8|LPT9)$'
    try:
        re.match(notperm2, folder_name.upper()).group()
        return False
    except AttributeError:
        pass
    try:
        re.search(notperm1, folder_name).group()
        return False
    except AttributeError:
        pass
    return True


def in_folder(folder_name):
    '''
    переход внутрь папки
    :param folder_name: имя папки куда перейти
    :return:
    '''
    import os
    path = os.getcwd()
    try:
        os.chdir(path + '\\' + folder_name)
        print('перешли в папку', folder_name)
    except FileNotFoundError:
        print("Такой папки не существует, попробуйте еще раз")


def folder_contents():
    '''
    Показывает содержимое текущей папки
    :return:
    '''
    import os
    path = os.getcwd()
    tree = os.walk(path)
    dir_list = []
    for i in tree:
        dir_list.append(i)
    print(f'по указаному пути содержутся следующие объекты - ')
    for dir_name in (dir_list[0][1]):
        print(dir_name)
    for dir_name in (dir_list[0][2]):
        print(dir_name)
    print('---------------------\n')


def del_folder(folder_name):
    '''
    Удаляет папку с заданным именем
    :param folder_name: имя папки
    :return: результат (удалили или нет)
    '''
    import lesson5_easy_task1 as delete_folder
    if delete_folder.rem_dir(folder_name):
        print('Удалили папку', folder_name)
    else:
        print(f'Папки с именем {folder_name} не существует')


def crt_folder(folder_name):
    '''
    Создает папку с заданным именем
    :param folder_name: имя папки
    :return: результат (создали или нет)
    '''
    import lesson5_easy_task1 as create_folder
    if create_folder.cr_dir(folder_name):
        print('Создали папку', folder_name)
    else:
        print(f'Папка с именем {folder_name} уже существует')


def rtn_folder():
    import os
    path = os.getcwd()
    os.chdir(os.path.split(path)[0])
    new_path = os.getcwd()
    if new_path == path:
        print('Дальше бежать некуда, вы на самом верху')
    else:
        print('Перешли на уроень выше')


def do():
    while True:
        try:
            choice = int(input('Выберите пункт:\n'
                               '1. Перейти в папку\n'
                               '2. Просмотреть содержимое текущей папки\n'
                               '3. Создать папку\n'
                               '4. Удалить папку\n'
                               '5. Вернуться в папку уровнем выше\n'
                               '6. Выход из программы любое другое число\n'
                               '---------------------\n'
                               'Ваш выбор:'))
            break
        except ValueError:
            print('введите число от 1 до 6')
    if choice == 1:
        folder_name = input("Введите имя папки ->")
        if is_folder_name(folder_name):
            in_folder(folder_name)
        else:
            print('Имя недопустимо или содержит недопустимые символы')
        return True
    elif choice == 2:
        folder_contents()
        return True
    elif choice == 3:
        folder_name = input("Введите имя папки ->")
        if is_folder_name(folder_name):
            crt_folder(folder_name)
        else:
            print('Имя недопустимо или содержит недопустимые символы')
        return True
    elif choice == 4:
        folder_name = input("Введите имя папки ->")
        if is_folder_name(folder_name):
            del_folder(folder_name)
        else:
            print('Имя недопустимо или содержит недопустимые символы')
        return True
    elif choice == 5:
        rtn_folder()
        return True
    else:
        return False


while do():
    continue
print('До свидания, было приятно с вами поработать!')
