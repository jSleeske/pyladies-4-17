'''
W Pythonie poza atrybutami instancji (tymi, które inicjalizujemy
np: za pomocą self.attr_name = value, albo obj.attr_name = value)
istnieją także atrybuty klasowe. Definiuje się je najczęściej w samej
klasie, a odwołuje się do nich poprzez NazwaKlasy.nazwa_atrybutu.

Można się do nich odwołać także poprzez instancję, ale tylko wtedy jeśli
nie będzie ona posiadać własnego atrybutu o takiej samej nazwie.

Wartości atrybutów klasowych są współdzielone pomiędzy wszystkimi obiektami
danej klasy.

Uruchom i przenaalizuj poniższy kod:
'''


class Circle:
    PI = 3.14


if __name__ == '__main__':
    circle1 = Circle()
    circle2 = Circle()

    print('Stan początkowy')
    print('Circle.PI:', Circle.PI)
    print('circle1.PI: ', circle1.PI)
    print('circle2.PI: ', circle2.PI)

    Circle.PI = 5  # dla ułatwienia obliczeń

    print('Po zmianie atrybutu klasy')
    print('Circle.PI:', Circle.PI)
    print('circle1.PI: ', circle1.PI)
    print('circle2.PI: ', circle2.PI)

    circle1.PI = 1
    circle2.PI = 2

    print('Po dodaniu atrybutów instancji')
    print('Circle.PI', Circle.PI)
    print('circle1.PI: ', circle1.PI)
    print('circle2.PI: ', circle2.PI)

    del circle1.PI
    del circle2.PI
    print('Po usunięciu atrybutów instancji')
    print('Circle.PI: ', Circle.PI)
    print('circle1.PI: ', circle1.PI)
    print('circle2.PI: ', circle2.PI)
