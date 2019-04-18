import random


class Barrels:

    @staticmethod
    def create_barrels():
        barrels = []
        for i in range(1, 91):
            barrels.append(i)
        return barrels

    @staticmethod
    def next_barrel(barrels):
        return barrels.pop(random.randint(0, len(barrels)-1))


class LottoCard:
    @staticmethod
    def _create_card_line(lotto_card, barrels_for_card, start, finish):
        it = 0
        while it < 5:
            num = random.randint(start, finish)
            barrel_num = random.randint(0, len(barrels_for_card)-1)
            if lotto_card[num] == '':
                lotto_card[num] = barrels_for_card[barrel_num]
                barrels_for_card.pop(barrel_num)
                it += 1

    @staticmethod
    def create_card():
        barrels_for_card = Barrels.create_barrels()
        lotto_card = ["", "", "", "", "", "", "", "", "",
                      "", "", "", "", "", "", "", "", "",
                      "", "", "", "", "", "", "", "", ""]
        LottoCard._create_card_line(lotto_card, barrels_for_card, 0, 8)
        LottoCard._create_card_line(lotto_card, barrels_for_card, 9, 17)
        LottoCard._create_card_line(lotto_card, barrels_for_card, 18, 26)
        return lotto_card

    @staticmethod
    def _print_lotto_card_line(lotto_card, start, finish):
        for i in range(start, finish):
            print('|', end='')
            if lotto_card[i] == '':
                print('    ', end='')
            else:
                if len(str(lotto_card[i])) < 2:
                    print(f'  {lotto_card[i]} ', end='')
                else:
                    print(f' {lotto_card[i]} ', end='')
        print('|')

    @staticmethod
    def print_lotto_card(lotto_card):
        print(' --------------------------------------------')
        LottoCard._print_lotto_card_line(lotto_card, 0, 9)
        LottoCard._print_lotto_card_line(lotto_card, 9, 18)
        LottoCard._print_lotto_card_line(lotto_card, 18, 27)
        print(' --------------------------------------------')

    @staticmethod
    def crossout_num(lotto_card, barrel):
        lotto_card.insert(lotto_card.index(barrel), "XX")
        lotto_card.remove(barrel)


#генерация игры
game_barrels = Barrels.create_barrels()
player_card = LottoCard.create_card()
master_card = LottoCard.create_card()
player_remaining_num = 15
master_remaining_num = 15
# тянем бочонки
while True:
    print('Ваша карта:')
    LottoCard.print_lotto_card(player_card)
    print('Карта мастера игры:')
    LottoCard.print_lotto_card(master_card)
    barrel = Barrels.next_barrel(game_barrels)
    print('Выпало число -> ', barrel)
    while True:
        choice = input('Зачеркнуть(1)/ продолжить(2)')
        if choice == '1' or choice == '2':
            break
        else:
            print('Сделайте выбор')
    if choice == '1':
        if barrel in player_card:
            LottoCard.crossout_num(player_card, barrel)
            player_remaining_num -= 1
            if barrel in master_card:
                LottoCard.crossout_num(master_card, barrel)
                master_remaining_num -= 1
        else:
            print('Вы ошиблись, выиграл Мастер игры')
            break
    if choice == '2':
        if barrel in player_card:
            print('Вы ошиблись, выиграл Мастер игры')
            break
        else:
            if barrel in master_card:
                LottoCard.crossout_num(master_card, barrel)
                master_remaining_num -= 1
    if player_remaining_num == 0:
        print('Выиграл Игрок')
        break
    if master_remaining_num == 0:
        print('Выиграл Мастер игры')
        break
print('Отличная игра!')
