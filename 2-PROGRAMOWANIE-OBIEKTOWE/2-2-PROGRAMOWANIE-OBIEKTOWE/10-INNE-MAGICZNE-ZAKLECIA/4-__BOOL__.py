'''
Ponownie wykorzystajmy model książki, dodając do niego dodatkowy atrybut,
quantity, przechowujący informację o ilości egzemplarzy danej książki.

Nastepnie dopiszmy nową metodę - __bool__, która będzie zwracała True,
jeśli liczba egzemplarzy będzie większa od 0 oraz False w przeciwnym razie.
'''


class Book:
    def __init__(self, author, title, page_count, price, quantity):
        self.author = author
        self.title = title
        self.page_count = page_count
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Book info: {self.title} by {self.author}'

    def __eq__(self, other):
        same_author = self.author == other.author
        same_title = self.title == other.title

        return same_author and same_title

    def __bool__(self):
        return self.quantity > 0


'''
Stwórzmy teraz dodatkową funkcję, która sprawdza, czy dany dana książka
jest dostępna:
'''


def is_available(book):
    if book:
        print('Given book is available')
    else:
        print('Book currently unavailable')


'''
Czas na nową książkę, w 100 egzemplarzach:
'''

book1 = Book('A. Sapkowski', 'Krew Elfów', 235, 15.67, 100)
is_available(book1)

book1.quantity = 0
is_available(book1)

'''
Działa!

Należy się tylko zastanowić, czy takie a nie inne zastosowanie
metody __bool__ ma sens.


>>> if book:
>>>     ...

Powyższy zapis nie pozwoli nam się od razu zorientować, że pod spodem
sprawdzana jest ilość egzemplarzy, i może sprawić, że kod bedzie mniej
czytelny.
'''
