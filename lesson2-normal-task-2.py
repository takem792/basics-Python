month = ("января", "Февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "ноября", "декабря")
days = ("первое", "второе", "третье", "четвертое", "и т.д.")
data = input('Введите дату в формате dd.mm.yyyy->')
print(f'Вы ввели дату - {days[(int(data[0:2]) - 1)]} {month[(int(data[3:5]) - 1)]} {data[6:10]} года')