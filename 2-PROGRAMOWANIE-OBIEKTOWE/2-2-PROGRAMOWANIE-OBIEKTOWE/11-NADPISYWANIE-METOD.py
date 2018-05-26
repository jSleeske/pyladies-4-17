'''
Jeśli jesteś już po części 10, to wiesz jak nadpisać wbudowane
metody dziedziczone niejawnie po klasie object.


Załóżmy, że piszmey właśnie aplikację imitującą odgłosy zwierząt.
Pozwala ona wpisać użytkownikowi nazwę zwierzęcia, a następnie
tworzy nowy obiekt i wywołuje na nim odpowiednią metodę.


>>> class Dog:
>>>     def bark(self):
>>>         print('Bark! Bark!')


>>> class Cat:
>>>     def meow(self):
>>>         print('Meow! Meow!')


>>> class Cow:
>>>     def moo(self):
>>>         print('Mooooo! Mooooo!')


>>> def make_sound(animal_name):
>>>     if animal_name == 'dog':
>>>         Dog().bark()
>>>     elif animal_name == 'cat':
>>>         Cat().meow()
>>>     elif animal_name == 'cow':
>>>         Cow().moo()

>>> while True:
>>>     animal_name = input('Animal name: ')
>>>     make_sound(animal_name)


Działa i to całkiem przyzwoicie.
Co jeśli jednak dodamy 10, 100, 1000 zwierząt?
Nasz if wydłuży się niesamowicie!
Co jeśli stwierdzimy, że koty nie robią 'Meow' tylko 'Purrr'
i postanowimy zmienić nazwę metody oraz jej implementację?
Czeka nas zmiana w 2 miejscach. Albo 1000, jeśli nasz kod się
rozrósł i używamy metody meow wielokrotnie.

Jak sobie z tym poradzić?
'''


class Animal:
    def make_sound(self):
        raise NotImplementedError(
            'Override this method in inheriting class'
        )


class Dog:
    def make_sound(self):
        print('Bark! Bark!')


class Cat:
    def make_sound(self):
        print('Meow! Meow!')


class Cow:
    def make_sound(self):
        print('Mooooo! Mooooo!')


def get_animal(animal_name):
    if animal_name == 'dog':
        return Dog()
    elif animal_name == 'cat':
        return Cat()
    elif animal_name == 'cow':
        return Cow()


def make_sound(animal_name):
    animal = get_animal(animal_name)
    animal.make_sound()


while True:
    animal_name = input('Animal name: ')
    make_sound(animal_name)


'''
Jak widać mamy tutaj jedną klasę bazową Animal, która definiuje,
ale nie implementuje metodę make_sound().

Metoda make_sound() jest częścią interfejsu. Interfejs to pojęcie o
wielu znaczeniach, ale w programowu obiektowym przyjęło się, że jest
to zestaw operacji (metod) jakie możemy wywołać na obiekcie.

Tworząc klasę bazową Animal i definiując tam metodę make_sound, możemy
'wymusić' na innych programistach jej zaimplementowanie, w klasach
dziedziczących, co oznacza, że będziemy mogli wchodzić z nimi w interakcje,
bez wiedzy o tym w jaki sposób działają one wewnętrznie.

Brzmi szalenie abstrakcyjnie, prawda?

Ale działa, i to dużo lepiej, niż poprzedni przykład.
Co prawda, nadal mamy do czynienia z długim if-em w funkcji get_animal,
natomiast dodając kolejne zwierzaki nie będziemy musieli się martwić,
jaką metodę na nich wywołać - będzie to zawsze make_sound(), a za detale
będzie odpowiadać implementacja tej funkcji w każdej konkretnej klasie.

Jest to jedno z fundamentalnych założeń programowania obektowego i każdy
programista powinien pisać kod w sposób, która sprawia, że obiekty mogą
się ze sobą komunikować bez wzajemnej wiedzy o swoich wewnętrznych mechanizmach
działania.

Więcej w temacie:

Interfejs:
https://stackoverflow.com/questions/2866987/what-is-the-definition-of-interface-in-object-oriented-programming

Loose coupling:
https://stackoverflow.com/questions/226977/what-is-loose-coupling-please-provide-examples
'''
