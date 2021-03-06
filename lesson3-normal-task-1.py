# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.


people = ["Вася", "Ира", "Люся", "Петя", "Сергей"]
ppl_salary = ["100000", "200000", "600000", "50000", "700000"]
list_employee = dict(zip(people, ppl_salary))   # словарь
with open("salary.txt", 'w', encoding="utf-8") as salary:
    for ppl in list_employee.keys():
        if int(list_employee[ppl]) < 500000:
            '''
            с ЗП выше 500.000 в файл не записываю, так как при передаче файла данные из него могут и распечатать,
            а нас просили мажоров не раскрывать :)
            '''
            salary.write(f'{ppl} - {list_employee[ppl]}\n')
with open("salary.txt", encoding="utf-8") as salary:
    for line in salary:
        print(f'{line.split()[0].upper().ljust(7)} - на руки - {str(0.87*int(line.split()[2])).rjust(10)} р.')
