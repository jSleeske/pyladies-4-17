'''
Wow! Tyle wiedzy, że aż głowę rozsadza! Warto chyba
sobie zrobić chwilę przerwy i na spokojnie przemyśleć
co się tutaj wydarzyło do tej pory.

Jeśli jednak czujesz się jeszcze na siłach, to możesz
się właśnie zastanawiać, czy np taka klasa Book, którą
sobie wcześniej zdefiniowaliśmy, też przypadkiem po czymś
nie dziedziczy.

Jak się zapewne domyślasz - oczywiście, że tak jest i oczywiście,
że robi to niejawnie ;)

Tym, po czym dziedziczą wszystkie klasy jest object
https://docs.python.org/3/library/functions.html#object

Dzięki temu wszystkie klasy, poza logiką, którą sami stworzymy,
zapewniają szereg funkcjonalności wykorzystywanych przez wewnętrzne
mechanizmy Pythona.

Oto jak one wyglądają:

['__repr__',
 '__hash__',
 '__str__',
 '__getattribute__',
 '__setattr__',
 '__delattr__',
 '__lt__',
 '__le__',
 '__eq__',
 '__ne__',
 '__gt__',
 '__ge__',
 '__init__',
 '__new__',
 '__reduce_ex__',
 '__reduce__',
 '__subclasshook__',
 '__init_subclass__',
 '__format__',
 '__sizeof__',
 '__dir__',
 '__class__',
 '__doc__'
]

Tak, są magiczne!

A jak ich używać? Dowiesz się w części 10-INNE-MAGICZNE-ZAKLĘCIA ;)
'''
