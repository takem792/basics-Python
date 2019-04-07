# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"


def user_info(user_name, user_age, user_city):
    '''
    Функция выводит информацию о Имени, Возрасте и Городе проживания user
    '''
    print(f'{user_name}, {user_age} год(а), проживает в городе {user_city}')


while True:
    user_name = input('Введите Имя->')
    if user_name:
        break
    print('Представьтесь, пожалуйста')
user_age = input('Введите возраст->')
user_city = input('Введите город проживания->')
if not user_age.isdigit():
    user_age = 'Нет информации'
if len(user_city) == 0:
    user_city = 'Нет информации'
user_info(user_name, user_age, user_city)
