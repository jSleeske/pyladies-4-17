'''
    Uruchom poniższy kod
'''


class Test:
    def run(self):
        self.result = 'result'


if __name__ == '__main__':
    test = Test()
    print(test.result)

'''
    Wynikiem takiej operacji będzie:
    AttributeError: 'Test' object has no attribute 'result'

    ... czyli nic przyjemnego :/

    Python jest językiem dynamicznym, dynamiczne są także obiektu,
    co oznacza, że w momencie uruchomienia programu dowolny obiekt 
    możemy zmodyfikować poprzez dodanie/usuwanie/modyfikację atrybutów
    lub metod.

    Co oznacza jedno - należy być ostrożnym ;) Zwłaszcza dokonując zmian w 
    obiektach, które pochodzą z bibliotek zewnętrznych.

    Jeśli zaś chodzi o unikanie takich błędów we własnych klasach to jedną z
    propozycji jest inicjalizacja atrybutów w konstruktorze. Nie jest to
    jednak przyjęty standard i nie brakuje też przeciwników tej metody, którzą
    twierdzą, że obowiązkiem programisty jest dbanie o to, aby w momencie 
    wywołania dowolnej metody zapewnić odpowiedni stan obiektu. 
'''

'''
    Przykład dynamicznego dodawnia metod i atrybutów do klasy
'''


class SimpleClass:
    pass


def say_hello(self):
    '''
        Funkcja say_hello zdefiniowana poza klasą
    '''
    print('Hello from {sender}'.format(sender=self.sender))


if __name__ == '__main__':
    simple = SimpleClass()
    '''
        Wygląda jak dodawanie właściwości ;) Tylko, że dodajemy do klasy a nie obiektu ;)
    '''
    SimpleClass.hello = say_hello
    '''
        Odpowiedzialność - inicjalizujemy właściwość 'sender'
        obiektu simple przed wywołaniem metody hello
    '''
    simple.sender = 'PyLadies'
    simple.hello()

'''
    Dlaczego i jak to w ogóle działa?
    W Pythonie wszystko jest obiektem - w tym funkcje ;)
    Skoro więc możemy przekazać obiekt typu str czy bool, to dlaczego
    miałoby to wyglądać inaczej dla obiektu funkcji? ;)
'''
