'''
    Klasa to pewien szablon/plan według którego tworzone są instancje
    danej klasy. Sama w sobie nie zawiera żadnych konretnych danych,
    a jedynie informacje o atrybutach i metodach jakie będzie 
    miał do dyspozycji każdy stworzony obiekt danej klasy.
'''
'''
    Obiekt to instancja danej klasy zawierająca konkretne dane, 
    czyli przypisane wartości do atrybutów.
    Jeśli zdefiniujemy klasę Samochód z atrybutami marka, model,
    to obiekt tej klasy pod atrybutem marka może mieć wartość np.
    'Mercedes-Benz', 'Fiat', a pod atrybutem model - 'SLS', 'Punto'.
'''


class Person:
    '''
        Minimalna definicja klasy. Używamy słowa kluczwego class, a nazwę
        klasy zapisujemy zaczynająć słowa od wielkich liter.
    '''
    pass


if __name__ == '__main__':
    '''
        W tym miejscu nastepuje stworznie nowego obiektu klasy Person.
        Zmienna person wskazuje na konkretny instancję klasy Person.
    '''
    person = Person()

    '''
        Ustawmy wartości atrybutów...
    '''
    person.name = 'John'
    person.age = 45
    person.sex = 'male'
    person.occupation = 'janitor'

    print(
        person.name,
        person.age,
        person.sex,
        person.occupation,
    )

    '''
        Wygląda całkiem podobnie do wyciągania wartości ze słownika?
        Tak! Nie trzeba przy tym uzywać nawiasów albo metody get() ;)
    '''
