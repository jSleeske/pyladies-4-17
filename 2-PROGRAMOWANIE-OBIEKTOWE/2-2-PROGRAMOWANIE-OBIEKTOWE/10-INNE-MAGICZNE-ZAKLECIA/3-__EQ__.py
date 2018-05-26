'''
Wykorzystajmy naszą klasę Book z pliku __STR__.py

>>> class Book:
>>>     def __init__(self, author, title, page_count, price):
>>>         self.author = author
>>>         self.title = title
>>>         self.page_count = page_count
>>>         self.price = price

>>>     def __str__(self):
>>>         return f'Book info: {self.title} by {self.author}'

Stworzyliśmy sobie także 2 nowe obiekty tej ksiązki:
>>> book1 = Book('A. Sapkowski', 'Krew Elfów', 235, 15.67)
>>> book2 = Book('A. Sapkowski', 'Krew Elfów', 235, 15.67)

Następnie chcieliśmy sprawdzić czy w rzeczywistości są takie same.

print(book1 == book2)
False

Co za los! Pomimo tego, że nasze książki pozornie wydają się takie same,
to jednak użycie operatora równości zwróciło False.

Dlaczego tak się stało? Domyślnie operator równości (==) sprawdza, czy dwie
zmienne (po jego lewej i prawej stronie wskazują na ten sam obiekt).

Jeśli chcemy nadpisać działanie w/w operatora, musimy nadpisać metodę __eq__.

Metoda __eq__ przyjmuje 2 argumenty:
    - self -> który wskazuje na obiekt PO LEWEJ stronie operatora równości.
    - other -> wskazuje na obiekt po prawej stronie operatora.

Kiedy więc wykonujemy:
>>> book1 == book2

to jest to równoznaczne z:
>>> book1.__eq__(book2)

W poniższym przykładzie, operator == na dwóch obiektach klasy Book zwróci
True, jeśli obie książki będą miały tak sam tytuł i autora.
'''


class Book:
    def __init__(self, author, title, page_count, price):
        self.author = author
        self.title = title
        self.page_count = page_count
        self.price = price

    def __str__(self):
        return f'Book info: {self.title} by {self.author}'

    def __eq__(self, other):
        same_author = self.author == other.author
        same_title = self.title == other.title

        return same_author and same_title


book1 = Book('A. Sapkowski', 'Krew Elfów', 235, 15.67)
book2 = Book('A. Sapkowski', 'Krew Elfów', 235, 15.67)

print(book1 == book2)

'''
W ten sposób możemy nadpisać każdy operator, pamietając o tym, że odpowiednia
metoda w klasie przyjmuje dwa argumenty, self oraz other:

OPERATOR  |  METODA
   ==        __eq__ (EQuals)
   >=        __ge__ (Greater than or Equal)
   <=        __le__ (Less than or Equal)
   >         __gt__ (GreaTer than)
   <         __le__ (LEss than)
   !=        __ne__ (Not Equal) -> domyślna implementacja wywołuje __eq__ i
                                   zwraca odwrotność!
'''
