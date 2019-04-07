# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь
# заглавные первые буквы. email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре,
# допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например: Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email
# (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.


def is_name(name_surname):
    ptr_name1 = '[A-Z]'
    ptr_name2 = '[^A-z]'
    flag = True
    try:
        re.search(ptr_name2, name_surname).group()
        print('Содержит что-то кроме букв, имя(фамилия) должна содержать только буквы')
        flag = False
    except AttributeError:
        pass
    try:
        re.match(ptr_name1, name_surname).group()
    except AttributeError:
        print('Первая буква должна быть заглавная')
        flag = False
    return flag


def is_email(e_mail):
    ptr_email = '[a-z_0-9]+@[a-z0-9]+\.(ru|org|com|])'
    try:
        re.match(ptr_email, e_mail).group(1)
    except AttributeError:
        print('e-mail должен быть в формате: \n'
              'текст в нижнем регистре, допускается нижнее подчеркивание и цифры, \n'
              'потом @, потом текст, допускаются цифры, \n'
              'точка, ru или org или com\n')
        return False
    return True


import re
while True:
    name = input('Введите имя ->\n')
    if is_name(name):
        break
while True:
    surname = input('Введите Фамилию ->\n')
    if is_name(surname):
        break
while True:
    email = input('Введите e-mail ->\n')
    if is_email(email):
        break
print(name, surname, email)