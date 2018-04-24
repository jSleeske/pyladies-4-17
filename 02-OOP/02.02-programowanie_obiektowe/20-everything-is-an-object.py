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
