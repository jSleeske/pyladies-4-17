def my_func(name, last_name, age, sex, occupation):
    '''
        Funkcja my_func przyjmuje 5 argumentów, nie ma zdefiniowanych argumentów domyślnych.
    '''
    print('{name} {last_name} is {age}-years-old {sex}, and is {occupation} by trade'.format(
        name=name,
        last_name=last_name,
        age=age,
        sex=sex,
        occupation=occupation,
    ))


if __name__ == '__main__':
    '''
        Typowy sposób wywołania funckcji my_func
    '''
    my_func('John', 'Kowalski', 45, 'male', 'programmer')

    #
    '''
        Może się zdarzyć, że dane potrzebne do wywołania funkcji przyjdą w liście/słowniku
        lub innej strukturze. Aby uniknąć żmudnego przepisywania przy wywołaniu, można użyć
        notacji * oraz **

        PS - ta żmudna notacja to:
        my_func(slownik['name'], slownik['last_name']...)
    '''
    params = ['John', 'Kowalski', 45, 'male', 'programmer']

    #
    '''
        Nie zadziała, albo zadziała w niechciany sposób, jeśli funkcja będzie miała zdefiniowane
        wartości domyślne dla argumentów.
    '''
    # my_func(params)
    # my_func([param for param in params])

    #
    '''
        Działający sposób - oczywiście pod warunkiem, że ilość elementów w liście params będzie
        odpowiadać ilości argumentów przyjmowanych przez funkcję my_func, oraz, że będą one w
        pożądanej kolejności
    '''
    my_func(*params)

    #
    '''
        Inny prawidłowy sposób wywołania funkcji my_func - wskazujemy jaką wartość 
        przypisujemy do danego argumentu. Kolejność nie ma znaczenia!
    '''
    my_func(name='John', last_name='Kowalski', age=45,
            sex='male', occupation='programmer')
    my_func(sex='male', last_name='Kowalski', age=45,
            occupation='programmer', name='John')

    '''
        Jak osiągnąć taki efekt nie martwiąc się o to, czy dane są w poprawnej kolejności?
        Za pomocą keyworded args (**kwargs)!
    '''
    params = {
        'name': 'John',
        'occupation': 'programmer',
        'last_name': 'Kowalski',
        'sex': 'male',
        'age': 45,
    }

    '''
        Przekazujemy słownik poprzedzony '**', dzięki czemu uzyskamy efekt taki jak nieco wyżej!
    '''
    my_func(**params)
