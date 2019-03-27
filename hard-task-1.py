questionnaire = []
while True:
    age = int(input('Введите ваш возраст -> '))
    if age == 1000:  # Условие для окончания анкетирования и показа результата
        print('Результат анкетирования:')
        for i in range(0, len(questionnaire)):
            print(questionnaire[i])
        break
    if age <= 20 or age >= 40:  # Условие для отсечение пациентов, не входящих в фокус группу
        print('Анкета для людей от 20 до 40')
        continue
    name = str(input('Введи ваше имя -> '))
    surname = str(input('Введи вашу фамилию -> '))
    weight = int(input('Введи ваше вес -> '))
#   Определяем состояние пациента
    if 20 < age <= 30:
        if 60 <= weight <= 80:
            result = 'Хорошее состояние'
        elif 50 <= weight < 60 or 80 < weight <= 90:
            result = 'Следует заняться собой'
        else:
            result = 'Следует обратиться к врачу!'
        print(result)
    elif 30 <= age < 40:
        if 70 <= weight <= 90:
            result = 'Хорошее состояние'
        elif 60 <= weight < 70 or 90 < weight <= 100:
            result = 'Следует заняться собой'
        else:
            result = 'Следует обратиться к врачу!'
        print(result)
    questionnaire.append([name, surname, age, weight, result])