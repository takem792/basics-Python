class Car:
    def __init__(self, name='машина', color='белая', speed=0, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self._signal()

    def _signal(self):
        if self.is_police:
            print('Иу-Иу-Иу')

    def go(self):
        print(f'{self.name} {self.color} поехала со скоростью {self.speed}')

    def stop(self):
        print(f'{self.name} {self.color} остановилась')

    def turn(self, direction):
        print(f'{self.name} {self.color} повернула {direction}')


class WorkCar(Car):
    pass


class TownCar(Car):
    pass


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


my_car1 = PoliceCar('Волга', 'синяя', 60)
my_car1.go()
