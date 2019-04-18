

class Barrels:

    @staticmethod
    def create_barrels():
        barrels = []
        for i in range(1, 91):
            barrels.append(i)
        return barrels

    @staticmethod
    def next_barrel(barrels, num):
        return barrels.pop(num)


class LottoCard:
    @staticmethod
    def create_card():
        barrels_for_card = Barrels.create_barrels()
        lotto_card = []
        it = 0
        while it < 15:
            num = random.randint(0, 26)
            if not lotto_card[num]:
                lotto_card[num] = barrels_for_card
                it += 1




#генерация игры
import random
new_barrels = Barrels.create_barrels()
print(new_barrels)
# тянем бочонки
while len(new_barrels) > 1:
    Barrels.next_barrel(new_barrels)
print('last barrel - ', new_barrels)
