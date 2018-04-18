'''
    class Person:
        pass

    if __name__ == '__name__':
        person = Person()
        person.name = 'John'
        person.age = 45
        person.sex = 'male'
        person.occupation = 'janitor'

        other_person = Person()
        other_person.name = 'Kate'
        other_person.age = 34
        other_person.sex = 'female'
        Other_person.occupation = 'teacher'

        yet_another_person = Person()
        yet_another_person.name = 'Rick'
        yet_another_person.age = 17
        yet_another_person.sex = 'male'
        yet_another_person.occupation = 'student'
'''

'''
    Powyższy kod nie wygląda zbyt czysto ani zwięźle. Dla każdego nowego obiektu
    przypisujemy do 4 atrybutów dane. Nawet wykonując taki kod w pętli
    nie rozwiązujemy naszego problemu, bo jeśli w innym miejscu programu będziemy 
    musieli stworzyć nowy obiekt danej klasy, to czeka nas przepisywanie wszystkiego
    od nowa :(

    Jak temu zaradzić?

    Magiczną metodą __init__()
'''

'''
    __init__(), to taka specjalna metoda (funkcja 'należąca' do obiektu),
    która zostanie wykonana tylko raz dla każdego obiektu - tuż po jego
    utworzeniu. Możemy do niej przekazać argumenty i dalej zainicjalizować
    nimi obiekt. 
'''


class Person:
    def __init__(self, name, age, sex, occupation):
        '''
            __init__ to nazwa metody-konstruktora wywoływanej w czasie
            tworzenia nowego obiektu danej klasu (nie musimy tego robić
            jawnie). Argument self jest wymagany i wskazuje on na
            świeżo skonstruowany obiekt.
        '''
        self.name = name
        self.age = age
        self.sex = sex
        self.occupation = occupation


if __name__ == '__main__':
    '''
        Argument self jest przekazywany niejawnie - nie musimy się nim martwić.
        Jest natomiast jawnie odbierany - czyli deklarujemy go w metodzie __init__
        jako pierwszy argument.
    '''
    a_person = Person('John', 45, 'male', 'janitor')

    print(
        a_person.name,
        a_person.age,
        a_person.sex,
        a_person.occupation,
    )
