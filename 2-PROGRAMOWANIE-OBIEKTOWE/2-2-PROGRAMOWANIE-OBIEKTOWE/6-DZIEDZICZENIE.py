'''
Po głębokiej wodzie, czas na głębszą wodę - dziedziczenie.
Jeden z filarów programowania obiektowego, temat niełatwy,
ale pozwalający pisać czysty i zwięzły kod.

Samo słowo dziedzieczenie, jest już w miarę mówiące - dostajemy
coś po czymś 'w spadku'. W przypadku Pythona, otrzymujemy właśnie
cechy i metody obiektu po którym dziedziczymy.

Skoro i tak jesteśmy na głębokiej wodzie, to po raz kolejny zacznijmy od
przykładu:
'''


class Book:
    def __init__(self, author, title, price):
        self.author = author
        self.title = title
        self.price = price

    def info(self):
        return f'Book info: {self.title} by {self.author}'


class Audiobook(Book):
    pass


class Paperbook(Book):
    pass


'''
Znowu stworzyliśmy sobie klasę Book, ale z drobnymi
modyfikacjami - usunęliśmy z metody __init__
informację o ilości stron.

Poniżej zdefiniowaliśmy dwie nowe klasy - Audiobook oraz
Paperbook, które dziedziczą po klasie Book.

Kiedy chcemy wskazać, że jakiś obiekt dziedziczy po innym,
to w nawiasach okrągłych musimy podać po jakich klasach
nasz nowy obiekt ma właśnie dziedziczyć.

Klasa dziedzicząco bywa nazywana:
- dziedziczącą (inheriting class)
- dzieckiem (child class)
- podklasą (subclass)

Klasa po której dziedziczą inne klasy nazywana jest:
- rodzicem (parent class)
- nadklasą (superclass)

Sprawdźmy zatem, czy faktycznie, klasy Audiobook i Paperbook
odziedziczyły cechy i metody po obiekcie Book.
'''

audiobook = Audiobook('A. Sapkowski', 'Krew Elfów', 15.67)
paperbook = Paperbook('J.K. Rowling', 'Harry Potter i Komnata Tajemnic', 25.99)

print(audiobook.info())
print(paperbook.title)

'''
Działa! Nowe klasy dziedziczące, mogą korzystać z całej logiki
oferowanej przez klasę-rodzica.

Ale zaraz, zaraz. W podklasach nie zdefiniowaliśmy metody __init__,
a program i tak działa, chociaż w plku 3-MAGICZNE-SELF.py napisane jest,
że ten 'tajemniczy mechanizm' wywołuje metodę __init__ klasy, którą
właśnie stworzył. O co chodzi?

Odp. Magiczna metoda __init__, tak jak każda inna też jest dziedziczona.
Jeśli więc jej nie nadpiszemy, to domyślnie zostanie wywołana ta, którą
odziedziczymy.
'''
