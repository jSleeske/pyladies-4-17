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
]


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
'''
class Book:
    def __init__(self, title, author, has_hardcover, price, pages, quantity):
        self.title = title
        self.author = author
        self.has_hardcover = has_hardcover
        self.price = price
        self.pages = pages
        self.quantity = quantity


if __name__ == '__main__':
    books = []
    for book_data in BOOKS_LIST:
        book = Book(**book_data)
        books.append(book)

    for book in books:
        print(book.title)
'''
