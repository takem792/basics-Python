class Person:
    def __init__(self, name='none', health=0, attack=0, armor=1.0):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor

    def _pers_attack(self, def_armor):
        damage = round(self.attack/def_armor, 0)
        return damage

    def damage(self, def_armor):
        return self._pers_attack(def_armor)

    def pers_damage(self, att_attack):
        self.health -= att_attack
        return self.health


class Fight:
    def __init__(self, who_attack, who_def):
        self.who_attack = who_attack
        self.who_def = who_def
        self.attack()

    def attack(self):
        self.who_def.pers_damage(self.who_attack.damage(self.who_def.armor))


player = Person('player', 100, 25, 1.4)
enemy = Person('enemy', 80, 30, 1.2)
while True:
    fight = Fight(player, enemy)
    if fight.who_def.health <= 0:
        print(f'{fight.who_attack.name} победил c {fight.who_attack.health} здоровья')
        break
    else:
        fight = Fight(enemy, player)
        if fight.who_def.health <= 0:
            print(f'{fight.who_attack.name} победил c {fight.who_attack.health} здоровья')
            break
