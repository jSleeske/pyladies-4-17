class Book:
    def __init__(self, title, author, has_hardcover, price, pages, quantity):
        self.title = title
        self.author = author
        self.has_hardcover = has_hardcover
        self.price = price
        self.pages = pages
        self.quantity = quantity

    def is_avaiable(self):
        return self.quantity > 0


'''
    Zleceniodawca projektu księgarni stwierdził, że poza książkami
    papierowymi chciałby także sprzedawać audiobooki oraz ebooki.
    Zastanów się jakie właściwości powinny posiadać w/w obiektu, a
    następnie je zaimplementuj!
'''
