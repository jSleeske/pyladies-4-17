class Person:
    '''
    Klasa Person - klasa nadrzędna, do której 'wyciągamy'
    część wspólną, czyli bazę dla wszystkich obiektów dziedziczących
    '''

    def __init__(self, name, age, sex, address):
        self.name = name
        self.age = age
        self.sex = sex
        self.address = address

    def get_info(self):
        '''
        Każdy obiekt klasy dziedziczącej będzie miał dostęp do metod i
        atrybutów klasy bazowej.
        '''
        return '{name} is {age} years old'.format(
            name=self.name,
            age=self.age,
        )


class Teacher(Person):
    '''
    W nawiasach okrągłych definujemy klasy po których dziedziczy
    nasza nowa klasa - w tym przypadku po klasie Person. Możmey dziedziczyć
    po więcej niż jednej klasie.
    '''

    def __init__(self, name, age, sex, address,
                 years_of_employment, salary):
        '''
        Jeśli nadpisujemy metodę __init__ klasy bazowej
        musimy ją jawnie wywołać :/
        super() odnosi się do klasy bazowej, na której następnie
        wywołujemy metodę __init__, natomiast wywołanie przez super()
        sprawi, że w metodzie __init__ 'self' będzie wskazywało obiekt klasy
        Teacher...
        '''
        super().__init__(name, age, sex, address)
        self.years_of_employment = years_of_employment
        self.salary = salary


class Student(Person):
    def __init__(self, name, age, sex, address, grade):
        super().__init__(name, age, sex, address)
        self.grade = grade


if __name__ == '__main__':
    student = Student('John Hopkins', 17, 'male',
                      'Oak Avenue 1337, Portland, Oregon', 'Twelfth grade')
    teacher = Teacher('Mary Poppins', 35, 'female',
                      'Neverland Street 25, Portland, Oregon', 7, 2500)

    print(student.get_info())
    print(teacher.get_info())

'''
Klasa Student i Teacher dziedziczą teraz po klasie Person,
która jest dla nich klasą bazową. 
Taki podział ma sens, bo wydrębniliśmy wszystkie cechy wspólne, które
posiada każdy student i nauczyciel, co więcej jeśli postanowimy stworzyć
nową klasę reprezentującą na przykład woźnych - też zapewne będą mogli
dziedziczyć po klasie Person i ją rozszerzać odpowiednimi atrybutami.
Tak samo jeśli uznamy, że każda z klas powinna być reprezentowana przez
dodatkowy atrybut, np. nazwisko, to zmianę będziemy museli dokonać w 
mniejszej ilości miejsc
'''
