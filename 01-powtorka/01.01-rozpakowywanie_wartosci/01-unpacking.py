'''
    Swap in place - bez potrzeby definiowania dodatkowej zmiennej tymaczasowej
'''
a = 3
b = 4

a, b = b, a
# print(a, b)


'''
    Rozpakowywanie wartości - listy
'''
a_list = [1, 2, 3, 4, 5]

'''
    Nie zadziała, po prawej mamy 5 elementów w tablicy, po lewej tylko 3 zmienne
'''
# first, all_in_the_middle, last = a_list

'''
    Zadziała, użycie gwiazdki przed nazwą zmiennej sprawi, że część wartości zostanie "spakowana" do listy
'''
first, *all_in_the_middle, last = a_list
# print(first, all_in_the_middle, last) # 1 [2, 3, 4] 5

*all_other, last = a_list
# print(all_other, last) # [1, 2, 3, 4] 5

first, *all_other = a_list
# print(first, all_other) # 1 [2, 3, 4, 5]

'''
    Nie zadziała, python nie wie ile miałby przypisać do każdej z list :/
'''
# *some_from_start, middle_one, *some_from_end = a_list
# print(some_from_start, middle_one, some_from_end) # SyntaxError: two starred expressions in assignment


'''
    Rozpakowywanie wartości - słowniki
'''
a_dict = {
    'name': 'John',
    'last_name': 'Kowalski',
    'age': 45,
    'sex': 'male',
    'occupation': 'programmer',
}

'''
    Zadziała, domyślnie rozpakuje klucze
'''
first_key, *other_keys, last_key = a_dict
# print(first_key, other_keys, last_key) # name ['last_name', 'age', 'sex'] occupation

'''
    Zadziała, rozpakuje wartości do zmiennych
'''
name, *other_info, occupation = a_dict.values()
# print(name, other_info, occupation) # John ['Kowalski', 45, 'male'] programmer
