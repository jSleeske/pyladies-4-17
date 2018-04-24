'''
                        *WSPÓLNIE*
Wykorzystaj poniższą klasę Book i dane w postaci słownika w celu
klasy magazynu książek za pomocą którego będzie można nimi zarządzać
'''


class Book:
    def __init__(self, title, author, is_hardcovered, price, pages, quantity):
        self.title = title
        self.author = author
        self.is_hardcovered = is_hardcovered
        self.price = price
        self.pages = pages
        self.quantity = quantity

    def __str__(self):
        return f'{self.title} by {self.author}'

    def is_available(self):
        return self.quantity > 0


BOOKS_LIST = [
    {
        'title': 'Harry Potter and the Chamber of Secrets',
        'author': 'J. K. Rowling',
        'is_hardcovered': False,
        'price': 15.70,
        'pages': 358,
        'in_stock': 23,
    },
    {
        'title': 'Lord of the Rings: The Two Towers',
        'author': 'J. R. R. Tolkien',
        'is_hardcovered': False,
        'price': 21.30,
        'pages': 488,
        'in_stock': 7,
    },
    {
        'title': 'Game of Thrones',
        'author': 'George R. R. Martin',
        'is_hardcovered': True,
        'price': 24.99,
        'pages': 712,
        'in_stock': 55,
    },
    {
        'title': 'A Study in Scarlet',
        'author': 'Arthur Conan Doyle',
        'is_hardcovered': True,
        'price': 21.37,
        'pages': 234,
        'in_stock': 0,
    },
]
