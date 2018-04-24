'''
Aby uniezależnić metodę init klasy dziedziczącej
od zmian w klasie bazowej można wykorzystać **kwargsy
'''
'''
class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

class Teacher(Person):
    def __init__(self, name, age, sex, address,
                 years_of_employment, salary):
        super().__init__(name, age, sex)
        self.salary = salary


class Student(Person):
    def __init__(self, name, age, sex, grade):
        super().__init__(name, age, sex)
        self.grade = grade
'''

'''
Co się stanie jeśli dodamy do klasy Person dodatkowy atrybut, na przykład adres?
W takim wypadku będziemy zmuszeni zaktualizować wszystkie metody init dla
wszystkich dziedziczących klas. Pracochłonne i podatne na błędy :(
Zamiast tego lepiej użyć **kwargsów
'''


class Person:
    def __init__(self, name, age, sex, address):
        '''
        Rozbudowaliśmy klasę Person o atrybut address
        '''
        self.name = name
        self.age = age
        self.sex = sex
        self.address = address


class Teacher(Person):
    def __init(self, salary, **kwargs):
        '''

        '''
        super().__init__(**kwargs)
        self.salary = salary


class Student(Person):
    def __init__(self, grade, **kwargs):
        '''
        2. Następuje próba rozpakowania przkazanych w kroku
        pierwszym par klucz-wartość do argumentów funkcji.
        Udaje się to tylko dla argumentu 'grade', reszta trafia 
        do arguemtnu **kwargs, który oznaczą nieznaną liczbę
        tzw. keyworded arguments. Czyli nasze kwargsy wyglądają
        mniej-więcej tak:
        name='John Hopkins', age=17, sex='male', address='Neverland'
        '''
        super().__init__(**kwargs)
        '''
        3. Rozpakowujemy kwargsy w wywołaniu nadrzędnej metody __init__
        co oznacza, że wywołanie powyżej 'pod spodem' wygląda tak:
        super().__init__(name='John Hopkins', age=17, sex='male', address='Neverland')
        '''
        self.grade = grade


if __name__ == '__main__':
    student_data = {
        'name': 'John Hopkins',
        'age': 17,
        'sex': 'male',
        'grade': 'Twelfth grade',
        'address': 'Neverland',
    }

    '''
    1. Przekazujemy słownik jako kwargsy do metody __init__
    '''
    student = Student(**student_data)
