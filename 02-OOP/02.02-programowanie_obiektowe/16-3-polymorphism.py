'''
Inny przykład polimorfizmu
'''


class Car:
    def __init__(self, brand, model, max_speed):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed

    def drive(self):
        raise NotImplementedError('Car is abstract, cannot drive!')


class SportCar(Car):
    def drive_at_max_speed(self):
        return '{brand} {model} at {speed} kmph goes vroooom!'.format(
            brand=self.brand,
            model=self.model,
            speed=self.max_speed,
        )


class Truck(Car):
    def drive_at_max_speed(self):
        return '{brand} {model} at {speed} kmph goes broooom!'.format(
            brand=self.brand,
            model=self.model,
            speed=self.max_speed
        )


def go_to_spain(car):
    print(car.drive_at_max_speed())


if __name__ == '__main__':
    sport_car = SportCar('Ferrari', 'Aventador', 320)
    truck = Truck('Scania', 'R 730', 95)

    go_to_spain(sport_car)
    go_to_spain(truck)
