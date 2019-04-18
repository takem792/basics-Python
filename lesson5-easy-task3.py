# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


import sys
import os
import shutil
file_name = os.path.basename(sys.argv[0])
name_parts = os.path.splitext(file_name)
new_file_name = str(name_parts[0]) + '_copy'
copy_num = 1
copy_new_file_name = new_file_name
while True:
    if not os.path.exists(copy_new_file_name):
        shutil.copy(file_name, copy_new_file_name)
        copy_num = 1
        break
    else:
        copy_new_file_name = new_file_name + str(copy_num)
        copy_num += 1
