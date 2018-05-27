'''
Ostatnio stworzyliśmy klasę osoba
>>> class Person:
>>>     pass

a następnie stworzyliśmy instancję (obiekt)
danej klasy i nadaliśmy mu imię, nazwisko
oraz wiek.
>>> human = Person()
>>> human.name = 'John'
>>> human.surname = 'Kowalski'
>>> human.age = 70

Co jeśli postanowilibyśmy stowrzyć mu drugiego człowieczka,
żeby nie był samotny?

>>> human2 = Person()
>>> human2.name = 'Alice'
>>> human2.surname = 'Smith'
>>> human2.age = 68

Dużo powtarzania się... i w zasadzie po co nam ta cała klasa
>>> class Person:
>>>    pass

skoro praktycznie nic nie robi...

Ale może! Oraz powinna!
A co dokładnie powinna robić?
Na przykład mówić nam w jaki sposób inicjalizowane
mają być nowe obiekty danej klasy.
Do kontrolowania tego zachowania służy metoda __init__.
Tak, jest magiczna.
'''


class Person:
    def __init__(self, first_name, surname, age):
        self.name = first_name
        self.surname = surname
        self.age = age


'''
Ale zaraz, zaraz...
Co to za dziwne self na początku?
I dlaczego przypisujmey do niego różne rzeczy?

Zobaczmy jak wygląda teraz tworzenie nowego obiektu
'''

human = Person('John', 'Kowalski', 70)
human2 = Person('Alice', 'Smith', 68)

print(f"Hi! My name is {human.name} {human.surname}",
      f"and I'm {human.age} years old."
      )

print(f"Hi! My name is {human2.name} {human2.surname}",
      f"and I'm {human2.age} years old."
      )

'''
Zapis:

>>> class Person:
>>>    def __init__(self, first_name, surname, age):
>>>        self.name = first_name
>>>        self.surname = surname
>>>        self.age = age

>>> human = Person('John', 'Kowalski', 70)


jest równoważny z zapisem:


>>> class Person:
>>>    pass

>>> human = Person()
>>> human.name = 'John'
>>> human.surname = 'Kowalski'
>>> human.age = 70

Z taką różnicą, że w pierwszym przypadku zamknęliśmy tą logikę w
metodzie __init__, która jest pierwszą metodą (wywoływaną automatycznie)
po stworzeniu nowego obiektu danej klasy.

Okej, a co to za magiczne self?
'''
