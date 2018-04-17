'''
    Klasa to pewien szablon/plan według którego tworzone są obiekty
    danej klasy. Sama w sobie nie zawiera żadnych konretnych danych,
    a jedynie informacje o właściwościach i funkcjach jakie będzie 
    miał do dyspozycji każdy obiekt.
'''
'''
    Obiekt to instancja danej klasy zawierająca konkretne dane, 
    czyli przypisane wartości do właściwości.
    Jeśli zdefiniujemy klasę Samochód z właściwościami marka, model,
    to obiekt tej klasy pod właściowością marka może mieć wartość np.
    'Mercedes-Benz', 'Fiat', a pod właściwością model - 'SLS', 'Punto'.
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
        Zmienna person wskazuje na konkretny obiekt klasy Person.
    '''
    person = Person()

    '''
        Ustawmy jakieś właściwości...
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
        Tak! Nie trzeba przy tym uzywać tych paskudnych nawiasów albo 
        metody get() ;)
    '''
