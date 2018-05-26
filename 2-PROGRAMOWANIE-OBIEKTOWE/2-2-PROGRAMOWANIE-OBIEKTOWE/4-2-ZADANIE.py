'''
Wykorzystując dane zawarte w liście BOOK_DATA i klasę Book z
poprzedniego ćwiczenia stwórz 3 obiekty klasy książka inicjalizując
je danymi ze wspomnianego słownika. Wykorzystaj tutaj kwargsy (więcej
o nich w części 1-1).
'''

BOOK_DATA = [
    {
        'title': 'Harry Potter i Komnata Tajemnic',
        'author': 'J.K. Rowling',
        'page_count': 170,
        'price': 25.99,
    },
    {
        'title': 'Krew Elfów',
        'author': 'A. Sapkowski',
        'page_count': 235,
        'price': 15.67,
    },
    {
        'title': 'Winds of Winter',
        'author': 'George R. R. Martin',
        'page_count': 578,
        'price': 34.99,
    },
]


class Book:
    def __init__(self, author, title, page_count, price):
        self.author = author
        self.title = title
        self.page_count = page_count
        self.price = price

    def info(self):
        return f'Book info: {self.title} by {self.author}'


if __name__ == '__main__':
    books = []

    for data in BOOK_DATA:
        book = Book(**data)
        books.append(book)

    for book in books:
        print(book.info())
