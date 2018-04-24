'''
Przenalizuj poniżesze dwie klasy, a następnie zrefaktoryzuj kod,
tak aby spełniał zasady DRY.
'''


class Paperbook:
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

    def is_avaiable(self):
        return self.quantity > 0

    def get_pages_count(self):
        return 'Book length: {pages} pages'.format(pages=self.pages)


class Audiobook:
    def __init__(self, title, author, price, hours,
                 minutes, seconds, narrator):
        self.title = title
        self.author = author
        self.price = price
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.narrator = narrator
        self._is_avaiable = True

    def __str__(self):
        return '{title} by {author}'.format(
            title=self.title,
            author=self.author
        )

    def is_avaiable(self):
        return self._is_avaiable

    def get_time(self):
        template = (
            'Book length: {hours} hour(s)'
            '{minutes} minute(s), {seconds} second(s)'
        )

        return template.format(
            hours=self.hours,
            minutes=self.minutes,
            seconds=self.seconds,
        )
