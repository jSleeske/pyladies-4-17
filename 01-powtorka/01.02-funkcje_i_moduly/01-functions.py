'''
    Wyobraźmy sobie, że każdy print odpowiada dłuższemu kawałkowi kodu.
    Jeśli napiszemy to raz i nigdy nie będziemy chcieli tego zmieniać, to
    nie jest to koniec świata. Jeśli jednak będziemy chcieli kiedyś wrócić
    do tego kodu, aby go poprawić/rozbudować może być to ciężkie, bo całość
    będzie jednym wielkim blokiem kodu i 'wgryzienie się' w sposób jego 
    działania może nam zająć dużo za dużo czasu.
'''

'''
    print("Making sandwich...")
    print('Slicing bread')
    print('Spreading butter on bread')
    print('Adding cheese to sandwich')
    print('Washing tomato')
    print('Peeling tomato')
    print('Slicing tomato')
    print('Adding tomato to sandwich')
    print('Washing cucumber')
    print('Slicing cucumber')
    print('Adding cucumber to sandwich')
    print('Sandwich ready!')
'''

'''
    Wykorzystując zasady takie jak DRY oraz KISS możemy przerobić ten program 
    tak, aby jego modyfikacja w przyszłości oraz ogólne zrozumienie działania
    było dużo łatwiejsze.
'''


def apply_spread(spread):
    print(f'Spreading {spread} on sandwich')


def slice_bread(bread):
    print(f'Slicing {bread}')


def add_vegetable(vegetable):
    print(f'Washing {vegetable}')
    print(f'Slicing {vegetable}')
    print(f'Adding {vegetable} to sandwich')


def make_sandwich(bread='bread', spread='butter', vegetables=None):
    print("Making sandwich...")
    slice_bread(bread)
    apply_spread(spread)
    if vegetables:
        for vegetable in vegetables:
            add_vegetable(vegetable)
    print('Sandwich ready!')


if __name__ == '__main__':
    make_sandwich(vegetables=['tomato', 'cucmber', 'onion', 'garlic'])

'''
    Przedstawiony powyżej podział jest jedynie przykładowy, sposobów na pisanie
    czystego kodu jest dużo!
'''
