'''
Czas na małą poparawkę w naszym kodzie:


>>> class Book:
>>>     def __init__(self, author, title, price):
>>>         self.author = author
>>>         self.title = title
>>>         self.price = price

>>>     def info(self):
>>>         return f'Book info: {self.title} by {self.author}'

>>> class Audiobook(Book):
>>>     def __init__(self, author, title, price, length, lector):
>>>         super().__init__(author, title, price)
>>>         self.length = length
>>>         self.lector = lector

>>> class Paperbook(Book):
>>>     def __init__(self, author, title, price, page_count, has_hardcover):
>>>         super().__init__(author, title, price)
>>>         self.page_count = page_count
>>>         self.has_hardcover = has_hardcover


>>> audiobook = Audiobook(author='A. Sapkowski',
>>>                       title='Krew Elfów',
>>>                       price=15.67,
>>>                       length=347,
>>>                       lector='Piotr Fronczewski',
>>>                       )

>>> paperbook = Paperbook(
>>>     'J.K. Rowling',
>>>     'Harry Potter i Komnata Tajemnic',
>>>     25.99,
>>>     235,
>>>     False,
>>> )

>>> print(audiobook.info())
>>> print(paperbook.title)


Sukces! Teraz mamy dostęp do poprawnie zinicjalizowanych atrybutów z klasy
nadrzędnej!

A o co chodzi z tym super().__init__()?

super() pozwala odwołać się do metod klasy nadrzędnej z zachowaniem konktestu.
W tym przypadku kontektem jest to, że jako parametr self zostanie przekazany
stworzony już obiekt klasy Audiobook albo Paperbook, a nie na przykład nowy
obiekt klasy Book.

Taki zapis:
>>> class A(B):
>>>     def __init(self, ...):
>>>         super().__init__(...)

jest równoznaczny z takim:
>>> class A(B):
>>>     def __init(self, ...):
>>>         B.__init__(self, ...)


Fantastycznie! Nadal jednak jest tutaj coś co możnaby poprawić. Metody __init__
w klasie dziedziczącej nie powinno interesować jakie i ile wartości przyjmuje
klasa nadrzędna (o ile ich nie modyfikuje). Przepisywanie ich wszystkich może
być żmude, prowadzić do błędów i sprawia, że w przypadku zmiany czegoś w klasie
nadrzędnej należałoby to poprawić w klasach dziedziczących! WSZYSTKICH! Brrrrr.

Musi istnieć lepszy sposób:
'''


class Book:
    def __init__(self, author, title, price):
        self.author = author
        self.title = title
        self.price = price

    def info(self):
        return f'Book info: {self.title} by {self.author}'


class Audiobook(Book):
    def __init__(self, length, lector, *args, **kwargs):
        print('In Audiobook __init__')
        print('ARGS:', args)
        print('KWARGS:', kwargs)
        super().__init__(*args, **kwargs)
        self.length = length
        self.lector = lector


print('Tworzę nowy obiekt klasy Audiobook, używając kluczy')
audiobook = Audiobook(author='A. Sapkowski',
                      title='Krew Elfów',
                      price=15.67,
                      length=347,
                      lector='Piotr Fronczewski',
                      )


print(audiobook.info(), '\n\n\n')

'''
Działa!

Ale znowu... co tu się stało?
Spójrzmy na metodę __init__ klasy Audiobook.
Przyjmuje ona teraz argument self - czyli sam obiekt,
length, lector, oraz:
*args -> czyli nieokreśloną liczbę argumentów bez kluczy (tuplę).
**kwargs -> czyli nieokreśloną liczbę argumentów z kluczami (słownik).

W momencie tworzenia nowego obiektu:

>>> audiobook = Audiobook(author='A. Sapkowski',
>>>                       title='Krew Elfów',
>>>                       price=15.67,
>>>                       length=347,
>>>                       lector='Piotr Fronczewski',
>>>                       )

Przekazujemy parametry razem z kluczami, dzięki czemu
w metodzie __init__ przechwytujemy wartości dla parametrów
length oraz lector, a pozostałe, jako, że przekazane w postaci
klucz wartość trafiają do parametru kwargs.

Jeśli stworzymy nowy obiekt bez uzywania kluczy:

>>> audiobook = Audiobook(347,
>>>                       'Piotr Fronczewski',
>>>                       'A. Sapkowski',
>>>                       'Krew Elfów',
>>>                       15.67,
>>>                       )

To musimy się upewnić, że przekazujemy wartości
parametrów w dobrej kolejności - najpierw length
oraz lector, a potem reszta. W takim przypadku, jeśli
przekazaliśmy wartości bez kluczy trafią one do parametru
args, a parametr kwargs pozostanie pusty.
'''

print('Tworzę nowy obiekt klasy Audiobook, nie używając kluczy')
audiobook = Audiobook(347,
                      'Piotr Fronczewski',
                      'A. Sapkowski',
                      'Krew Elfów',
                      15.67,
                      )
print('\n\n\n')

'''
Analogicznie, kiedy uzywamy stylu mieszanego, musimy upewnić się, że
wartości bez kluczy przekazujemy JAKO PIERWSZE, a dopiero potem wartości
z kluczami.

Na przykład:

>>> audiobook = Audiobook(347,
>>>                       'Piotr Fronczewski',
>>>                       author='A. Sapkowski',
>>>                       'Krew Elfów',
>>>                       15.67,
>>>                       )

Zwróci błąd - Python nie będzie wiedział jak przypisać wartości
bez kluczy, nawet jeśli liczba wartości będzie odpowiadać liczbie
parametrów.

Poprawny przykład:
'''

print('Tworzę nowy obiekt klasy Audiobook',
      'używając stylu mieszanego - keyworded args na końcu'
      )
audiobook = Audiobook(347,
                      'Piotr Fronczewski',
                      'A. Sapkowski',
                      title='Krew Elfów',
                      price=15.67,
                      )

'''
Dzięki takiemu podejściu, metodę __init__ klas dziedziczących interesuje
tylko to, czy dostały parametry, których wymagają do poprawnego
zaincjalizowania obiektu 'na swoim poziomie', pozostałe przekazane
paramtery przekazują 'wyżej' gdzie kolejna wartstwa logiki, sprawdza,
czy dostała to czego potrzebuje. I tak dalej!
'''
