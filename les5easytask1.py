class WorkCar:
    def __init__(self, name='машина', color='белая', speed=0, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} {self.color} поехала со скоростью {self.speed}')

    def stop(self):
        print(f'{self.name} {self.color} остановилась')

    def turn(self, direction):
        print(f'{self.name} {self.color} повернула {direction}')


class TownCar:
    def __init__(self, name='машина', color='белая', speed=0, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} {self.color} поехала со скоростью {self.speed}')

    def stop(self):
        print(f'{self.name} {self.color} остановилась')

    def turn(self, direction):
        print(f'{self.name} {self.color} повернула {direction}')


class SportCar:
    def __init__(self, name='машина', color='белая', speed=0, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} {self.color} поехала со скоростью {self.speed}')

    def stop(self):
        print(f'{self.name} {self.color} остановилась')

    def turn(self, direction):
        print(f'{self.name} {self.color} повернула {direction}')


class PoliceCar:
    def __init__(self, name='машина', color='белая', speed=0, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.signal()

    def signal(self):
        if self.is_police:
            print('Иу-Иу-Иу')

    def go(self):
        print(f'{self.name} {self.color} поехала со скоростью {self.speed}')

    def stop(self):
        print(f'{self.name} {self.color} остановилась')

    def turn(self, direction):
        print(f'{self.name} {self.color} повернула {direction}')


my_car1 = SportCar('Порше', 'синяя', 160)
my_car1.go()
