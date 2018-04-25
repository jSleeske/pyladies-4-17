'''
W Pythonie wszystko jest obiektem, np. takie wyrażenie
'''
# x = str('Ala ma kota')
x = 'Ala ma kota'
'''
stworzy nowy obiekt klasy str, który posiada róznie atrybuty i metody
'''
# Metody obiektu klasy str
x.capitalize()
x.isalpha()
#

'''
W Pythonie wszystkie klasy niejawnie dziedziczą po klasie object. Klasa object
jest więc klasą bazową wszystkich innych klas.
'''
o = object()

'''
Klasa object definiuje wspólne metody dla wszystkich dziedziczących klas, m. in. 
metodę __init__() oraz metodę __str__()
'''


'''
W Pythonie funkcje też są obiektami, posiadają atrybuty i możemy je przypisywać
do zmiennych.
'''


def greet(name):
    '''
    To jest tzw docstring funkcji
    '''
    print(f'Hello {name}!')


'''
Przy uruchamianiu kodu w miejscu definicji funkcji zostanie
stworzony obiekt funkcji, jego nazwą będzie nazwa funkcji, np.
w tym przypadku będzie będzie on dostepny pod zmienną greet
'''

'''
Atrybut __doc__ przechowuje w sobie docstring funkcji (jeśli
go zdefiniujemy).
'''
print(greet.__doc__)  # To jest tzw docstring funkcji

'''
Dodając nawiasy okrągłe wywołujemy funkcję!  
'''
print(greet('Jan'))  # Hello Jan

say_hello = greet
'''
say_hello wskazuje teraz na ten sam obiekt funkcji!
'''

say_hello('PyLadies')  # ?

'''
Funkcje możemy przekazywać do innych funkcji, tak samo jak
każdy inny obiekt!
'''


def call_a_function_with_param(param, func):
    func(param)


call_a_function_with_param('John', greet)  # ?
