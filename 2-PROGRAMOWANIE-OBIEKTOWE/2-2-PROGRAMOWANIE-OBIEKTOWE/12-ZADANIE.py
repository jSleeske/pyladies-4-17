'''
Stwórz klasę Kształt, posiadającą metodę abstrakcyjną get_area(),
a następnie zaimplementuj klasy: Trójkąt, Prostokąt oraz Koło,
które będą nadpisywały w/w metodę, tak aby zwracać poprawny
wynik obliczeń dla odpowiedniej figury geometryczne.

Nie zapomnij o implementacji odpowiednich metod __init__,
które będą przyjmowały odpowiednie atrybuty w zależności od
klasy (wysokość, szerokośc, promień itd.)
'''


class Shape:
    def get_area(self):
        raise NotImplementedError('Override this method in inheriting class!')


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return self.base * self.height / 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Circle(Shape):
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return Circle.PI * (self.radius ** 2)


if __name__ == '__main__':
    shapes = [
        Triangle(base=24, height=14),
        Rectangle(width=20, height=60),
        Circle(radius=12.5),
    ]

    for shape in shapes:
        print(f'{shape.__class__.__name__} area: {shape.get_area()}')
