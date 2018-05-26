'''
Jeszcze raz wykorzystajmy naszą klasę Book z zadania 4.

>>> class Book:
>>>     def __init__(self, author, title, page_count, price):
>>>         self.author = author
>>>         self.title = title
>>>         self.page_count = page_count
>>>         self.price = price

>>>     def info(self):
>>>         return f'Book info: {self.title} by {self.author}'

Stworzyliśmy sobie także nowy obiekt tej ksiązki:
>>> book1 = Book('A. Sapkowski', 'Krew Elfów', 235, 15.67)

Następnie wyprintowaliśmy sobie informacje o nim za pomocą metody info()
>>> print(book1)

A nie! Przez gapiostwo zapomnieliśmy o wywołaniu metody. Zamiast ładnego
komunikatu otrzymaliśmy coś takiego:
<__main__.Book object at 0x7f27f8b06278>

Hej, dobra wiadomość jest taka, że przynajmniej program się nie wywalił.
Oraz potrafił coś nam wyprintować! Ale skąd wiedział co i jak?
Na to pierwsze pytanie odpowiedź znajduje się w częsci 9-DZIEDZICZENIE.
Co do drugiego - dzięki specjalnej, magicznej (a jak!) metodzie __str__.

Co to za metoda i kiedy jest wywoływana - a no wtedy, kiedy na przykład
chcemy skonwertować dany obiekt na łańcuch znaków ( str(book) ). Co na
przykład próbuje zrobić metoda print - cokolwiek do niej prześlemy w postaci
argumentów, włączając wyrażenia takie jak dodawanie, wywołania innych funkcji
- koniec końców zostanie zamienione na łańcuch znaków. Chyba, że się nie da,
wtedy wasz program się wykrzaczy.

Jeśli wywołując:
>>> print(book1)

chcielibyśmy osiągnąć taki sam efekt jak wywołując
>>> print(book1.info())

to jedyne co musimy zrobić to nadpisać metodę __str__
dla danej klasy. Łatwe, proste i szeroko stosowane.
'''


class Book:
    def __init__(self, author, title, page_count, price):
        self.author = author
        self.title = title
        self.page_count = page_count
        self.price = price

    def __str__(self):
        return f'Book info: {self.title} by {self.author}'


book1 = Book('A. Sapkowski', 'Krew Elfów', 235, 15.67)

print(book1)
