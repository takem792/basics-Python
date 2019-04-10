# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


import os
path = os.getcwd()
tree = os.walk(path)
dir_list = []
for i in tree:
    dir_list.append(i)
print(f'по указаному пути содержутся следующие папки - ')
for dir_name in (dir_list[0][1]):
    print(dir_name)

