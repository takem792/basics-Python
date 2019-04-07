# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.


def attack(person1, person2):
    person1['player_health'] = person1['player_health'] - person2['enemy_damage']
    person2['enemy_health'] = person2['enemy_health'] - person1['player_damage']
    return person1, person2


name = input('Введите имя игрока->')
player = {'player_name': name, 'player_health': 100, 'player_damage': 50}
enemy = {'enemy_name': 'Imp', 'enemy_health': 80, 'enemy_damage': 25}
print(attack(player, enemy))