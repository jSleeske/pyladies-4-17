'''
Jedną z podstawowych zasad pisania kodu jest DRY - Don't Repeat Yourself.
Spójrzymy na poniższy przykład
'''


class Teacher:
    def __init__(self, name, age, sex, address,
                 years_of_employment, salary):
        self.name = name
        self.age = age
        self.sex = sex
        self.address = address
        self.years_of_employment = years_of_employment
        self.salary = salary


class Student:
    def __init__(self, name, age, sex, address, grade):
        self.name = name
        self.age = age
        self.sex = sex
        self.address = address
        self.grade = grade


'''
Jak łatwo zauważyć obie klasy mają dużą część wspólna - są
to atrybuty: name, age, sex oraz address
Jak więc przestać się powtarzać? Stosując dziedziczenie
'''
