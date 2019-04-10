# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


import os
dir_name = 'dir_'
# делаем папки
dir_create = []
for num in range(1, 3):
    try:
        os.mkdir(dir_name+str(num))
        dir_create.append(dir_name+str(num))
    except FileExistsError:
        print('Такая папка уже существует')
print("Созданы следующие папки:", dir_create)
# удаляем папки
des = input('удаляем? (y/n)\n')
dir_remove = []
if des == "y":
    for num in range(1, 3):
        try:
            os.rmdir(dir_name+str(num))
            dir_remove.append(dir_name+str(num))
        except FileNotFoundError:
            pass
    print('Удалены следующие папки:', dir_remove)
else:
    print("Как знаешь, но этот мусор кому-то удалять придется... :)")
