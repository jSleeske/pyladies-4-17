'''
Okej, a co to za magiczne self?

Zdefiniujmy sobie w klasie metodę dodatkową metodę:
'''


class Person:
    def __init__(self, first_name, surname, age):
        self.name = first_name
        self.surname = surname
        self.age = age

    def introduce(self):
        print(f"Hi! My name is {self.name} {self.surname}",
              f"and I'm {human.age} years old."
              )


human = Person('John', 'Kowalski', 70)

'''
Uwaga, uwaga...
'''
human.introduce()
Person.introduce(human)

'''
Jak to się stało, że oba powyższe wywołania zwróciły to samo?

Czy to możliwe, że ten argument self to obiekt na którym wywoływana
jest metoda?

Dokładnie tak!

A jak to możliwe, że w tym pierwszym przypadku niczego nie musimy przekazywać?

Kiedy wywołujemy
>>> human.introduce()

to niejawnie przekazujemy do metody introduce sam obiekt human!

Obiekt na którym wywołujemy metodę jest ZAWSZE niejawnie przekazywany
jako pierwsza wartość do wywoływanej metody.

Dlatego wywołując daną metodę nie musimy sami tego robić - zostanie to
zrobione za nas. Jedyne co musimy przekazać to pozostałe argumenty
(ale tylko wtedy jeśli metoda ich wymaga).

Tak w ogóle to metoda oznacza tutaj po prostu funkcję, którę
wywołujemy na obiekcie/instancji (a więc za pomocą notacji z kropką).

Czyli podążąjąc tą logiką...
kiedy tworzymy nowy obiekt i przekazujemy mu argumenty:

>>> human = Person('John', 'Kowalski', 70)

to:
1. Pewien mechanizm o którym na razie nie wiecie tworzy nowy obiekt klasy
   Person.
2. Następnie wywoływana jest metoda __init__ klasy Person, do której jako
   pierwszy argument przekazywany jest dopiero co stworzony obiekt, a
   następnie wszystkie argumenty, które przekazaliśmy my (czyli w tym przypadku
   'John', 'Kowalski' oraz 70).
3. Metoda __init__ nic nie zwraca. Natomiast mechanizm, który stworzył nasz
   obiekt i wywołał niejawnie metodę __init__ zwraca nam w pełni
   zainicjalizowany obiekt!

   Woooohooo!

   Podsumowując, tworząc nową metodę w klasie ZAWSZE jako pierwszy argument w
   definicji podajemy self, a następnie wszystkie inne argumenty.
   Natomiast przy wywołaniu metody na obiekcie nie musimy podawać tego
   pierwszego argumentu. Zostanie on przekazany niejawnie.

   Przykład:

>>> class Car:
>>>     def __init__(self, name):
>>>         self.name = name

>>>     def make_sound(self, sound):
>>>         print(f'{self.model} goes {sound}')

>>> a_car = Car('Fiat Punto')
>>> a_car.make_sound('Bruuuuuum!')
'''
