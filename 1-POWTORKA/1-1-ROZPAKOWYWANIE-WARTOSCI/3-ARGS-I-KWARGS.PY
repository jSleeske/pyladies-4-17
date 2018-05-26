'''
Co jeśli chcemy mieć metodę, która przyjmuje dowolną ilość argumentów?

Proszę bardzo!
'''


def unlimited_power_of_args(*args):
    # args bez * na początku to tupla!
    for index, arg in enumerate(args):
        print(f'Arg {index}: {arg}')


unlimited_power_of_args('Ala', 'ma', 'kota')
unlimited_power_of_args('Chrząszcz', 'brzmi', 'w',
                        'trzcinie', 'w', 'Szczebrzeszynie')

'''
A jeśli chcemy przyjąć dowolną ilość kwargsów?

Nie ma problemu!
'''


def unlimited_power_of_kwargs(**kwargs):
    # kwargs bez ** na początku to słownik!
    for key, value in kwargs.items():
        print(f'Key: {key}, value: {value}')


unlimited_power_of_kwargs(kot='Filemon', pies='Reksio')
unlimited_power_of_kwargs(kot='Filemon', kot2='Garfield', pies='Reksio')


'''
Hmmm, a można to połączyć?

Jasne!
'''


def unlimited_power_of_args_and_kwargs(*args, **kwargs):
    print('Recieved following args:', args)
    print('Recieved following kwargs:', kwargs)


unlimited_power_of_args_and_kwargs('Ala', 'ma', zwierze='kot')

'''
Jedyny warunek? Przy wywołaniu zaczynamy od argsów, kwargsy zawsze na końcu!

Tak jest źle i nie zabangla:
>>> unlimited_power_of_args_and_kwargs(kto='Ala', 'ma', zwierze='kot')
'''

'''
Wow, a można wrzucić jeszcze nazwane argumenty?

Oczywiście, że można!
'''


def ohh_my_god_python_is_great(name, animal, *args, **kwargs):
    print('Name:', name)
    print('Animal:', animal)
    print('Args', args)
    print('Kwargs', kwargs)


my_args = ('Chrząszcz', 'brzmi', 'w', 'trzcinie')
my_kwargs = {
    'rzeczownik': 'Chrząszcz',
    'czasownik': 'brzmi',
}
ohh_my_god_python_is_great('Ala', 'kot', *my_args)
ohh_my_god_python_is_great('Ala', *my_args, **my_kwargs)
