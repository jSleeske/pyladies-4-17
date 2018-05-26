'''
Stwórz klasę Książka, która będzie posiadała następujące atrybuty:
autor, tytuł, liczba stron, cena (przekazywane w metodzie __init__)
oraz metodę info() która nie przyjmuje żadnych dodatkowych parametrów,
a zwróci informacje o tytule i autorze.

Stwórz dwa obiekty tej klasy i wywołaj na nich metodę info.
'''


class Book:
    def __init__(self, author, title, page_count, price):
        self.author = author
        self.title = title
        self.page_count = page_count
        self.price = price

    def info(self):
        return f'Book info: {self.title} by {self.author}'


book1 = Book('A. Sapkowski', 'Krew Elfów', 235, 15.67)
book2 = Book('J.K. Rowling', 'Harry Potter i Komnata Tajemnic', 170, 25.99)

print(book1.info())
print(book2.info())
