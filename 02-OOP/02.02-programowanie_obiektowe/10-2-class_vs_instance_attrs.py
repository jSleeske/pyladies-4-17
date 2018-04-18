class Circle:
    pi = 3.14


if __name__ == '__main__':
    circle1 = Circle()
    circle2 = Circle()

    print('circle1.pi: ', circle1.pi)
    print('circle2.pi: ', circle2.pi)

    Circle.pi = 5  # dla ułatwienia obliczeń

    print('Po zmianie atrybutu klasy')
    print('circle1.pi: ', circle1.pi)
    print('circle2.pi: ', circle2.pi)

    circle1.pi = 1
    circle2.pi = 2

    print('Po dodaniu atrybutów instancji')
    print('circle1.pi: ', circle1.pi)
    print('circle2.pi: ', circle2.pi)
    print('Circle.pi', Circle.pi)

    del circle1.pi
    del circle2.pi
    print('Po usunięciu atrybutów instancji')
    print('circle1.pi: ', circle1.pi)
    print('circle2.pi: ', circle2.pi)
