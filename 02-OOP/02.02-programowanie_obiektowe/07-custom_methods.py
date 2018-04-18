'''
    Tak jak zostało to wspomniane klasy to zbiór nie tylko
    atrybutów (danych) ale i metod (funkcji), które na tych danych operują.

    Nie jesteśmy w żaden sposób ograniczeni jeśli chodzi o dodawanie
    własnych metod do klas. Musimy tylko pamiętać, o tym dodatkowym
    argumencie 'self', którego nie podajemy przy wywołaniu metody ;)
'''


class Car:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def drive(self, road_name):
        '''
            Metoda drive(), która przyjmuje dodatkowy parametr
            w postaci nazwy drogi, po której porusza się samochód.
        '''
        print('Driving on {road} at {speed} kmph'.format(
            speed=self.max_speed,
            road=road_name,
        ))


if __name__ == '__main__':
    ferrari = Car(max_speed=330)
    ferrari.drive('State Highway')
