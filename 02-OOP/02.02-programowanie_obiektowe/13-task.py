class Book:
    def __init__(self, title, author, price, pages, has_hardcover, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages
        self.has_hardcover = has_hardcover
        self.quantity = quantity

    def __str__(self):
        return '{title} by {author}'.format(
            title=self.title,
            author=self.author
        )
        # return f'{self.title} by {self.author}'

    def is_avaiable(self):
        return self.quantity > 0


'''
    Zleceniodawca projektu księgarni stwierdził, że poza książkami
    papierowymi chciałby także sprzedawać audiobooki.
    Zastanów się jakie właściwości powinny posiadać w/w obiektu, a
    następnie je zaimplementuj!
'''
