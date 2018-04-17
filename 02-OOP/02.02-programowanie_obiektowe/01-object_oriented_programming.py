'''
    programowanie obiektowe (ang. object-oriented programming) 
    – paradygmat programowania, w którym programy definiuje się 
    za pomocą obiektów – elementów łączących stan (czyli dane, 
    nazywane najczęściej polami) i zachowanie (czyli procedury, 
    tu: metody). Obiektowy program komputerowy wyrażony jest jako 
    zbiór takich obiektów, komunikujących się pomiędzy sobą w celu 
    wykonywania zadań.
                                                    [wikipedia.pl]

    ...czyli tworzymy pewne obiekty, które przechowują informacje o 
    danych jak i o funkcjach za pomocą których na tych danych można 
    operować. Istnieje powiązanie pomiędzy danymi i funkcjami!
'''


'''
    Każdy z tych słowników reprezentuje zbiór danych, na których
    być może będziemy chcieli wykonać pewne operacje!
'''

[
    {
        'name': 'John',
        'age': 45,
        'sex': 'male',
        'occupation': 'janitor',
    },
    {
        'name': 'Kate',
        'age': 34,
        'sex': 'female',
        'occupation': 'teacher',
    },
    {
        'name': 'Rick',
        'age': 17,
        'sex': 'male',
        'occupation': 'student',
    },
]

'''
    Ale na razie każdy z nich jest po prostu strukturą przechowującą dane :(
    
    PS - składnia dostępu do wartości w słowniku: a_dict['key']
'''
