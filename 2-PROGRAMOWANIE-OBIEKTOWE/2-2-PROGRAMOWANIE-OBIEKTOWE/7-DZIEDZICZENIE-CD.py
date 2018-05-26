'''
Ideą dziedziczenia jest wyciąganie części wspólnej kodu, tak aby możliwie
jak największe jego fragmenty nie duplikowała się w naszym programie. Ułatatwia
to wszelkie późniejsze modyfikacje oraz rozbudowę, skraca całość i zauważalnie
wpływa na czytelność.

W poprzednim przykładzie stowrzyliśmy bazową klasę Book oraz dwie podklasy -
Audiobook oraz Paperbook. Chociaż w tamtym przykładzie klasy dziedziczące
nie implementowały żadnej własnej logiki, to teraz to się zmieni. W klasie
nadrzędnej umieściliśmy informacje o autorze, tytule oraz cenie - są to cechy,
które niewątpliwie będą posiadały wszystkie książki, niezależnie od tego, czy
będą książkami papierowymi, czy w formie do osłuchu. Jakie dodatkowe cechy,
które nie występują w książkach drukowanychmogłyby posiadać audiobooki, i na
odwrót?

Dla audiobooka może być to na przykład informacja o długości oraz lektorze, a
dla ksiązki papierowej - ilość stron i informacja o tym, czy książka posiada
twardą okładkę.

Nadpiszmy więc teraz metody __init__ i zobaczmy co się stanie!
'''


class Book:
    def __init__(self, author, title, price):
        self.author = author
        self.title = title
        self.price = price

    def info(self):
        return f'Book info: {self.title} by {self.author}'


class Audiobook(Book):
    def __init__(self, author, title, price, length, lector):
        self.length = length
        self.lector = lector


class Paperbook(Book):
    def __init__(self, author, title, price, page_count, has_hardcover):
        self.page_count = page_count
        self.has_hardcover = has_hardcover


'''
Stwórzmy teraz nowe obiekty powyższych klas (wykorzystując 2 rózne style):
'''

audiobook = Audiobook(author='A. Sapkowski',
                      title='Krew Elfów',
                      price=15.67,
                      length=347,
                      lector='Piotr Fronczewski',
                      )

paperbook = Paperbook(
    'J.K. Rowling',
    'Harry Potter i Komnata Tajemnic',
    25.99,
    235,
    False,
)

'''
Na razie wszystko działa...
'''

print(audiobook.title())
'''
AttributeError: 'Audiobook' object has no attribute 'title'

BŁĄD!

Ale jak to?
Przecież klasa Book dostarcza metodę __init__, w której incjalizowany
jest atrybut title. Hmmm, dziwna sprawa, o co może chodzić?

Wróćmy na chwilę do pliku 3-MAGICZNE-SELF.py. Są tam wymienione kroki,
które wykonuje Python, podczas tworzenia nowego obiektu danej klasy.

W kroku drugim wskazane jest, że wywoływana jest metoda __init__ klasy,
której obiekt właśnie stworzyliśmy. Czy tutaj coś zawiodło?

>>> audiobook = Audiobook(author='A. Sapkowski',
>>>                       title='Krew Elfów',
>>>                       price=15.67,
>>>                       length=347,
>>>                       lector='Piotr Fronczewski'
>>>                       )

>>> audiobook.lector
Piotr Fronczewski

Hmm, czyli nie o to chodzi.

Czyli o co???

O to, że jeśli nadpiszemy metodę __init__ (lub w gruncie rzeczy jakąkolwiek
inną), to metoda z klasy nadrzędnej nie zostanie wykonana! Mamy na to wpływ,
i powinnśmy to zmieniać w zależności od efektu jaki chcielibyśmy osiągnąć.
W powyższym przypadku niewątpliwie chcemy mieć dostęp do tych wszystkich
atrybutów naszej klasy nadrzędnej (superklasy), a więc w metodzie __init__
klasy dziedziczącej musimy, już tym razem jawnie, wywołać metodę __init__
naszej superklasy.
'''
