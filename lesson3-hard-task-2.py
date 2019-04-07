# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.


def is_number(s):
    '''
    Является ли аргумент числом (float)
    '''
    try:
        float(s)
        return True
    except ValueError:
        return False


def attack(person_att, person_def):
    '''
    Функция для получения статов защищающегося после атаки
    :param person_att: кто атакует
    :param person_def:  кто защищается
    :return: статы того, кто защищается
    '''
    person_def['health'] = person_def['health'] - round(result_damage(person_att['damage'], person_def['armor']), 0)
    return person_def


def result_damage(damage, armor):
    '''
    Функция для расчета урона в зависимости от брони
    :param damage: урон
    :param armor: броня
    :return: урон, уменьшенный на броню
    '''
    return damage / armor


def character_stats_r(ch_name):
    '''
    функция для считывания из файла статов персонажа (имя файла совпадает с именем персонажа)
    :param ch_name: имя персонажа
    :return: словарь со статами персонажа
    '''
    ch_stats = {}
    with open(ch_name + ".txt", encoding="utf-8") as ch_stats_file:
        for line in ch_stats_file:
            if is_number(line.split()[1]):
                ch_stats[line.split()[0]] = float(line.split()[1])
            else:
                ch_stats[line.split()[0]] = line.split()[1]
    return ch_stats


def character_stats_w(ch_name):
    '''
    функция для записи статов персонажа в файл с именем персонажа
    :param ch_name:
    :return:
    '''
    with open(ch_name['name'] + ".txt", 'w', encoding="utf-8") as ch_stats_file :
        for stats in ch_name.keys():
            ch_stats_file.write(f'{stats} {ch_name[stats]}\n')


def fight(ch1, ch2):
    '''
    Функция сражения между двумя персонажами до смерти одного из них
    :param ch1: персонаж 1
    :param ch2: персонаж 2
    :return: Победитель
    '''
    while True:
        pers_def = attack(ch1, ch2)
        if pers_def['health'] <= 0:
            winer = ch1
            break
        pers_def = attack(ch2, ch1)
        if pers_def['health'] <= 0:
            winer = ch2
            break
    return winer


import random
# Враги
enemy_o = {'name': 'Одержимый', 'health': 30, 'damage': 15, 'armor': 1}
enemy_i = {'name': 'Имп', 'health': 40, 'damage': 75, 'armor': 0.8}
enemy_a = {'name': 'Адский_крушитель', 'health': 150, 'damage': 40, 'armor': 1.1}
enemy_k = {'name': 'Рыцарь_Ада', 'health': 210, 'damage': 50, 'armor': 1.2}
enemy_r = {'name': 'Ревенант', 'health': 180, 'damage': 90, 'armor': 1.1}
enemy_poole = {1: enemy_o, 2: enemy_i, 3: enemy_a, 4: enemy_k, 5: enemy_r}
# Игрок
name = input('Как зовут тебя, странник?\n')
player = {'name': name, 'health': 100, 'damage': 50, 'armor': 1.5}
print('\nДобро пожаловать в игру\n')
print(f'***Игрок {name} начинает игру***\n')
# Создаем файлы со статами
character_stats_w(player)
enemy = enemy_poole[random.randint(1, 5)]
character_stats_w(enemy)
# считываем статы
player = character_stats_r(player['name'])
enemy = character_stats_r(enemy['name'])
# Начало поединка
print('Ты видишь перед собой', enemy['name'])
while True:
    agressive = input(f'Начать битву c {enemy["name"]}? (Да или Нет)->\n')
    if agressive.lower() == "да":
        print(f'**{player["name"]} бросается на {enemy["name"]}**')
        print('*** КТО ЖЕ ПОБЕДИТ ***')
        winer = fight(player, enemy)
        break
    elif agressive.lower() == "нет" :
        print(f'**  {enemy["name"]} агрессивно рычит  **\n  сРррРРррРРРррРР\n**  и бросается на {player["name"]}  **')
        print('*** КТО ЖЕ ПОБЕДИТ ***')
        winer = fight(enemy, player)
        break
    else:
        print(f'{player["name"]}, нужно сделать выбор\n')
winer = fight(player, enemy)
print(f'Победитель поединка\n{winer["name"]} (показатель здоровья - {winer["health"]})')
