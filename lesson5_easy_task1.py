# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def cr_dir(dir_name='dir_'):
    '''
    Создаем папку с заданным именем
    :param dir_name: Имя папки, по умолчанию  dir_
    :return: True если успешно, False, если нет
    '''
    import os
    try:
        os.mkdir(dir_name)
        return True
    except FileExistsError:
        return False


def rem_dir(dir_name='dir_'):
    '''
    Удаляем папку с заданным именем
    :param dir_name: Имя папки, по умолчанию  dir_
    :return: True если успешно, False, если нет
    '''
    import os
    try:
        os.rmdir(dir_name)
        return True
    except FileNotFoundError:
        return False


def cr_dir_num(dir_name='dir_'):
    # делаем папки для задания
    dir_create = []
    for num in range(1, 3):
        if cr_dir(dir_name + str(num)):
            dir_create.append(dir_name + str(num))
    print("Созданы следующие папки:", dir_create)


def rem_dir_num(dir_name='dir_'):
    # удаляем папки для задания
    des = input('удаляем? (y/n)\n')
    dir_remove = []
    if des == "y":
        for num in range(1, 3):
            if rem_dir(dir_name + str(num)):
                dir_remove.append(dir_name + str(num))
        print('Удалены следующие папки:', dir_remove)
    else:
        print("Как знаешь, но этот мусор кому-то удалять придется... :)")


if __name__ == "__main__":
    cr_dir_num()
    rem_dir_num()
