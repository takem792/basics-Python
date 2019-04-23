import random


class Barrels:
    '''
    Класс для дейсвия с бочонками
    '''
    @staticmethod
    def create_barrels():
        '''
        Создание мешочка с бочонками
        :return:
        '''
        barrels = []
        for i in range(1, 91):
            barrels.append(i)
        return barrels

    @staticmethod
    def next_barrel(barrels):
        '''
        Выбрасывание бочонка с удалением последнего из мешка
        :param barrels:
        :return:
        '''
        return barrels.pop(random.randint(0, len(barrels)-1))


class LottoCard:
    '''
    класс для работы с карточками лото
    '''
    def __init__(self, name):
        self.name = name
        self.lotto_card = ["", "", "", "", "", "", "", "", "",
                           "", "", "", "", "", "", "", "", "",
                           "", "", "", "", "", "", "", "", ""]
        self._create_card()
        self.remaining_num = 15

    def _create_card_line(self, barrels_for_card, start, finish):
        '''
        Создание одной линии карты
        :param barrels_for_card: мешочек с бочонками
        :param start: параметры линии
        :param finish: параметры линии
        :return: строку карточки
        '''
        it = 0
        while it < 5:
            num = random.randint(start, finish)
            barrel_num = random.randint(0, len(barrels_for_card)-1)
            if self.lotto_card[num] == '':
                self.lotto_card[num] = barrels_for_card[barrel_num]
                barrels_for_card.pop(barrel_num)
                it += 1

    def _create_card(self):
        '''
        создаем карточку лото
        :return: карточка лото
        '''
        barrels_for_card = Barrels.create_barrels()
        self._create_card_line(barrels_for_card, 0, 8)
        self._create_card_line(barrels_for_card, 9, 17)
        self._create_card_line(barrels_for_card, 18, 26)

    def _print_lotto_card_line(self, start, finish):
        '''
        печать одной линии карточки лото
        :param start: параметры линии
        :param finish: параметры линии
        :return: линия карточки
        '''
        for i in range(start, finish):
            print('|', end='')
            if self.lotto_card[i] == '':
                print('    ', end='')
            else:
                if len(str(self.lotto_card[i])) < 2:
                    print(f'  {self.lotto_card[i]} ', end='')
                else:
                    print(f' {self.lotto_card[i]} ', end='')
        print('|')

    def print_lotto_card(self):
        '''
        Печать карточки лото
        :return: карточку лото
        '''
        print(' --------------------------------------------')
        self._print_lotto_card_line(0, 9)
        self._print_lotto_card_line(9, 18)
        self._print_lotto_card_line(18, 27)
        print(' --------------------------------------------')

    def crossout_num(self, barrel):
        '''
        Замена в карточки лото зачеркнутого числа на ХХ
        :param barrel: номер бочонка
        :return: карточку с зачеркнутым числом
        '''
        self.lotto_card.insert(self.lotto_card.index(barrel), "XX")
        self.lotto_card.remove(barrel)


#генерация данных для игры
game_barrels = Barrels.create_barrels()
player_card = LottoCard('Игрок')
master_card = LottoCard('Мастер Игры')
#тянем бочонки
while True:
    print(f'{player_card.name} - Ваша карта:')
    player_card.print_lotto_card()
    print(f'{master_card.name} - Ваша карта:')
    master_card.print_lotto_card()
    barrel = Barrels.next_barrel(game_barrels)
    print('Выпало число -> ', barrel)
    while True:
        choice = input('Зачеркнуть(1)/ продолжить(2)')
        if choice == '1' or choice == '2':
            break
        else:
            print('Сделайте выбор')
    if choice == '1':
        if barrel in player_card.lotto_card:
            player_card.crossout_num(barrel)
            player_card.remaining_num -= 1
            if barrel in master_card.lotto_card:
                master_card.crossout_num(barrel)
                master_card.remaining_num -= 1
        else:
            print(f'Вы ошиблись, выиграл {master_card.name}')
            break
    if choice == '2':
        if barrel in player_card.lotto_card:
            print(f'Вы ошиблись, выиграл {master_card.name}')
            break
        else:
            if barrel in master_card.lotto_card:
                master_card.crossout_num(barrel)
                master_card.remaining_num -= 1
    if player_card.remaining_num == 0:
        print(f'Выиграл {player_card.name}')
        break
    if master_card.remaining_num == 0:
        print(f'Выиграл {master_card.name}')
        break
    print(f'{player_card.name} у Вас осталось -> {player_card.remaining_num} <- чисел    ------    {master_card.name}'
          f' -> у Вас осталось -> {master_card.remaining_num} <- чисел')
print('Отличная игра!')
