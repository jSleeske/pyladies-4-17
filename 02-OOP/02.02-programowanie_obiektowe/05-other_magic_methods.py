'''
    __init__ jest tylko jedną z wielu 'magicznych' metod 
    dostępnych do wykorzystania! Inną jest __str__ dzięki 
    której uzyskamy czytelną reprezentację tekstową naszego
    obiektu.
'''


class Person:
    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #     return 'Hi, mu name is {name}'.format(name=self.name)


if __name__ == '__main__':
    person = Person('Joe')
    '''
        Z zakomentowanym powyżej fragmentem kodu otzymamy coś
        podobnego: <__main__.Person object at 0x7f0b8b285a90>
        Mało czytelne, prawda? 
        Odkomentuj i zobacz jak zmienił się wynik!
    '''
    print(person)
