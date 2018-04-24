class Audiobook:
    '''
    Przykładowa klasa Audiobook
    tytuł, author, cena, długość, narrator.
    Powinna być zawsze dostępna!
    '''

    def __init__(self, title, author, price, hours,
                 minutes, seconds, narrator):
        self.title = title
        self.author = author
        self.price = price
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.narrator = narrator

        # Opcjonalnie
        # self._is_avaiable = True

    def __str__(self):
        return '{title} by {author}'.format(
            title=self.title,
            author=self.author
        )

    def is_avaiable(self):
        return True
        # lub
        # return self._is_avaiable

    def get_length(self):
        template = '{hours} hour(s), {minutes} minute(s), {seconds} second(s)'
        return template.format(
            hours=self.hours,
            minutes=self.minutes,
            seconds=self.seconds,
        )


if __name__ == '__main__':
    # init from dict
    audiobook_details = {
        'title': 'A Study in Scarlet',
        'author': 'Arthur Conan Doyle',
        'price': 21.37,
        'hours': 3,
        'minutes': 15,
        'seconds': 27,
        'narrator': 'Sir David Attenborough',
    }

    abook = Audiobook(**audiobook_details)
    print(abook.get_length())
