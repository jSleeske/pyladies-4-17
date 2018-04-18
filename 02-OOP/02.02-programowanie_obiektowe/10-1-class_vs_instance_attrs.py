class Person:
    name = 'John'

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    joe = Person('Joe')
    print(joe.name)     # Joe
    print(Person.name)  # John

'''
    W Pythonie poza atrybutami instancji (tymi, które inicjalizujemy
    np: za pomocą self.attr_name = value, albo obj.attr_name = value)
    istnieją także atrybuty klasowe. Definiuje się je najczęściej w samej
    klasie, a odwołuje się do nich poprzez NazwaKlasy.nazwa_atrybutu.

    Można się do nich odwołać także poprzez instancję, ale tylko wtedy jeśli 
    nie będzie ona posiadać własnego atrybutu o takiej samej nazwie.

    Wartości atrybutów klasowych są współdzielone pomiędzy wszystkimi obiektami
    danej klasy. 
'''
