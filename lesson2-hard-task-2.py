month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
while True:
    data = input("Введите дату в формате dd.mm.yyyy ->")
    data_check = data.split('.')
    if len(data) != 10:   # Если длина строки 10, то ошибка
        print("Ошибка формата!")
        continue
    if len(data_check) !=3:   # Если точек не две, то ошибка
        print("Ошибка формата!")
        continue
    if len(data_check[0]) != 2 or len(data_check[1]) != 2 or len(data_check[2]) != 4:   # Если ошибка в длинне элементов, то ошибка
        print("Ошибка формата!")
        continue
    if not data_check[0].isdecimal() or not data_check[1].isdecimal() or not data_check[2].isdecimal():   #Если ввели не числа
        print("Ошибка формата!")
        continue
    if 0 < int(data[3:5]) < 13:   # Если ошибка в месяце
        if 0 < int(data[0:2]) < month[int(data[3:5])]:   # Если ошибка в дне
            if 0 < int(data[6:10]) < 10000:   # Если ошибка в годе
                print("Дата введена корректно")
                break
            else:
                print("Ошибка, год должен быть от 1 до 9999")
        else:
            print(f'Ошибка, день должен быть от 1 до {month[int(data[3:5])]} для месяца {int(data[3:5])}')
    else:
        print("Ошибка, месяц должен быть от 1 до 12")