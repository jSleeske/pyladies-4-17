'''
Hej, to self musiała mocno zamieszać. Niestety tak
to już jest w Pythonie, co jeszcze bardziej
którego podejście do obiektów jest zdecydowanie
inne od większości popularnych języków programowania.
Przed przejściem dalej przeczytaj sobie podsumowanie tego
co było do tej pory.

Czym różni się klasa od obiektu klasy w Pythonie?

Klasa to jedynie 'szablon', który mówi nam jakie
cechy mają posiadać wszystkie obiekty tej klasy,
jakie operacje możemy na każdym obiekcie wykonać oraz
w jaki sposób jest inicjalizowany.

W przypadku klasy książka z poprzednich zadań - tymi cechami
(zwanymi także atrybutami) były: tytuł, autor, liczba stron,
i cena.

Zdefiniowaliśmy sobie także jedną operację (metodę) - info(),
które zwracała nam ładną reprezentację tekstową danego obiektu.

Stworzyliśmy także specjalną metodę __init__, w której napisaliśmy
własną logikę inicjalizowania obiektu wartościami.

Obiekt danej klasy to... po prostu obiekt, który danym
cechom przypisuje konrektne wartości. Czyli tak jak jesteście
w stanie powiedzieć, że każda książka posiada szereg cech takich jak
tytuł, autora itd. to nie jesteście w stanie ich wskazać:

>>> Book.title
AttributeError: type object 'Book' has no attribute 'title'

Bo to tak jakbyście spróbowali powiedzieć, że każda książka posiada
taki sam tytuł.

Najpierw należy stworzyć nowy obiekt danej klasy, podając jej nazwę oraz
nawiasy okrągłe, w których umieszczamy parametry - konkretne wartości dla
poszczególnych cech w formie argsów, kwargsów, lub mieszance powyższych.

>>> book1 = Book('A. Sapkowski', 'Krew Elfów', page_count=235, price=15.67)

Dopiero w takim momencie możemy odnieść się do cechy KONRETNEJ książki i
uzyskać jej tytuł:

>>> print(book1.title)
Krew Elfów

Jeśli chcecmy odwołać się do danej metody możemy to zrobić na dwa sposoby:
1. Przez instancję (obiekt) danej klasy - zazwyczaj używany:
>>> book1.info()

2. Przez klasę - ale musimy wtedy jawnie podać jako pierwszy paramter obiekt
tejże klasy:
>>> Book.info(book1)
'''
