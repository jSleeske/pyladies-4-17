'''
    Przykład dynamicznego dodawnia metod i właściwości do klasy
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

    # del SimpleClass.hello
    # simple.hello()

'''
    Dlaczego i jak to w ogóle działa?
    W Pythonie wszystko jest obiektem - w tym funkcje ;)
    Skoro więc możemy przekazać obiekt typu str czy bool, to dlaczego
    miałoby to wyglądać inaczej dla obiektu funkcji? ;)
'''
